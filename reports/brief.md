# Molecular similarity search with RDKit

Status: BLOCKED  
Prepared: 2026-10-03  
Discovery: Matching public similarity Lab 0.1.1 and its owned immutable workspace are verified. Reuse the dedicated models-rdkit-similarity staging implementation and existing workspace; do not create a duplicate.  
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

- [x] A1: An identical query and collection molecule scores 1.0; all scores stay within [0,1]. Compare every score and complete ranking on a frozen small fixture against independent pinned RDKit calls to within 1e-12.
- [x] A2: Top_k, threshold and tie handling match the published contract, including no matches, repeated compounds, equivalent SMILES and invalid collection rows.
- [x] A3: A chiral-pair fixture verifies the declared chirality setting; changing this setting requires a new release or explicit recorded configuration.
- [x] A4: Collection identity, number of valid/searched/invalid entries and query checksum are retained. Every displayed hit links back to its original collection ID.
- [ ] A5: A public study compares two similarity thresholds on the same example collection and explains the resulting change in hit count; the UI makes the searched collection and limits clear.

### Public hosting completion criteria

- [x] H1: The exact release records code, model/parameter files, ancillary data, sample fixtures, dependency versions/digests and applicable license/attribution obligations; there are no unresolved rights for assets actually shipped or used in the public service.
- [x] H2: Every item-specific check below has linked evidence. Parity and small demonstrations are labelled accurately; neither is presented as broad biological validation.
- [x] H3: A completed managed run has non-empty typed results and required visuals; retrieved artifact byte sizes and SHA-256 digests are independently verified. A matching Passport is retained with its limitations.
- [ ] H4: The Lab has a public immutable release, is listed and discoverable on the public Hub, and its page opens as a non-owner. Invocation authentication/payment requirements, if any, are explicit; users need no private owner API key or local software installation.
- [ ] H5: Hosting is active for that exact release on the approved Modal setup. A cold invocation and a subsequent invocation of the declared example accept the real user input, produce the declared outputs and meet frozen limits. Baseline example inference requires no undeclared online service.
- [ ] H6: The Results page contains at least one deliberately public, legally shareable example run with visuals and downloadable artifacts. The item-specific comparison is retained as an actual experiment/study and visible in Experiments when supported. If the platform cannot expose this, record a blocker instead of calling an empty page done.
- [ ] H7: Record measured cold/warm latency, peak memory/VRAM where available, provider compute spend, upload/request bounds, timeout/cancellation behavior and idle resource policy. Release inputs are isolated between users; no private user data or signed asset URLs appear in public examples.
- [ ] H8: Deliver exact staging commit(s), release reference, public URL, hosting identity, run/experiment/Passport references, evidence summary, outstanding limitations and rollback/disable instructions. Update this file and the index only after verifying completion.

## Completion record — BLOCKED, public release verified; active hosting incomplete

