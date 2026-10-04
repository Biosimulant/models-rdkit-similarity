# Molecular similarity search with RDKit

Status: NOT_STARTED  
Prepared: 2026-10-03  
Discovery: No matching named capability found in the accessible release inventory and owned-project searches on this date. Recheck before execution.  
Scope: Public hosting candidate, subject to exact asset/license and runtime preflight; not a completed legal clearance or deployment.

## Goal

Publish and host a CPU Lab that ranks molecules from a user-supplied collection by structural similarity to a query and shows the matched structures and exact scoring definition.

## Source and licensing decision

[RDKit fingerprints and similarity](https://www.rdkit.org/docs/GettingStartedInPython.html) and [BSD license](https://github.com/rdkit/rdkit).

RDKit is BSD-3-Clause. Start with a user-uploaded collection and a small original example fixture, avoiding unlicensed commercial databases. Public sample data must have documented redistribution permission.

## Execution prompt

Work on this item end to end using Biosimulant MCP for Hub discovery, immutable workspaces, managed execution, retained artifacts, qualification, publication and hosting. Recheck the live Hub and owned private projects before creating a Lab; resume a matching implementation rather than making a duplicate. This brief is a proposed first-release contract, not evidence that the sources, checkpoints or example inputs have already been retained.

Inspect current Biosimulant authoring, visualization, compute and hosting contracts. Prepare an item-specific MRS/MTS with the exact inputs, units, constraints, output views and acceptance checks below. Verify real source artifacts and licenses before authoring. Freeze the model/runtime, fixtures, numerical tolerances and intended use before final verification; do not weaken failing criteria to publish. If inputs, rights or runtime support are missing, preserve the precise blocker and leave the item incomplete.

For repository development follow /Users/demi/Documents/projects-local/bsim/AGENTS.md: synchronize staging from current main while preserving staging-only work; use an isolated staging worktree when needed; commit/push staging only. Keep production on Modal. Do not merge main or redeploy production without fresh explicit approval after a concrete staging review. Distinguish local/isolated checks from end-to-end staging and hosted checks.

Prefer existing pretrained artifacts or deterministic tools; do not start training or large sweeps without an approved item-specific need and cost plan. Obtain a new bounded compute budget for this item; the colony-counter budget/approvals do not transfer. Batch exact plans where supported. Respect live MCP approvals for changes, managed compute, public publication and hosting; prepare the concrete reviewable subject before requesting consequential approval.

Implement the actual user-facing inference/analysis inputs and results below, with reusable visual outputs and declared visualization requirements. Finish the approved public release and hosting flow, then verify listing, non-owner access, real hosted inference, downloads and sample results. A published training graph, empty result page or local-only demo is incomplete.

### Scientific task and interface

Original request: “Find similar molecules to these compounds.” This is a search against an explicitly identified collection; do not imply it searches all known chemistry.

Inputs: one query SMILES, CSV collection with molecule_id and smiles (≤10,000 rows initially), top_k between 1 and 100, and minimum similarity in [0,1]. Version 1 uses Morgan fingerprints, radius 2, 2048 bits, with a declared chirality setting, and Tanimoto similarity. Expose this definition next to the result.

Outputs: ranked IDs, original and canonical SMILES, score, exact-match flag, invalid-row report, collection checksum, fingerprint parameters and duplicate policy. Include 2D query/hit drawings, a score bar plot and downloadable rankings. Equal scores sort deterministically by a documented stable ID rule. Keep genuine duplicates traceable rather than deleting them silently.

Do not send query molecules or uploaded collections to a third-party search service. Similarity is not evidence of equal potency, activity, toxicity or patent status.

### Compute and rollout scope

CPU only; pilot uses ≤100 example molecules, ≤120 seconds. Benchmark the 10,000-row upper bound before enabling it.

Measure the pilot before increasing bounds. If a public inference endpoint would exceed its resource or time limits, adjust the proposed product scope before approval; do not queue unbounded jobs.

### Item-specific acceptance criteria

- [ ] A1: An identical query and collection molecule scores 1.0; all scores stay within [0,1]. Compare every score and complete ranking on a frozen small fixture against independent pinned RDKit calls to within 1e-12.
- [ ] A2: Top_k, threshold and tie handling match the published contract, including no matches, repeated compounds, equivalent SMILES and invalid collection rows.
- [ ] A3: A chiral-pair fixture verifies the declared chirality setting; changing this setting requires a new release or explicit recorded configuration.
- [ ] A4: Collection identity, number of valid/searched/invalid entries and query checksum are retained. Every displayed hit links back to its original collection ID.
- [ ] A5: A public study compares two similarity thresholds on the same example collection and explains the resulting change in hit count; the UI makes the searched collection and limits clear.

### Public hosting completion criteria

- [ ] H1: The exact release records code, model/parameter files, ancillary data, sample fixtures, dependency versions/digests and applicable license/attribution obligations; there are no unresolved rights for assets actually shipped or used in the public service.
- [ ] H2: Every item-specific check below has linked evidence. Parity and small demonstrations are labelled accurately; neither is presented as broad biological validation.
- [ ] H3: A completed managed run has non-empty typed results and required visuals; retrieved artifact byte sizes and SHA-256 digests are independently verified. A matching Passport is retained with its limitations.
- [ ] H4: The Lab has a public immutable release, is listed and discoverable on the public Hub, and its page opens as a non-owner. Invocation authentication/payment requirements, if any, are explicit; users need no private owner API key or local software installation.
- [ ] H5: Hosting is active for that exact release on the approved Modal setup. A cold invocation and a subsequent invocation of the declared example accept the real user input, produce the declared outputs and meet frozen limits. Baseline example inference requires no undeclared online service.
- [ ] H6: The Results page contains at least one deliberately public, legally shareable example run with visuals and downloadable artifacts. The item-specific comparison is retained as an actual experiment/study and visible in Experiments when supported. If the platform cannot expose this, record a blocker instead of calling an empty page done.
- [ ] H7: Record measured cold/warm latency, peak memory/VRAM where available, provider compute spend, upload/request bounds, timeout/cancellation behavior and idle resource policy. Release inputs are isolated between users; no private user data or signed asset URLs appear in public examples.
- [ ] H8: Deliver exact staging commit(s), release reference, public URL, hosting identity, run/experiment/Passport references, evidence summary, outstanding limitations and rollback/disable instructions. Update this file and the index only after verifying completion.

## Completion record — fill after execution

- Status: NOT_STARTED / IN_PROGRESS / BLOCKED / DONE
- Completed date:
- MRS/MTS and frozen acceptance version:
- Exact source/model/runtime identities:
- License evidence and notices:
- Staging commit(s), environment and test evidence:
- Public release reference and Hub URL:
- Hosting identity and hosted example invocation:
- Public run, experiment and Passport:
- Measured latency, resource usage and cumulative spend:
- Caveats, blockers and rollback/disable state:

Mark DONE only when the goal and all applicable criteria are evidenced. An omitted criterion needs an explicitly approved scope change; do not check it off as passed.

