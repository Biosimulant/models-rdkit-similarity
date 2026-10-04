# Item 02 completion record — BLOCKED, not DONE

Updated 2026-10-04. Implemented, verified and publicly released the frozen structural-search Lab. Active hosting fails the exact input/timeout contract; no production deployment/provider change was made. All gate evidence is in [acceptance.md](acceptance.md).

Public Lab: https://hub.biosimulant.com/labs/f0291213-a063-4aeb-8981-8e0e739f665d . Exact release **demi/rdkit-molecular-similarity-search@0.1.0**, package51644052-5c60-4208-9f86-7a93cdf7d51b, version9b797fb4-462c-489a-a9fb-0795c037a4ad, SHA2569de060e143a8b844e614855d6a44ea9d6d3303520897c4db8d1e0f0afd193600,1162009bytes. Public listing/discovery and anonymous package bytes verified; all shipped code/assets/fixtures/notices match frozen local files (Lab manifest normalized by platform). Original sample is BSD-3-Clause. No unresolved shipped-asset rights or external molecule search service.

Dedicated repo https://github.com/Biosimulant/models-rdkit-similarity/tree/staging. Frozen implementation commitf0b2918fe9c300ba04595c45f0e2290ec6ff2a99; earlier evidence77eaf510c70d361e4c44517283e6395a95fb8767,c06e9dda552b52dba2a2d407075d8704f80861b0. Evidence delivery commit is recorded in the external brief/index after push. New repo has no main branch baseline. Clean core staging synchronized before work: biosim main/staging95071d18412aa9c3a174a38a066fd85e39428cc6; backend maincd1b8312b2db5c29ec494d3f063bd8ac2ebfbcc2 ancestor of inspected staging4b1dfd3529920db7bc3eafb52c9d78c3c9de40da. Staging-only and other active-worktree work preserved. No core edits/deployments/provider switches. Local/isolated checks, managed Modal execution, public access and hosted checks are distinct; core end-to-end staging deployment and hosted checks were not performed.

MRS1.0.0/MTS1.0.0, exact tolerances and fixtures frozen.28 tests pass on macOS staging and isolated Linux; five composed CLI cases per environment accept actual pasted/uploaded inputs, thresholds/no hits/chiral pair and verify seven typed outputs/downloads/visuals. Morgan radius2,2048bits,chiralityTrue,Tanimoto on-bit intersection/union; inclusive threshold then top_k; descending scores/exact Unicode ID/row index; canonical isomeric exact_match, preserve all duplicates/fragments/isotopes/stereo. Limits10000rows/2MiB, top_k1..100,8192SMILES characters,256atoms/512bonds,120s. Small-fixture parity is software verification, not broad biological validity.

Private workspace6d098ff1-41e3-47c8-84f8-29bdbd46f091; exact approved revision97f8a493-fd93-4507-ba30-2c136f31edd7, SHA0343eeaae0e6255ee6f116244b2955b03290545e4f973412d9abcddc1c9cb1a3; applied approved35-operation plan3c30e3ed-a410-4533-b40c-c93dffe65bcf. User separately approved bounded three-arm study and public publication/benchmark exact plans; no approvals transferred from other items.

Actual completed studyf82e8c35-0803-41a7-a253-4541c25ba8ea: https://studio.biosimulant.com/experiments/f82e8c35-0803-41a7-a253-4541c25ba8ea . Approved plan5ad01f1d-737d-4346-83d0-afba4fb47c16. Three13-row original-fixture runs,11valid/2invalid, same collectionSHA82d2966a523a3e35e31926135be0238c91abea8e7513b4351ab29834989002fb:

