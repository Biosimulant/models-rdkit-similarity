# Modeling Technical Specification: RDKit Molecular Similarity Search

## 1. Document Control
MTS identifier: RDKit-Molecular-Similarity-MTS
Version: 1.0.0
Status: Approved
Last revised: 2026-10-04
MRS: RDKit-Molecular-Similarity-MRS version 1.0.0, Approved by explicit user goal.
Owner: demi; Codex implements. Approval covers implementation, not consequential MCP plans.

Revision History
1.0.0 — 2026-10-04 — Fixed finite RDKit adapter implementing approved exact brief. Protected MTS scaffolder failed integrity check in both available skill copies; master left unchanged and document authored independently against required section/traceability validator.

## 2. Technical Decision Summary
MTS-001: Freeze RDKit 2025.9.1, biosimulant 0.0.34, NumPy 2.2.6, Pillow 11.3.0 and Python 3.12. Author one finite search adapter. No fitting, weights, external database or online runtime services.

## 3. Scope, Boundaries, and Assumptions
Exact MRS inputs/outputs, limits, identities, scoring and intended use preserved. No inherited compute/publication approval from descriptors or CFU. Linux x86_64 retained checksum-verified native drawing assets; macOS used only for local development.

## 4. MRS Traceability
| MRS requirement | Component/decision | Test or protocol | Evidence | Owner | Unchanged criterion |
| --- | --- | --- | --- | --- | --- |
| MRS-001 | search.py and composed runtime | A1 | reports/acceptance.md | demi / Codex | An identical query and collection molecule scores 1.0; all scores stay within [0,1]. Compare every score and complete ranking on a frozen small fixture against independent pinned RDKit calls to within 1e-12. |
| MRS-002 | search.py and composed runtime | A2 | reports/acceptance.md | demi / Codex | Top_k, threshold and tie handling match the published contract, including no matches, repeated compounds, equivalent SMILES and invalid collection rows. |
| MRS-003 | search.py and composed runtime | A3 | reports/acceptance.md | demi / Codex | A chiral-pair fixture verifies the declared chirality setting; changing this setting requires a new release or explicit recorded configuration. |
| MRS-004 | search.py and composed runtime | A4 | reports/acceptance.md | demi / Codex | Collection identity, number of valid/searched/invalid entries and query checksum are retained. Every displayed hit links back to its original collection ID. |
| MRS-005 | search.py and composed runtime | A5 | reports/acceptance.md | demi / Codex | A public study compares two similarity thresholds on the same example collection and explains the resulting change in hit count; the UI makes the searched collection and limits clear. |
| MRS-006 | MCP lifecycle and public verification | H1 | reports/acceptance.md | demi / Codex | The exact release records code, model/parameter files, ancillary data, sample fixtures, dependency versions/digests and applicable license/attribution obligations; there are no unresolved rights for assets actually shipped or used in the public service. |
| MRS-007 | MCP lifecycle and public verification | H2 | reports/acceptance.md | demi / Codex | Every item-specific check below has linked evidence. Parity and small demonstrations are labelled accurately; neither is presented as broad biological validation. |
| MRS-008 | MCP lifecycle and public verification | H3 | reports/acceptance.md | demi / Codex | A completed managed run has non-empty typed results and required visuals; retrieved artifact byte sizes and SHA-256 digests are independently verified. A matching Passport is retained with its limitations. |
| MRS-009 | MCP lifecycle and public verification | H4 | reports/acceptance.md | demi / Codex | The Lab has a public immutable release, is listed and discoverable on the public Hub, and its page opens as a non-owner. Invocation authentication/payment requirements, if any, are explicit; users need no private owner API key or local software installation. |
| MRS-010 | MCP lifecycle and public verification | H5 | reports/acceptance.md | demi / Codex | Hosting is active for that exact release on the approved Modal setup. A cold invocation and a subsequent invocation of the declared example accept the real user input, produce the declared outputs and meet frozen limits. Baseline example inference requires no undeclared online service. |
| MRS-011 | MCP lifecycle and public verification | H6 | reports/acceptance.md | demi / Codex | The Results page contains at least one deliberately public, legally shareable example run with visuals and downloadable artifacts. The item-specific comparison is retained as an actual experiment/study and visible in Experiments when supported. If the platform cannot expose this, record a blocker instead of calling an empty page done. |
| MRS-012 | MCP lifecycle and public verification | H7 | reports/acceptance.md | demi / Codex | Record measured cold/warm latency, peak memory/VRAM where available, provider compute spend, upload/request bounds, timeout/cancellation behavior and idle resource policy. Release inputs are isolated between users; no private user data or signed asset URLs appear in public examples. |
| MRS-013 | MCP lifecycle and public verification | H8 | reports/acceptance.md | demi / Codex | Deliver exact staging commit(s), release reference, public URL, hosting identity, run/experiment/Passport references, evidence summary, outstanding limitations and rollback/disable instructions. Update this file and the index only after verifying completion. |

