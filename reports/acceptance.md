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
| H5 | BLOCKED | [Exact public0.1.1 hosting plan](candidate-v011-hosting-ready-plan.json) now admits all five inputs,2MiB/10000 rows/120s/Modal0.5CPU512MiB/max1/minwarm0. Exact plan approval/admin activation and real cold/subsequent pasted/uploaded invocations remain. [Staging/production rollout and rollback](hosting-progress-v011-20261004.json). No hosted identity yet. |
| H6 | PARTIAL/BLOCKED | Three deliberate original-fixture public runs appear in Hub Results after refresh, with image/text/bar/table. [22 anonymous access/artifact checks](public-examples-verification.json) pass all non-HTML bytes for all arms; public Studio run pages expose seven Files download controls; anonymous API transfers verify. Hub Results does not offer a dedicated artifact-download panel; use the public run Files or API links. [Actual retained study](study-final.json) exists, but [public Experiments limitation](public-experiments-blocker.png) remains. |
| H7 | PARTIAL | [Resources/cost](resource-cost.json): managed pilot1.943s,10k4.835s, Modal0.5CPU/512MiB,0GPU, declared120s/profile metadata300s. Isolated Linux10k peak188071936 bytes under512MiB. Five-run provider estimate$0.013830; beta user charge$0; actual invoice/managed peak absent. Hosted cold/warm, cancellation, cross-account input isolation/idle behavior not run. Local unique mode700/600 invocation directories pass isolation. Exact hosting plan max1/minwarm0/idle300s/120s/networkblocked; not activated. No private molecule data or signed URLs are in deliberate public examples. |
| H8 | PARTIAL delivery record / overall incomplete | [Completion record](brief-completion-record.md) records exact source commit, immutable release, public URL, workspace/revision, runs/study/Passports, costs/blockers/rollback. Hosting identity is explicitly none. Brief/index remain BLOCKED, not DONE. |

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
