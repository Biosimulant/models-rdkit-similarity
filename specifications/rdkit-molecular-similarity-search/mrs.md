# Model Requirements Specification: RDKit Molecular Similarity Search

## 1. Document Control
MRS identifier: RDKit-Molecular-Similarity-MRS
Version: 1.0.0
Status: Approved
Last revised: 2026-10-04
Owner: demi; evidence implementer: Codex.
Approval receipt: The 2026-10-04 user goal explicitly instructs implementation of the full brief exact contract and acceptance criteria. This authorizes requirements and implementation; exact MCP compute, public release and hosting plans remain separately approval-bound.

Revision History
1.0.0 — 2026-10-04 — Freeze unchanged brief requirements and original fixtures before final verification.

## 2. Executive Summary
Finite deterministic structural search against exactly the supplied collection; no training, online search or biological inference.

## 3. Biological Objective and Intended Use
Inspect structural similarity to a query, retaining original collection identity and IDs. Similarity establishes no equal potency, activity, toxicity, safety or patent status.

## 4. Model Definition and Scope
Selected type or types: deterministic chemical structural ranking. Morgan radius 2, 2048 bits, chirality enabled; Tanimoto bit intersection/union. One finite invocation; no biological time evolution.

## 5. Inputs
One query SMILES; exactly one uploaded UTF-8 CSV or equivalent pasted CSV, header molecule_id,smiles; 1..10000 data rows; top_k integer 1..100; minimum_similarity finite [0,1]. Product bounds: CSV 2 MiB, SMILES 8192 characters, ID 1..128 characters, 256 atoms/512 bonds per molecule. Invalid molecular rows report errors; malformed CSV rejects request. Uploaded bytes hash exactly including BOM/newlines; no third-party search. Preserve salts, isotopes and stereochemistry without standardization. Query or wildcard/unsupported graph rejection is explicit.

## 6. Outputs
Rank, zero-based data-row index, original ID/SMILES, canonical isomeric SMILES, dimensionless score [0,1], exact-match flag from canonical equality, invalid-row report, collection/query checksums, valid/searched/invalid counts, full parameters and duplicate policy. Inclusive threshold applied before top_k. Ties descend score then ascend exact Unicode ID then row index. Keep all duplicates traceable. Query/hit 2D drawings, dimensionless score bars, table and visible scoring/collection interpretation. No-hit view shows query plus explicit text and empty downloadable rankings; bar/table have no invented values. Download CSV/JSON, invalid CSV, receipt and PNG; JSON preserves exact text, CSV escapes formula-leading text.

## 7. Data, Assay, and Evidence Specification
Original public example.csv: ethanol, equivalent representation, repeat ID, propanol, butanol, ethylamine, acetate, benzene, chiral alanine pair, salt, invalid and empty SMILES. These are hand-authored software fixtures under repository BSD-3-Clause, not empirical biology or a commercial database. Upstream source, license, dependency distributions and native drawing library notices retained. No training or assay partitions needed.

## 8. Ground Truth or Estimand
Independently called pinned RDKit Morgan radius-2 bit fingerprints and TanimotoSimilarity, absolute tolerance 1e-12 on every score and complete ranking. Canonical identity tested separately from fingerprint score. No broad chemical or biological validation claim.

## 9. Generalization Domain
Supported molecular graphs within published input bounds, against supplied collection only. No potency/activity/toxicity/patent-status inference; small parity fixtures are not exhaustive chemistry validation.

## 10. Performance Requirements
CPU only; initial pilot <=100 molecules and <=120 seconds. Measure pilot before increasing bounds; benchmark 10000 rows before enabling the upper bound. Exact cost approval for managed compute; frozen 120-second wall-clock timeout. Cold/warm hosted limits verified separately from local timing.

## 11. Validation Plan
Freeze code/runtime/fixtures/parameters/tolerance before final checks. Independent upstream full parity, identity, score bounds, threshold/top_k/ties/duplicates/equivalence/no hits/invalid rows, chiral pair, input integrity/isolation, composed runtime visuals/downloads, 100-row pilot then 10000-row benchmark. Durable managed artifacts hashed independently and Passport retained. Non-owner public listing/example/study/hosting/cold/warm/downloads each independently verified. No prospective biological validation is claimed.

## 12. Acceptance and Traceability
Owner: demi; evidence implementer: Codex.