Updated 2026-10-04. Exact public release [demi/rdkit-molecular-similarity-search@0.1.0](https://hub.biosimulant.com/labs/f0291213-a063-4aeb-8981-8e0e739f665d) is listed/discoverable, opens anonymously, and has three actual public examples with computed structures/scoring/collection limits. Anonymous source/assets/fixture/license package bytes and non-HTML artifacts verify.28 frozen tests pass on macOS staging/isolated Linux; three managed13-row study arms pass, thresholds0.2→0.6 reduce6→3 hits; approved managed10000-row benchmark passes in4.835s with independently verified top100 ranking. This is software verification, not broad biological validation.

Dedicated [staging repo](https://github.com/Biosimulant/models-rdkit-similarity/tree/staging), source commitf0b2918fe9c300ba04595c45f0e2290ec6ff2a99. Core staging synchronized/preserved before work; no main commits, core source changes/deployments/provider switch. Private revision97f8a493-fd93-4507-ba30-2c136f31edd7; actual experimentf82e8c35-0803-41a7-a253-4541c25ba8ea; hosting identity none. Detailed exact references, Passports, costs, all gate links and rollback: [completion record](../../models/models-rdkit-similarity/reports/brief-completion-record.md), [acceptance matrix](../../models/models-rdkit-similarity/reports/acceptance.md).

Precise blockers: hosting preflight drops CSV upload, caps query/collection text at2000characters vs8192/2MiB and uses300s vs120s; not executed. Hub Experiments redirects to authenticated Studio instead of showing the actual retained study publicly. Generated HTML retrieves367bytes larger than advertised with a different hash; other retained artifacts pass. Hub Results shows visuals but dedicated artifact downloads use public Studio Files/API links. Cold/warm hosted inputs, cancellation/isolation/idle/resource metrics remain unverified. Correct platform staging support and concrete new production deployment/exact hosting approval are required before deployment. Production remains Modal.

Four-run provider preflight estimate$0.011064; beta user charge$0; actual provider invoice/managed peak memory unavailable. Isolated Linux10k peak188071936bytes under512MiB; benchmark repeats nine small structures, not all supported chemical graphs. Temporary harness resources cleaned; no hosting resources created. A1–A4/H1–H2 pass; A5/H3–H8 remain partial or blocked. **Not DONE.**

Evidence delivery commit **50a4cfb3a1feb291fba1132e1dc2aff9a5fd7bac**, pushed and verified equal to origin/staging; dedicated working tree clean. Full frozen Lab files remain unchanged. [Repository evidence](https://github.com/Biosimulant/models-rdkit-similarity/tree/50a4cfb3a1feb291fba1132e1dc2aff9a5fd7bac/reports).


## Subsequent staging progress — still BLOCKED

Updated 2026-10-04 08:12 UTC. Public release 0.1.0 is confirmed discoverable in
Hub search. Candidate 0.1.1 declares all five inputs, preserved CSV text,
2 MiB / 10,000-row bounds, numeric bounds and 120-second timeout; science and
component 0.1.0 are unchanged. Its exact private plan expired without a reply
or apply; public 0.1.0 remains intact. Refresh the plan before later approval.

Core source was synchronized from current main `4db9d8fccf853155dfa45f0cb08ee269901695b7`
while retaining staging history, and fixes were pushed to staging only:
`90b8df0080c6421e34dae4991268f22aa6192830` and
`3848b4ed603d56538f9410da24f08085d1378164`. CI passes; exact-commit staging
API and worker deployments succeeded and API health is healthy/connected/schema
compatible. Local backend 118 checks pass with one optional archive skip;
28 model checks, five composed cases and two real local RDKit child adapter
cases pass. Deployment/health and isolated adapter evidence are separate from
actual authenticated staging HTTP/worker and public hosted verification.
No production deployment/provider switch occurred. Incremental managed runs: 0.

The HTML mismatch is exactly an injected 367-byte Cloudflare beacon; removing
it reconstructs the advertised original hash. This is root-cause evidence,
not a passing original download. A tested no-transform header is deployed on
staging; live public bytes still need verification. Public actual study display,
hosting/admin approval, cold/warm inputs and isolation/cancellation/idle metrics
remain unresolved. Four-run provider estimate stays $0.011064, beta charge $0;
actual invoice and incremental build cost unavailable. No active hosting resources.

Candidate/evidence delivery commit `ae3328a03876b0564c55a77bad21bf6c96c3ab50` is pushed to dedicated staging;
[full evidence](../../models/models-rdkit-similarity/reports/hosting-progress-20261004.json)
and [acceptance matrix](../../models/models-rdkit-similarity/reports/acceptance.md)
retain every gate and remaining work. **Not DONE.**


Live revalidation: public pilot HTML still retrieves100630 bytes instead of100263
with the same mismatching hash; the deployed staging no-transform header does
not prove production transfer integrity. Production pilot is absent on staging
(404), so authenticated staging invocation remains unverified. MCP study readback
confirms all three completed11/6/3-hit arms, with no public-study access claim.
The unchanged candidate private proposal was refreshed after expiry; exact
approval is pending, and no apply/compute/publication/hosting has occurred.
Latest gate evidence commit `aaa520692c96a3ec32d8c5f2c5a6fb16ca9d0d0f` is pushed on dedicated staging.
Overall remains BLOCKED, not DONE; costs and Modal production unchanged.

## Latest verified progress — 2026-10-04 09:01 UTC, still BLOCKED

Approved private revision67a97dfc-4e38-4510-a85e-da3dc8039e50 completed a new managed Modal pilot in1.910s: seven typed outputs, four visuals and independently verified complete ranking/all seven original artifact hashes. Approved public release [demi/rdkit-molecular-similarity-search@0.1.1](https://hub.biosimulant.com/labs/f0291213-a063-4aeb-8981-8e0e739f665d) is listed and opens publicly; its1,164,660-byte immutable package hash and30 source/asset/fixture/license documents match. All21 artifacts of the three public examples now independently match original sizes/hashes, including HTML after the production no-transform fix. H3 now passes; historical mismatch is resolved.

Required query smoke draft and redundant drawing-path fixes were tested on staging, CI37190330685 passed, and staging API/worker deployed742fd3f. After the user's new explicit approval, these two commits only were promoted via [PR32](https://github.com/Pledre/biosimulant-backend/pull/32): production API/worker deployedb2a47638606b320f3abc756ea3febc7e6ac3405a successfully; health is healthy/connected/schema compatible. Staging histories and concurrent work preserved. Production stays Modal. Rollback API/worker toae81e6af273ba10c7212e272dcf7a224a27c5266; no migration. This is local/isolated/CI/deployment evidence; authenticated staging end-to-end invocation is still unverified.

The public hosting plan now correctly exposes query, pasted CSV, uploaded CSV, top_k and threshold;2MiB/10000 rows/120s,Modal0.5CPU512MiB,max1,minwarm0,idle300s,networkblocked. Its exact digest approval and existing administrator review are pending; no hosting identity or cold/warm result yet. Actual public study display, hosted invocation/download/input bounds/cancellation/isolation/idle telemetry remain. Five-run provider estimate$0.013830,beta charge$0; actual invoice/managed peak and hosting cost unavailable. [Latest full record](../../models/models-rdkit-similarity/reports/hosting-progress-v011-20261004.json), [acceptance matrix](../../models/models-rdkit-similarity/reports/acceptance.md). **Not DONE.**

Exact0.1.1 original-fixture managed run8ca33c3a-0755-470e-b782-288da6c3a175 was deliberately made public and all seven of its artifacts pass anonymous original-byte checks. Four public examples now have28 verified artifact transfers; source/internal fixture only, no private user molecules. [Exact public example](../../models/models-rdkit-similarity/reports/candidate-v011-public-example-verification.json), [visible results](../../models/models-rdkit-similarity/reports/public-v011-exact-run.png), [Files controls](../../models/models-rdkit-similarity/reports/public-v011-exact-run-files.png). Hosting approval remains pending.
