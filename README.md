# RDKit Molecular Similarity Search

Biosimulant finite CPU Lab: search exactly your CSV collection using Morgan radius 2, 2048-bit fingerprints, chirality enabled, and Tanimoto on-bit intersection/union. Similarity scores are dimensionless and do not establish equal potency, activity, toxicity or patent status.

Status: staging implementation verified locally; awaiting exact MCP workspace approval and item-specific managed compute. Public Lab release and active hosting are not yet verified.

Inputs: query_smiles; exactly one of collection_csv or collection_file (UTF-8 CSV header molecule_id,smiles); top_k integer 1..100; minimum_similarity finite in [0,1], inclusive. Maximum 10000 rows, 2 MiB collection, 8192 SMILES characters, 256 atoms and 512 bonds per structure. An upper-bound staging benchmark is retained; hosted availability requires its own verification.

Outputs: ranked original IDs and SMILES, canonical isomeric SMILES, Tanimoto score, exact-match flag, original row index, invalid-row report, checksums, full fingerprint definition/counts/duplicate policy, query and matched 2D structures, score bars and CSV/JSON/PNG downloads. All duplicate rows remain; scores sort descending, exact Unicode ID ascending, then zero-based data-row index. Exact match is canonical isomeric equality, independent of fingerprint collisions. Salts/fragments, isotopes and stereochemistry are preserved without neutralization or tautomer standardization.

The original example collection is public and licensed BSD-3-Clause. Raising its threshold from 0.2 to 0.6 for ethanol reduces hits from six to three. This software demonstration is not broad biological validation. See reports/local-comparison.json; a retained public MCP experiment remains required.

Code and tests remain on staging. Production remains Modal. Dependency/native/font notices and checksums are retained in labs/molecular-similarity/sources. No weights, online chemical database or third-party search call. Python 3.12; biosimulant 0.0.34, RDKit 2025.9.1, NumPy 2.2.6 and Pillow 11.3.0.

Local verification: `python -m pytest labs/molecular-similarity/tests -q` then `python scripts/verify_runtime.py` and `python scripts/benchmark.py` in an isolated environment with requirements-test.txt. Local CLI runs create no managed Run or Passport. Every acceptance/hosting gate is tracked in reports/acceptance.md.

MRS/MTS: specifications/rdkit-molecular-similarity-search. Original brief: reports/brief.md. No production deployment or provider switch is authorized by these files. Once hosting exists, read current hosting revision and pause/withdraw it via Biosimulant MCP; preserve immutable evidence.