## 5. Architecture and Data Flow
MTS-002: Public typed inputs map to search module. One execute(inputs, *, context) call under ExecutionPolicy.ONCE_BEFORE_RUN unwraps BioSignal.value, validates CSV/SMILES, fingerprints query and each valid row, sorts/filters and emits typed report, threshold hit_count and file outputs. visualize reads computed state only. No graph edges or temporal delay; world duration=1 step=1 is orchestration only.

## 6. Data Implementation
MTS-003: Exact upload bytes hash before UTF-8-sig decoding. Record original query UTF-8 SHA-256 independently. Reader enforces exact two columns, bounded row count and regular files. IDs/SMILES kept byte-faithful in JSON. All valid rows searched once, no deduplication; canonical isomeric representations used only for identity. File-download CSV protects leading formula characters. Hand-authored public fixture under BSD-3-Clause.

## 7. Input, Output, and Error Contracts
Typed scalar str query/CSV/file, int64 top_k and float64 minimum_similarity. record report schema hits=json,invalid_rows=json,receipt=json with emitted_unit=1; hit_count int64 count; five typed file outputs CSV/JSON/PNG. Every score dimensionless; row counts count. Invalid query/schema/limits reject with bounded error, invalid collection molecules retain row index/ID/code. Inclusive threshold, then top_k; stable Unicode ID and row-index ties. No-hit report/image/text and empty CSV/JSON supported.

## 8. Model Method and Uncertainty
MTS-004: GetMorganGenerator(radius=2,fpSize=2048,includeChirality=True) using pinned upstream defaults recorded in receipt, GetFingerprint and TanimotoSimilarity. All fragments preserved; no neutralization/desalt/tautomer change. Exact_match iff canonical isomeric SMILES equal; collisions are not identity. Deterministic bit similarity has no biological confidence or activity probability.

## 9. Biosimulant Fit Assessment
Biosimulant fit: Adapter fit
Frozen RDKit scientific implementation remains authoritative; Biosimulant adds typed packaging, reusable visualization, managed retention, Passports and hosting requested by the user. No platform readiness or biological validation inferred.

## 10. Biosimulant Realization
MTS-005: BioModule MolecularSimilarity with inputs()/outputs(), execute and matching manifest biosim.execution_policy=once_before_run. reset instance result state each invocation, fresh private temporary output directory, file modes 600/root700. bar/table values match typed hits; image contains query and computed ranked structures; text exposes exact scoring, searched collection checksum and constraints. image and text always required; bar/table required for nonempty example. Five downloadable artifacts retained alongside nonempty workspace-results.

## 11. Verification and Test Design
MTS-006: Independent pinned AllChem.GetMorganFingerprintAsBitVect and DataStructs calls on complete frozen fixture at tolerance 1e-12. Test exact hits, equivalence, repeated IDs, inclusive threshold, top_k edges, Unicode ties, no matches, malformed/invalid/oversize inputs, chiral enabled versus disabled control, counts/checksums, visualization numeric parity and repeated invocation isolation. Composed CLI with real CSV-file and text inputs plus retained artifacts. Pilot100 before benchmark10000; measure peak process RSS and duration. Local/isolated tests never replace managed artifacts or hosted checks.

## 12. Reproducibility, Security, Performance, and Cost
MTS-007: CPU0.5, RAM512MiB, free Modal profile selected from live catalog; no GPU/training. Frozen application timeout120s. Provider cost requires exact MCP plan. Max10000 rows,2MiB,8192 SMILES chars,256 atoms/512 bonds; top100 drawings. No network search, URL inputs or public private data. Native assets have independently checked provenance and full notices. Actual provider bill/peak resources reported unavailable when platform does not expose them.

## 13. Model Lock, Release, and Operations
MTS-008: Retain file hashes in freeze-manifest before final verification. Ship fixtures/runtime/assets/licenses; release version0.1.0. Managed pilot/study first, Passport/artifact review, separately approved immutable public release, Hub listing then exact Modal public hosting plan. No core deployment. Hosting scale-to-zero/max1 proposed; verify live plan before approval. Rollback read current hosting revision then pause/withdraw; visibility/listing reversal if authorized. Preserve failed runs and criteria.

## 14. Mechanistic Technical Module Applicability
Not applicable: finite graph-ranking has no dynamical equations, solver, temporal state, interventions or biological mechanism.

## 15. Risks, Decisions, and Open Questions
Fingerprint collisions, unsupported chemistry, runtime drawing dependencies, platform CSV/public-study/hosting gaps remain explicit. No broadened claims; no weakened acceptance. All failed checks remain recorded.

## 16. References and Glossary
Approved RDKit-Molecular-Similarity-MRS1.0.0, complete brief reports/brief.md; upstream RDKit Release_2025_09_1 commit237a1d9027c800784afed8788540f38a3aa595f8; sources and NOTICE.md.
