# Acceptance evidence — RDKit Molecular Similarity Search

Status: BLOCKED — public immutable release, Hub listing, actual example results and anonymous downloads verified; active hosting and public Experiments remain blocked. No requirement is waived. Updated 2026-10-04.

| Gate | State | Linked evidence and precise limits |
| --- | --- | --- |
| A1 | PASS | [28 frozen tests](frozen-tests.txt), [Linux tests](linux-tests.txt), [independent legacy RDKit tests](../labs/molecular-similarity/tests/test_acceptance.py): identity1, all scores[0,1], complete small-fixture ranking and every score within1e-12. [Managed payload parity](managed-verification.json) confirms all three fixture runs. |
| A2 | PASS | Same tests cover inclusive threshold before top_k, Unicode ID/row ties, no matches, repeated/equivalent molecules, invalid rows. [Five actual text/file CLI cases](local-runtime-verification.json), [isolated Linux cases](linux-runtime-verification.json). Managed thresholds yield11/6/3 hits. Hosted file input remains H5 blocked. |
| A3 | PASS | Frozen alanine chiral pair separates fingerprints with includeChirality=True; independent disabled-chirality control scores1. Declared fixed release setting. |
| A4 | PASS | Exact CSV raw bytes including BOM/newlines, query checksum, valid/searched/invalid counts, original IDs and row indices verified locally and in [managed receipts](managed-verification.json); [10k payload](managed-benchmark-verification.json) matches its255570-byte checksum. |
| A5 | PARTIAL/BLOCKED | [Actual completed study](study-final.json) retains thresholds0.2/0.6 and explains6→3 on same13-row original collection (11 valid/2 invalid). Both arms deliberately public. [Hub results](public-hub-results.png) expose collection/scoring/limits; [public description](public-description.json) explains comparison. Actual study is visible in authenticated [Studio](https://studio.biosimulant.com/experiments/f82e8c35-0803-41a7-a253-4541c25ba8ea), but Hub Experiments only redirects to authenticated Studio; no public study control exists. |
| H1 | PASS | [Freeze](freeze-manifest.json), [NOTICE](../labs/molecular-similarity/NOTICE.md), full pinned distribution/native/font licenses and original BSD fixture. [Anonymous release byte/member verification](public-release-verification.json) proves exact code/assets/fixtures/notices. Native owner-bound re-download succeeds with ordinary User-Agent: [verified bytes](native-runtime.zip.verification.json). No commercial database/weights/online search. |
| H2 | PASS | Every gate is mapped here; MRS/MTS validators0errors/0warnings, exact release/scoring/tolerances retained. Demonstrations and small-fixture parity are software verification, not broad chemistry/biological validation. Failed gates remain failed. |
| H3 | PASS | [Exact 0.1.1 completed run](candidate-v011-run-final.json), [all seven original direct artifacts and independent parity](candidate-v011-managed/acceptance-verification.json), [matching REVIEW Passport](candidate-v011-run-passport.json). All21 original public fixture artifacts now verify, including HTML: [anonymous verification](public-all-artifact-verification.json). Historical issue: [Pilot completed](managed-pilot-status.json), seven typed outputs/four computed visuals, [matching REVIEW Passport](pilot-passport.json); six non-HTML artifacts independently verify, including CSV/JSON/receipt/PNG/results. [HTML verification](managed-pilot/report.html.verification.json) fails: advertised100263 bytes vs downloaded100630; SHA differs. Platform-added HTML bytes prevent the all-artifact gate from passing. |
| H4 | PARTIAL | [Public0.1.1 publication](candidate-v011-publication.json), [anonymous exact package](candidate-v011-public-verification.json), [listed metadata](candidate-v011-public-description.json), [public page/results](public-v011-results.png). Reading examples/downloads needs no owner key or install. Normal Studio authentication/managed approval applies; active hosted invocation access/payment unverified until H5. Registry runtime_valid=false/domain_validated=false; REVIEW Passport and software parity are not broad validation. |
| H5 | PARTIAL | Exact0.1.1 is administrator-approved and ready on Modal. Actual pasted/uploaded fixture returns6/3hits, seven outputs/four visuals; all12 artifact hashes pass. [Pasted](hosted-v011-paste/acceptance-verification.json), [uploaded](hosted-v011-upload/acceptance-verification.json). Confirmed cold-container invocation remains unverified. |
| H6 | PARTIAL/BLOCKED | Three deliberate original-fixture public runs appear in Hub Results after refresh, with image/text/bar/table. [22 anonymous access/artifact checks](public-examples-verification.json) pass all non-HTML bytes for all arms; public Studio run pages expose seven Files download controls; anonymous API transfers verify. Hub Results does not offer a dedicated artifact-download panel; use the public run Files or API links. [Actual retained study](study-final.json) exists, but [public Experiments limitation](public-experiments-blocker.png) remains. |
| H7 | PARTIAL | Hosted execution1.076/0.9587s, wall3.688286/4.155509s; bounds/cancelled terminal status pass. [Operations](hosted-v011-operations.json). Declared120s/max1/minwarm0/idle300s. Cold/warm container classification, enforced timeout, cross-account/idle telemetry, provider peak/invoice and hosted charges unavailable. Managed estimate$0.013830/beta$0. |
| H8 | PARTIAL / overall incomplete | [Current record](hosting-progress-v011-20261004.json) records public0.1.1, exact hosting identity/revision3, all provenance, runs, costs, blockers and pause/rollback. Brief/index remain BLOCKED, not DONE. |

## Staging and operational boundary

Dedicated repo https://github.com/Biosimulant/models-rdkit-similarity/tree/staging, source f0b2918fe9c300ba04595c45f0e2290ec6ff2a99; prepared-evidence commits77eaf510c70d361e4c44517283e6395a95fb8767 andc06e9dda552b52dba2a2d407075d8704f80861b0. New repo has no main baseline. Core clean staging checkouts synchronized before work: biosim baseline95071d18412aa9c3a174a38a066fd85e39428cc6; backend maincd1b8312b2db5c29ec494d3f063bd8ac2ebfbcc2 ancestor of staging4b1dfd3529920db7bc3eafb52c9d78c3c9de40da. Existing staging-only/other-worktree work preserved. No core modification/deployment/provider switch. Linux tests are isolated staging runtime checks; managed runs execute on Modal; neither is a core end-to-end staging deployment or hosted check. Unique harness image/containers removed, base cache/venv retained.

Next: platform staging must support generic CSV upload, preserved multiline text with declared bounds and120s timeout; public retained experiment display and matching generated-HTML metadata need repair. Then obtain fresh concrete production-deployment approval under AGENTS.md and a valid exact hosting plan approval; enable exact release on Modal and verify cold/warm upload/paste inference, downloads, bounds/cancellation/isolation/idle/resource metrics. Existing unrelated platform worktrees remain untouched.

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


Live continuation readback, 2026-10-04: [production HTML recheck](live-html-recheck-20261004.json)
still fails exact bytes/hash, with no no-transform header on the production
response. The same original public fixture run is absent (404) on staging,
so the successful staging deployment/health cannot establish actual invocation
or live artifact-transfer acceptance. [Study readback](study-readback-20261004.json)
confirms three completed arms and 11/6/3 hits; this is owned access only. Local
Hub staging source `11347bdca65627d63ffc84c1afb15982b49b6ae7` explicitly renders
an authenticated Studio Experiments handoff, matching the retained public UI
blocker. No broader public study capability is inferred. New private plan is
[retained](candidate-v011-private-plan-refreshed.json) awaiting exact approval;
previous expired proposal remains retained separately. No new compute.

## Latest 0.1.1 publication and hosting progress — 2026-10-04

The private revision and public exact0.1.1 release are approved and executed. [Publication](candidate-v011-publication.json), [anonymous exact package](candidate-v011-public-verification.json), [release Passport](candidate-v011-release-passport.json), [current full operational record](hosting-progress-v011-20261004.json). H3 now passes; the earlier HTML byte mismatch is resolved in production and all21 public artifact hashes pass. Public listing remains verified. All five hosting inputs and 2MiB/10k/120s are admitted by the valid exact plan. H5 remains BLOCKED until its approval/admin activation and real hosted invocations. H4 remains partial until public invocation access is verified. A5/H6 remain partial because public actual study UI is unsupported. H7/H8 remain partial until final hosted operational evidence. Five managed runs have provider estimate$0.013830 and beta charge$0. Actual invoice/peak and hosting costs unavailable.

Core staging CI and API/worker rollout passed for742fd3f. Under the user's new explicit approval, only the RDKit smoke-draft and inline-drawing fixes were promoted through PR32 and production API/worker deployedb2a4763; health is healthy/connected/compatible. Compute stays Modal. Existing staging/concurrent work was preserved and production merged back to staging. Rollback API/worker toae81e6a; no migration. These local/isolated/CI/deployment checks do not establish authenticated staging end-to-end or hosted invocation readiness. No active hosting resources yet. **Not DONE.**

The exact0.1.1 managed fixture run is also deliberately public. [Anonymous original transfer verification](candidate-v011-public-example-verification.json) passes all seven artifacts, [public results](public-v011-exact-run.png) and [seven Files download controls](public-v011-exact-run-files.png) are visible. Four public examples now have28 exact artifact checks. Actual public study UI and hosting checks still block completion.

The exact0.1.1 managed example now appears in Hub Results with all four computed visuals: [public Hub screenshot](public-v011-hub-exact-run.png). One transient browser fetch failed before an HTTP response; a reload recovered. This is recorded separately from consistently passing anonymous artifact byte checks. Evidence/source delivery96a3b8a is pushed to dedicated staging.

## Hosting request executed — administrator sign-in required

On2026-10-04 the user explicitly instructed approval through admin. The exact prepared public0.1.1 hosting plan was executed before expiry. Hosting identitya363d62f-278a-48e6-96d3-088fa31f9a15, revision1, spec2ec49c32-a01f-4f85-b18f-8365aaee4c6c, digest9940744e190ff8c004f5345b4c4c2a9408975c93277cc586b029176cef54fdb5. Status is awaiting_approval; no checks yet. The configured production administrator console redirects to sign-in and no authenticated admin session is available. User sign-in is requested; approval is authorized but not performed. No authentication/role/approval bypass or new compute started. Exact request and current state are retained in reports/candidate-v011-hosting-requested.json and reports/hosting-progress-v011-20261004.json. H5 remains blocked; hosting is not active.

## Administrator approval and active hosting — 2026-10-04

The previous administrator-login blocker is resolved. After the user signed in and explicitly instructed approval, the exact public0.1.1 request was approved in the administrator console. Hosted identitya363d62f-278a-48e6-96d3-088fa31f9a15 is ready at revision3; archive/image/cache/smoke pass, smoke1.598s. Compute remains Modal0.5CPU/512MiB/max1/minwarm0/120s/idle300s/networkblocked. No new core deployment/provider/auth change occurred during this verification. [Hosting record](hosting-progress-v011-20261004.json).

Actual pasted13-row fixture invocation8c7b1978-8c74-46cf-817a-3df0f7ba21fc returns6hits at0.2: execution1.076s, accepted-to-completed3.688286s. Real browser-uploaded identical245-byte/checksummed fixture invocation9f24cf70-26e6-431c-b927-f3b2d70735ff returns3hits at0.6: execution0.9587s, wall4.155509s. Each full retained result contains seven outputs/four visuals; all twelve original artifact byte sizes/hashes independently verified. Compact status values are empty by design; full results contain hit_count/report and file ports. [Pasted evidence](hosted-v011-paste/acceptance-verification.json), [uploaded evidence](hosted-v011-upload/acceptance-verification.json), [visible hosted structures/results](hosted-v011-result-visible.png). Normal Studio sign-in protects uploads/results; no owner API key or local install is needed. Separate non-owner hosted execution/payment account remains unverified.

Top_k101, threshold1.01 and10001rows reject before compute. A2MiB+1 request rejects at gatewayHTTP413; this does not prove exact2MiB pasted-envelope admission. Both collection sources reject during model execution with generic lab_execution_failed; corrected upload-only input succeeds. Cancellation of bounded10000-row invocation9c007018-593e-4888-98c2-58e591b852de gives retained cancelled status and no result; lease revocation succeeds, provider stop telemetry unavailable. [Operations](hosted-v011-operations.json). A browser CSV download event timed out; five controls are visible and all owned artifact bytes retrieve correctly through MCP, but browser-save completion is not claimed.

H5 is now PARTIAL: exact hosting and real pasted/uploaded inputs/outputs pass; cold-container evidence remains. H4/H7/H8 remain partial, A5/H6 remain blocked on public actual study UI. No confirmed cold/warm classification, provider peak/invoice, cross-account isolation, enforced-timeout or idle-container telemetry. Five managed-run estimate remains$0.013830, beta managed charge$0. Four hosted invocation requests (two completed, one dual-source failure, one cancelled) plus one smoke; hosted plans expose no cost estimate, actual hosting/build spend and hosted charge unavailable. Disable this hosting via owner hosting_update pause at currentrevision3 or admin Pause; withdraw to remove routing. Core rollback staysae81e6a; production stays Modal. **BLOCKED, not DONE.**
