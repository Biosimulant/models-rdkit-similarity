"""Finite, bounded structural similarity against exactly the supplied collection."""
from __future__ import annotations

import base64
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import tempfile
import time

from .linux_libraries import ensure_linux_libraries
ensure_linux_libraries()

from biosim import BioModule, ExecutionPolicy, SignalSpec
from rdkit import Chem, DataStructs, RDConfig, rdBase
from rdkit.Chem import Draw, rdFingerprintGenerator
from rdkit.Chem.Draw import rdMolDraw2D

MAX_ROWS = 10000
MAX_BYTES = 2 * 1024 * 1024
MAX_SMILES = 8192
MAX_ATOMS = 256
MAX_BONDS = 512
TIMEOUT = 120
PARAMETERS = {"algorithm": "Morgan", "radius": 2, "fpSize": 2048,
              "includeChirality": True, "useBondTypes": True,
              "countSimulation": False, "includeRingMembership": True,
              "onlyNonzeroInvariants": False, "includeRedundantEnvironments": False,
              "metric": "Tanimoto", "score_unit": "1",
              "definition": "on-bit intersection / on-bit union; RDKit TanimotoSimilarity"}
DUPLICATES = "Keep every valid collection row, including repeated IDs and equivalent SMILES; row_index distinguishes occurrences."
TIES = "Descending score, then exact molecule_id in ascending Unicode code-point order, then zero-based CSV data-row index."
CAVEAT = "Searches only the supplied collection. Structural similarity does not establish equal potency, activity, toxicity, safety or patent status. Fingerprint collisions can score 1 without structural identity."
FIELDS = ["rank", "row_index", "molecule_id", "original_smiles", "canonical_smiles", "score", "exact_match"]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def molecule(text):
    if not isinstance(text, str) or not text or len(text) > MAX_SMILES:
        raise ValueError("input_limit: SMILES must contain 1..8192 characters")
    parser = Chem.SmilesParserParams()
    parser.sanitize = False
    parser.parseName = False
    parser.allowCXSMILES = False
    with rdBase.BlockLogs():
        mol = Chem.MolFromSmiles(text, parser)
        if mol is None or mol.GetNumAtoms() == 0:
            raise ValueError("parse_error: unsupported or invalid SMILES")
        if mol.GetNumAtoms() > MAX_ATOMS or mol.GetNumBonds() > MAX_BONDS:
            raise ValueError("structure_limit: maximum 256 atoms and 512 bonds")
        if any(a.GetAtomicNum() == 0 or a.HasQuery() for a in mol.GetAtoms()):
            raise ValueError("unsupported_structure: wildcard/query atoms unsupported")
        try:
            Chem.SanitizeMol(mol)
            Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
        except Exception as exc:
            raise ValueError("sanitize_error: invalid molecular valence or aromaticity") from exc
    return mol