| ID | Brief ID | Unchanged acceptance criterion | Evidence |
| --- | --- | --- | --- |
| MRS-001 | A1 | An identical query and collection molecule scores 1.0; all scores stay within [0,1]. Compare every score and complete ranking on a frozen small fixture against independent pinned RDKit calls to within 1e-12. | reports/acceptance.md; not yet accepted |
| MRS-002 | A2 | Top_k, threshold and tie handling match the published contract, including no matches, repeated compounds, equivalent SMILES and invalid collection rows. | reports/acceptance.md; not yet accepted |
| MRS-003 | A3 | A chiral-pair fixture verifies the declared chirality setting; changing this setting requires a new release or explicit recorded configuration. | reports/acceptance.md; not yet accepted |
| MRS-004 | A4 | Collection identity, number of valid/searched/invalid entries and query checksum are retained. Every displayed hit links back to its original collection ID. | reports/acceptance.md; not yet accepted |
| MRS-005 | A5 | A public study compares two similarity thresholds on the same example collection and explains the resulting change in hit count; the UI makes the searched collection and limits clear. | reports/acceptance.md; not yet accepted |
| MRS-006 | H1 | The exact release records code, model/parameter files, ancillary data, sample fixtures, dependency versions/digests and applicable license/attribution obligations; there are no unresolved rights for assets actually shipped or used in the public service. | reports/acceptance.md; not yet accepted |
| MRS-007 | H2 | Every item-specific check below has linked evidence. Parity and small demonstrations are labelled accurately; neither is presented as broad biological validation. | reports/acceptance.md; not yet accepted |
| MRS-008 | H3 | A completed managed run has non-empty typed results and required visuals; retrieved artifact byte sizes and SHA-256 digests are independently verified. A matching Passport is retained with its limitations. | reports/acceptance.md; not yet accepted |
| MRS-009 | H4 | The Lab has a public immutable release, is listed and discoverable on the public Hub, and its page opens as a non-owner. Invocation authentication/payment requirements, if any, are explicit; users need no private owner API key or local software installation. | reports/acceptance.md; not yet accepted |
| MRS-010 | H5 | Hosting is active for that exact release on the approved Modal setup. A cold invocation and a subsequent invocation of the declared example accept the real user input, produce the declared outputs and meet frozen limits. Baseline example inference requires no undeclared online service. | reports/acceptance.md; not yet accepted |
| MRS-011 | H6 | The Results page contains at least one deliberately public, legally shareable example run with visuals and downloadable artifacts. The item-specific comparison is retained as an actual experiment/study and visible in Experiments when supported. If the platform cannot expose this, record a blocker instead of calling an empty page done. | reports/acceptance.md; not yet accepted |
| MRS-012 | H7 | Record measured cold/warm latency, peak memory/VRAM where available, provider compute spend, upload/request bounds, timeout/cancellation behavior and idle resource policy. Release inputs are isolated between users; no private user data or signed asset URLs appear in public examples. | reports/acceptance.md; not yet accepted |
| MRS-013 | H8 | Deliver exact staging commit(s), release reference, public URL, hosting identity, run/experiment/Passport references, evidence summary, outstanding limitations and rollback/disable instructions. Update this file and the index only after verifying completion. | reports/acceptance.md; not yet accepted |

Definition of Done: every A1–A5 and H1–H8 passes with linked evidence; missing evidence is incomplete, never waived implicitly.

## 13. Constraints, Risks, and Governance
All development/tests/commits/pushes staging only; preserve other work. Production remains Modal. Never transmit collections to a third-party search service. Exact MCP plans/digests and approval boundaries govern managed operations; no secret or signed URLs in public examples.

## 14. Reproducibility, Deliverables, and Handoff
Dedicated repository, MRS/MTS, frozen code/source/runtime/fixture/digest/license record, managed run/study/Passport, public release/URL, hosting identity, measured latency/cost/limits, precise blockers and rollback instructions. New version required for chirality or scoring changes.

## 15. Mechanistic Module Applicability
Not applicable: deterministic graph search has no kinetics, reactions or causal biological claims. The common core controls this computation.

## 16. Milestones and Responsibilities
Requirements and source freeze → staging implementation/tests → exact approved managed pilot → measured upper-bound benchmark → approved study → artifact/Passport review → separate public release approval → active approved Modal hosting → non-owner verification → DONE only if every criterion passes. demi owns approvals; Codex records evidence.

## 17. Open Questions and Decisions
No requirements are unresolved. Operational release gates await actual evidence: live CSV handling, public study exposure, deployment administrator permissions and provider telemetry. Unsupported capabilities remain blockers.

## 18. References and Glossary
https://www.rdkit.org/docs/GettingStartedInPython.html ; retained upstream commit 237a1d9027c800784afed8788540f38a3aa595f8, Release_2025_09_1. Tanimoto is a dimensionless bit-vector similarity, not a probability of activity. Exact full brief: reports/brief.md.