| Arm | Run / public example | Execution seconds | Hit count | Passport |
| --- | --- | --- | --- | --- |
| threshold0 pilot | [0850f12f-e803-4876-8f98-1df512b2e7fd](https://studio.biosimulant.com/runs/0850f12f-e803-4876-8f98-1df512b2e7fd) |1.9433969070669264|11|ececeebe-8753-4424-9d3a-5346435a9142|
| threshold0.2 | [1169e304-181a-44ad-b089-8d252145cd41](https://studio.biosimulant.com/runs/1169e304-181a-44ad-b089-8d252145cd41) |2.1706244399538264|6|7e3cf7d5-bf2c-4894-9cc1-18aaaacbf7aa|
| threshold0.6 | [e4b31111-37b1-4faa-aead-323bcd0b54a5](https://studio.biosimulant.com/runs/e4b31111-37b1-4faa-aead-323bcd0b54a5) |1.874264616984874|3|d00956ad-7179-4c77-9e59-010322462e0f|

All deliberately public, visible in refreshed Hub Results with computed structures/text/bars/table.22 anonymous run/list/artifact access checks verify non-HTML byte sizes/hashes. Public run Files provides downloadable originals; Hub itself lacks a dedicated artifact panel. Raising threshold0.2→0.6 removes weaker fingerprint overlaps (6→3), without potency/activity/toxicity/patent claims. Actual study comparison is retained in authenticated Studio, but Hub Experiments only directs to an authenticated workspace; public study-display gate remains incomplete.

10k approved managed benchmark plan d71ad832-9920-439a-aa8f-78e77de40d54, run05685e99-9f1a-4c16-b172-1bdfabe34461:4.8350782910129055seconds,10000valid/0invalid,100returned,7typed outputs/4visuals. Verified results398169bytes/SHA9c6dccb3c6f238da15aa8b4d5be0833a058f625328337dcccf5646b0a2953f34; every score/complete top100 ranking matches independent pinned RDKit calls. Synthetic9-structure repetition benchmark does not cover all maximum-size chemical graphs.

Passports: revision38061cde-eeec-4ed3-86f4-4303c27a8e6e; release193032e6-d8b2-4452-9db1-e49a37d21826; benchmark7dbfed68-2893-4858-af36-376d6a6b06be. All REVIEW, not universal scientific validity. Pilot artifact/visual checksPASS; curated source-evidence resource not pinned (source files/license hashes retained), compatibilityN/A with0wires. Registry qualification schema_valid=true,runtime_valid=false,domain_validated=false. Actual managed run success does not substitute for registry or domain qualification.

Costs/resources: four approved Modal0.5CPU/512MiB CPU runs, noGPU/training. Combined provider preflight estimate **$0.011064**, free-beta user charge **$0**, actual provider invoice unavailable. Requested timeout120s each; allocation metadata300s. Managed peakRSS unavailable. Isolated Linux100row pilot2.095s/180719616-bytepeak;10k4.183s/188071936-bytepeak under512MiB/networknone. Pilot/benchmark queue-to-completion roughly24/25s includes infrastructure; none are hosted cold/warm metrics. Local directories isolate invocations; hosted cross-user isolation/cancellation/idle behavior unverified. Unique harness image/containers removed, caches/venv retained. No hosted resource was started.

Precise blockers:

1. Hosting planc4851a3e-cf3d-435c-8326-44f92cd07e38 for exact release omits collection_file, resolves collection_csv/query to2000chars (declared2MiB/8192chars), timeout300s (declared120s). Administrator approval also required. No correct-contract plan approved/executed; hosting_get reports hosted:null, identity **none**. Proposed Modal max1/minwarm0/idle300s/networkblocked is preflight only.
2. Public actual experiment display is unsupported by current Hub Experiments UI. Do not call the redirect a visible public study.
3. Generated pilot HTML advertises100263bytes/SHA2b94ce52c5c567ac682742de21b1466933b953eabdc54ea0daae823c4c2f1b03 but retrieves100630bytes/SHA13682ac94f4922d5886f0b7b982761a6d951279f09e8b2efafc0b11a7fd7d802. All non-HTML artifacts pass. Full H3 remains incomplete.

Remaining work: repair/verify generic CSV upload, preserved multiline collection input/bounds and120s timeout in platform staging; repair HTML checksum metadata and public retained-study display. Obtain new concrete production deployment approval only after staging evidence, plus valid exact hosting approval. Keep Modal; invoke cold then subsequent pasted/uploaded example, verify outputs/limits/cancellation/isolation/idle/resources/actual cost and downloads as non-owner. Re-evaluate every partial gate; mark DONE only when all pass.

Rollback: no deployment to roll back and no hosting to pause. To withdraw listing, use Lab metadata hub_listed=false; public example sharing can be switched back to private in Studio. Immutable release/evidence remain retained. If hosting is later created, read its current identity/revision and use approved pause/withdraw before changing deployment; retain all run artifacts. Never switch production providers for this item.

Public UI download observation: rankings.csv control is present and was clicked; CUA download-event capture timed out without UI/console error. This event capture is inconclusive; direct anonymous CSV transfer is independently verified. See [public UI record](public-ui-verification.json).

## Subsequent staging progress — 2026-10-04

The live preflight now rejects collection_csv length rather than silently truncating it: [current response](hosting-current-preflight.json). Platform source now supports the declared2MiB/10000-row envelope with legacy128KiB/100 defaults preserved and honors declared120s timeout. Backend staging implementation90b8df0080c6421e34dae4991268f22aa6192830 and CI commit3848b4ed603d56538f9410da24f08085d1378164 are pushed; primary checkouts preserved, main baseline4db9d8fccf853155dfa45f0cb08ee269901695b7 synchronized into isolated staging worktree.118 tests pass,1 skipped;13 new cases pass after formatting.

The367-byte HTML difference is exactly a Cloudflare Web Analytics script: [forensic hash proof](html-transformation-root-cause.json). Staging artifact responses now declare private/no-store/no-transform; this is still not verified public transfer. Cloudflare's [official documentation](https://developers.cloudflare.com/web-analytics/faq/) explains that no-transform prevents automatic injection.

Candidate Lab0.1.1 adds explicit CSV format/upload/multiline preservation/byte and row/numeric/timeout metadata while leaving model0.1.0, algorithm, fixtures and all scientific requirements unchanged.28 tests,5 composed CLI cases and [two actual RDKit child adapter cases](hosting-staging-adapter-verification.json) pass; all five downloads and original BOM/CRLF checksums verify. [Freeze](freeze-candidate-v011.json), [spec](hosting-staging-candidate-spec.json), [private plan](candidate-v011-private-plan.json), [progress/commits](hosting-progress-20261004.json). Exact private revision approval requested; not applied. No additional managed run/provider spend, public release or hosting; no production deploy. Public study display and all live hosting gates remain incomplete.


### Verified staging rollout — 2026-10-04 08:09 UTC

Backend implementation `90b8df0080c6421e34dae4991268f22aa6192830` and CI gate
`3848b4ed603d56538f9410da24f08085d1378164` were pushed to staging only.
[CI](https://github.com/Pledre/biosimulant-backend/actions/runs/37187418150)
passed on Python 3.12 for the contract and Python 3.11 for the routing gate.
Coolify staging API and worker webhook deployments succeeded at that exact
commit; a manual API redeploy also succeeded in 12 seconds, using the existing
image. Worker deployment took 67 seconds. Staging API `/health` returned HTTP
200, healthy, database connected and schema compatible. Screenshots, worker
logs, health response and CI metadata are retained in this reports directory.
This proves source rollout and health, not actual authenticated HTTP/worker
invocation or public hosted readiness. No production deployment occurred.

The candidate private change plan expired at 08:08:13 UTC without a user
reply or apply. Candidate 0.1.1 is retained locally on staging; the public
0.1.0 and approved immutable private revision remain intact. Refresh its exact
plan before later approval/apply. No new managed run, publication or hosting
was executed. All prior checklist statuses remain partial/BLOCKED.

New local checks: 118 backend checks pass, one optional pinned Lotka archive
check skips because CURATED_LOTKA_ARCHIVE is absent; 28 similarity checks,
five composed cases and two actual local Python 3.12 adapter child executions
pass. The adapter verifies raw pasted/uploaded identity, seven outputs, four
visuals, five byte/hash-pinned downloads and scratch cleanup. The HTML
367-byte mismatch is traced to a Cloudflare beacon injection; removal
reconstructs the advertised original hash exactly, but does not count as an
unmodified download. The tested `no-transform` header is deployed on staging
only and still requires live transfer verification.

Hub search at 08:09 UTC returned the exact public similarity 0.1.0 release.
Existing four-run provider estimate remains $0.011064 and beta user charge
$0; actual invoice and incremental build/deployment cost are unavailable.
No additional managed/Modal computation or hosting resources were created.
Production stays on Modal. Remaining gates: authenticated staging integration,
fresh private/public exact plans, separately approved production rollout,
correct-contract public hosting/admin approval, cold/warm invocations and
limits/cancellation/isolation/idle metrics, public actual study display, and
unmodified public HTML bytes. **Not DONE.**

## 0.1.1 verified publication and production support, still BLOCKED

Latest exact refs, all gates, costs and rollback are in [current operational record](hosting-progress-v011-20261004.json). Public exact0.1.1 release and its own original-fixture managed run8ca33c3a are readable without owner credentials. All28 original artifacts across four public examples verify; H3 passes. Core staging smoke draft and drawing fixes were promoted under fresh explicit user approval via PR32; production API/worker b2a4763 pass deployment/health with Modal unchanged. The correct five-input hosting plan is prepared but unexecuted pending exact digest and administrator approval. A5/public actual study UI and H5 hosted operations still block DONE. Five managed runs estimate$0.013830, beta charge$0; actual invoice/host spend/managed peak unknown. Rollback core API/worker toae81e6a. Hosted pause/withdraw instructions apply only after an actual hosting identity exists.

## Hosting request executed — administrator sign-in required

On2026-10-04 the user explicitly instructed approval through admin. The exact prepared public0.1.1 hosting plan was executed before expiry. Hosting identitya363d62f-278a-48e6-96d3-088fa31f9a15, revision1, spec2ec49c32-a01f-4f85-b18f-8365aaee4c6c, digest9940744e190ff8c004f5345b4c4c2a9408975c93277cc586b029176cef54fdb5. Status is awaiting_approval; no checks yet. The configured production administrator console redirects to sign-in and no authenticated admin session is available. User sign-in is requested; approval is authorized but not performed. No authentication/role/approval bypass or new compute started. Exact request and current state are retained in reports/candidate-v011-hosting-requested.json and reports/hosting-progress-v011-20261004.json. H5 remains blocked; hosting is not active.

## Administrator approval and active hosting — 2026-10-04

The previous administrator-login blocker is resolved. After the user signed in and explicitly instructed approval, the exact public0.1.1 request was approved in the administrator console. Hosted identitya363d62f-278a-48e6-96d3-088fa31f9a15 is ready at revision3; archive/image/cache/smoke pass, smoke1.598s. Compute remains Modal0.5CPU/512MiB/max1/minwarm0/120s/idle300s/networkblocked. No new core deployment/provider/auth change occurred during this verification. [Hosting record](hosting-progress-v011-20261004.json).

Actual pasted13-row fixture invocation8c7b1978-8c74-46cf-817a-3df0f7ba21fc returns6hits at0.2: execution1.076s, accepted-to-completed3.688286s. Real browser-uploaded identical245-byte/checksummed fixture invocation9f24cf70-26e6-431c-b927-f3b2d70735ff returns3hits at0.6: execution0.9587s, wall4.155509s. Each full retained result contains seven outputs/four visuals; all twelve original artifact byte sizes/hashes independently verified. Compact status values are empty by design; full results contain hit_count/report and file ports. [Pasted evidence](hosted-v011-paste/acceptance-verification.json), [uploaded evidence](hosted-v011-upload/acceptance-verification.json), [visible hosted structures/results](hosted-v011-result-visible.png). Normal Studio sign-in protects uploads/results; no owner API key or local install is needed. Separate non-owner hosted execution/payment account remains unverified.

Top_k101, threshold1.01 and10001rows reject before compute. A2MiB+1 request rejects at gatewayHTTP413; this does not prove exact2MiB pasted-envelope admission. Both collection sources reject during model execution with generic lab_execution_failed; corrected upload-only input succeeds. Cancellation of bounded10000-row invocation9c007018-593e-4888-98c2-58e591b852de gives retained cancelled status and no result; lease revocation succeeds, provider stop telemetry unavailable. [Operations](hosted-v011-operations.json). A browser CSV download event timed out; five controls are visible and all owned artifact bytes retrieve correctly through MCP, but browser-save completion is not claimed.

H5 is now PARTIAL: exact hosting and real pasted/uploaded inputs/outputs pass; cold-container evidence remains. H4/H7/H8 remain partial, A5/H6 remain blocked on public actual study UI. No confirmed cold/warm classification, provider peak/invoice, cross-account isolation, enforced-timeout or idle-container telemetry. Five managed-run estimate remains$0.013830, beta managed charge$0. Four hosted invocation requests (two completed, one dual-source failure, one cancelled) plus one smoke; hosted plans expose no cost estimate, actual hosting/build spend and hosted charge unavailable. Disable this hosting via owner hosting_update pause at currentrevision3 or admin Pause; withdraw to remove routing. Core rollback staysae81e6a; production stays Modal. **BLOCKED, not DONE.**