def collection_bytes(collection_csv="", collection_file=""):
    if not isinstance(collection_csv, str) or not isinstance(collection_file, str):
        raise ValueError("Collection text/file must be strings")
    if bool(collection_csv) == bool(collection_file):
        raise ValueError("Provide exactly one collection CSV text or uploaded CSV")
    if collection_file:
        path = Path(collection_file)
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
            raise ValueError("Collection must be a regular CSV file <=2 MiB")
        with path.open("rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
    else:
        raw = collection_csv.encode("utf-8")
    if len(raw) > MAX_BYTES:
        raise ValueError("Collection exceeds 2 MiB")
    return raw


def search(query_smiles, collection_csv="", collection_file="", top_k=10, minimum_similarity=0.0):
    if rdBase.rdkitVersion != "2025.09.1":
        raise RuntimeError("RDKit differs from frozen 2025.9.1 release")
    if type(top_k) is not int or not 1 <= top_k <= 100:
        raise ValueError("top_k must be an integer in 1..100")
    if isinstance(minimum_similarity, bool) or not isinstance(minimum_similarity, (int, float)) or not math.isfinite(minimum_similarity) or not 0 <= minimum_similarity <= 1:
        raise ValueError("minimum_similarity must be finite in [0,1]")
    start = time.monotonic()
    query = molecule(query_smiles)
    canonical_query = Chem.MolToSmiles(query, canonical=True, isomericSmiles=True)
    raw = collection_bytes(collection_csv, collection_file)
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Collection must be UTF-8") from exc
    reader = csv.DictReader(io.StringIO(text), strict=True)
    if reader.fieldnames != ["molecule_id", "smiles"]:
        raise ValueError("CSV header must be exactly molecule_id,smiles")
    generator = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048, includeChirality=True)
    query_fp = generator.GetFingerprint(query)
    valid, invalid, count = [], [], 0
    try:
        for index, row in enumerate(reader):
            if time.monotonic() - start > TIMEOUT:
                raise TimeoutError("Collection processing exceeded 120 seconds")
            count += 1
            if count > MAX_ROWS:
                raise ValueError("Collection exceeds 10000 rows")
            if None in row or any(v is None for v in row.values()):
                raise ValueError("Each CSV row must contain exactly two fields")
            original = {"row_index": index, "molecule_id": row["molecule_id"], "original_smiles": row["smiles"]}
            try:
                if not row["molecule_id"] or len(row["molecule_id"]) > 128:
                    raise ValueError("id_limit: molecule_id must contain 1..128 characters")
                mol = molecule(row["smiles"])
                canonical = Chem.MolToSmiles(mol, canonical=True, isomericSmiles=True)
                score = float(DataStructs.TanimotoSimilarity(query_fp, generator.GetFingerprint(mol)))
                valid.append({**original, "canonical_smiles": canonical, "score": score,
                              "exact_match": canonical == canonical_query})
            except ValueError as exc:
                invalid.append({**original, "error_code": str(exc).split(":", 1)[0], "error": str(exc)})
    except csv.Error as exc:
        raise ValueError("Malformed CSV") from exc
    if count == 0:
        raise ValueError("Collection requires at least one data row")
    valid.sort(key=lambda row: (-row["score"], row["molecule_id"], row["row_index"]))
    eligible = [row for row in valid if row["score"] >= minimum_similarity]
    hits = [{"rank": rank, **row} for rank, row in enumerate(eligible[:top_k], 1)]
    receipt = {"rdkit_version": rdBase.rdkitVersion, "adapter_version": "0.1.0",
               "query_original_smiles": query_smiles, "query_canonical_smiles": canonical_query,
               "query_sha256": sha(query_smiles.encode("utf-8")),
               "collection_sha256": sha(raw), "collection_size_bytes": len(raw),
               "collection_identity": "SHA-256 of exact submitted UTF-8 bytes including BOM/newlines",
               "collection_rows": count, "valid_entries": len(valid), "searched_entries": len(valid),
               "invalid_entries": len(invalid), "threshold_hit_count": len(eligible), "returned_hits": len(hits),
               "top_k": top_k, "minimum_similarity": minimum_similarity,
               "fingerprint_parameters": PARAMETERS, "duplicate_policy": DUPLICATES, "tie_policy": TIES,
               "exact_match_definition": "Equal canonical isomeric SMILES, not fingerprint equality",
               "standardization": "None; retain all fragments, charges, isotopes and stereochemistry",
               "limits": {"rows": MAX_ROWS, "collection_bytes": MAX_BYTES, "smiles_characters": MAX_SMILES,
                          "atoms": MAX_ATOMS, "bonds": MAX_BONDS, "timeout_seconds": TIMEOUT},
               "calculation_seconds": time.monotonic() - start, "caveat": CAVEAT}
    return {"hits": hits, "invalid_rows": invalid, "receipt": receipt}


class MolecularSimilarity(BioModule):
    execution_policy = ExecutionPolicy.ONCE_BEFORE_RUN

    def __init__(self):
        self.report = None
        self.artwork = None
        self.artwork_src = None

    def inputs(self):
        specs = {key: SignalSpec.scalar(dtype="str") for key in ("query_smiles", "collection_csv")}
        specs["collection_file"] = SignalSpec.scalar(dtype="str", value_type="file", format="csv")
        specs["top_k"] = SignalSpec.scalar(dtype="int64")
        specs["minimum_similarity"] = SignalSpec.scalar(dtype="float64")
        return specs

    def outputs(self):
        specs = {"report": SignalSpec.record(schema={"hits": "json", "invalid_rows": "json", "receipt": "json"}, emitted_unit="1"),
                 "hit_count": SignalSpec.scalar(dtype="int64", emitted_unit="count")}
        for name, fmt in [("rankings_csv", "csv"), ("rankings_json", "json"), ("invalid_csv", "csv"), ("receipt_file", "json"), ("drawings", "png")]:
            specs[name] = SignalSpec.scalar(dtype="str", value_type="file", format=fmt)
        return specs

    def execute(self, inputs, *, context):
        self.report = self.artwork = self.artwork_src = None
        values = {key: signal.value for key, signal in inputs.items()}
        if set(values) - set(self.inputs()):
            raise ValueError("Unknown input")
        self.report = search(**values)
        output = Path.cwd() / "outputs"
        output.mkdir(exist_ok=True)
        root = Path(tempfile.mkdtemp(prefix="molecular-similarity-", dir=output)).resolve()
        root.chmod(0o700)
        files = {name: root / filename for name, filename in [("rankings_csv", "rankings.csv"),
                 ("rankings_json", "rankings.json"), ("invalid_csv", "invalid-rows.csv"),
                 ("receipt_file", "receipt.json"), ("drawings", "molecules.png")]}
        for name, rows, fields in [("rankings_csv", self.report["hits"], FIELDS),
                ("invalid_csv", self.report["invalid_rows"], ["row_index", "molecule_id", "original_smiles", "error_code", "error"])]:
            with files[name].open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                for row in rows:
                    writer.writerow({k: "'" + v if isinstance(v, str) and v.startswith(("=", "+", "-", "@")) else v for k, v in row.items()})
        files["rankings_json"].write_text(json.dumps(self.report, ensure_ascii=False, allow_nan=False, indent=2))
        files["receipt_file"].write_text(json.dumps(self.report["receipt"], ensure_ascii=False, allow_nan=False, indent=2))
        # Draw the query plus up to 100 actual ranked hits; every legend retains row identity.
        molecules = [molecule(values["query_smiles"])] + [molecule(h["canonical_smiles"]) for h in self.report["hits"]]
        legends = ["QUERY"] + [f"#{h['rank']} row {h['row_index']} {h['molecule_id'][:24]}\nTanimoto={h['score']:.6f}" for h in self.report["hits"]]
        options = rdMolDraw2D.MolDrawOptions()
        options.fontFile = str(Path(RDConfig.RDDataDir) / "Fonts/Telex-Regular.ttf")
        image = Draw.MolsToGridImage(molecules, molsPerRow=4, subImgSize=(250, 200), legends=legends, drawOptions=options)
        image.save(files["drawings"])
        preview = image.copy()
        preview.thumbnail((1000, 2200))
        stream = io.BytesIO()
        preview.save(stream, format="PNG")
        if len(stream.getvalue()) > 1250000:
            raise RuntimeError("Drawing preview exceeds visual byte bound")
        self.artwork = str(files["drawings"])
        self.artwork_src = "data:image/png;base64," + base64.b64encode(stream.getvalue()).decode("ascii")
        for path in files.values():
            path.chmod(0o600)
        return {"report": self.report, "hit_count": self.report["receipt"]["threshold_hit_count"], **{k: str(v) for k, v in files.items()}}

    def visualize(self):
        if self.report is None:
            return []
        receipt = self.report["receipt"]
        hits = self.report["hits"]
        visuals = [{"schema_version": "1", "render": "image", "data": {
                    "source": {"kind": "artifact", "path": self.artwork}, "src": self.artwork_src,
                    "alt": "Query and ranked matched structures with original ID and collection row"}},
                   {"schema_version": "1", "render": "text", "data": {"text":
                    f"Searched collection {receipt['collection_sha256']}: {receipt['searched_entries']} valid of {receipt['collection_rows']} rows; {receipt['invalid_entries']} invalid. "
                    f"Threshold >= {receipt['minimum_similarity']}; {receipt['threshold_hit_count']} eligible; top {receipt['top_k']}. "
                    "Morgan radius=2, 2048 bits, chirality=True. Tanimoto = on-bit intersection / on-bit union, unit 1. "
                    + TIES + " " + DUPLICATES + " Limits: 10000 rows / 2 MiB; 256 atoms and 512 bonds per structure. " + CAVEAT}}]
        if hits:
            visuals += [{"schema_version": "1", "render": "bar", "data": {"items": [
                        {"label": f"{h['molecule_id']} (row {h['row_index']})", "value": h["score"], "unit": "1"} for h in hits]}},
                        {"schema_version": "1", "render": "table", "data": {"columns": FIELDS, "rows": [[h[k] for k in FIELDS] for h in hits]}}]
        return visuals
