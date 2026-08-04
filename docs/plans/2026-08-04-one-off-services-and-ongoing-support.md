# One-off Services and Ongoing Support Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Make fixed-scope, one-off projects the primary AI Services offer, with optional ongoing support clearly presented after a successful first project.

**Architecture:** Keep this as a single-page static-site change. Extend the existing cream/copper `index.html` design system with responsive one-off-service and support-plan card grids, then validate the source and rendered page with an ad-hoc local verifier plus real-browser desktop/mobile checks. Publish through the repository’s existing GitHub Pages source: `main` at `/`.

**Tech Stack:** Semantic HTML5, embedded CSS, Python standard-library verification, local static HTTP server, Git/GitHub Pages.

---

### Task 1: Record the release baseline and Pages source

**Objective:** Confirm the exact source branch and explain the repository/live mismatch before touching public content.

**Files:**
- Inspect: `index.html`
- Inspect: `docs/superpowers/specs/2026-08-04-one-off-services-and-ongoing-support-design.md`
- Inspect: GitHub Pages configuration for `492kw/ai-services`

**Step 1: Inspect local and remote Git state**

Run:
```bash
git status --short --branch
git remote -v
git log --oneline --decorate -12
git ls-remote --heads origin
```

Expected: local `main` contains the approved specification commit while remote `main` is still at the prior site commit.

**Step 2: Inspect Pages API configuration and build record**

Run a token-authenticated GitHub API query for `/repos/492kw/ai-services/pages` and `/pages/builds`.

Expected: Pages uses `main` with path `/`, and the latest build commit identifies the deployed revision.

**Step 3: Fetch the cache-busted live page and compare content markers**

Run:
```bash
curl -sSL -H 'Cache-Control: no-cache' 'https://492kw.github.io/ai-services/?v=preflight' -o /tmp/ai-services-live-preflight.html
```

Expected: live markers match the latest deployed commit, while the approved one-off content is absent until implementation is pushed.

**Step 4: Record conclusion for release**

The expected cause is not an incorrect Pages setting: Pages is correctly configured to deploy remote `main`; the approved local commit was ahead of remote and therefore had never triggered a deployment. Do not alter Pages configuration unless this evidence changes.

### Task 2: Add the implementation plan to version control

**Objective:** Preserve the approved execution path before changing the site.

**Files:**
- Create: `docs/plans/2026-08-04-one-off-services-and-ongoing-support.md`

**Step 1: Self-review the plan**

Check that the plan has exact paths, sequenced 2–5 minute steps, commands, verification, the Pages diagnosis, no invented deliverables, and no requirement to modify unrelated assets/configuration.

**Step 2: Commit the plan**

Run:
```bash
git add docs/plans/2026-08-04-one-off-services-and-ongoing-support.md
git commit --author='Simon Fung <simonfungwork@gmail.com>' -m 'docs: add one-off services implementation plan'
```

Expected: one documentation commit containing only the plan.

### Task 3: Route visitors to the smallest useful first project

**Objective:** Change hero/navigation calls to action so the first commercial action is the one-off offer.

**Files:**
- Modify: `index.html` (header navigation and hero section)
- Test: `/tmp/verify-ai-services-one-off.py`

**Step 1: Write the failing content/link checks**

Create an ad-hoc Python verifier that parses `index.html`, requires the approved hero entry copy verbatim, and requires the primary hero and navigation route to target `#one-off-projects`.

**Step 2: Run the verifier to demonstrate the current page fails**

Run:
```bash
python3 /tmp/verify-ai-services-one-off.py /home/simon/ai-services/index.html
```

Expected: FAIL because the one-off section, exact entry copy and target anchor do not yet exist.

**Step 3: Make the minimal hero/navigation edit**

Add the exact required entry heading and paragraph adjacent to the primary project CTA. Change that CTA to `href="#one-off-projects"`; retain the work-example CTA. Add a concise navigation route to `#one-off-projects` without removing accessibility or existing work/contact routes.

**Step 4: Re-run the relevant verifier checks**

Run the verifier and expect hero text and primary route checks to pass, with expected later-section checks still failing until the next tasks are complete.

### Task 4: Add the primary fixed-scope project section and process

**Objective:** Put the exact seven one-off services, qualification and fixed-scope process before the existing examples.

**Files:**
- Modify: `index.html` (embedded CSS and new content between `#services` and `#work`)
- Test: `/tmp/verify-ai-services-one-off.py`

**Step 1: Extend only the existing design system**

Add CSS for a responsive seven-card one-off grid that uses three desktop columns (with a full-width final card to avoid an orphan) and one mobile column. Add lightweight process-step styling that reuses existing cards, borders, dark text, copper labels and visible focus conventions.

**Step 2: Add semantic primary content**

Insert `section#one-off-projects` after the existing service introduction. Include verbatim:
- `One-off projects with a clear finish line`
- its approved supporting sentence
- the seven exact names/ranges exactly once each
- the exact prices qualification immediately after the list
- four ordered fixed-scope process steps, including scope, price, inclusions, deliverables and completion date agreed in writing.

Do not add per-service deliverables, durations, guarantees or unsupported claims.

**Step 3: Run content and order checks**

Run the verifier. Expected: exact primary content is present once, has correct source order before `#work`, and contains no prohibited exclusive-choice wording.

### Task 5: Add optional support after the first project

**Objective:** Keep support visible but explicitly secondary and non-mandatory.

**Files:**
- Modify: `index.html` (embedded CSS and new section after the one-off process)
- Test: `/tmp/verify-ai-services-one-off.py`

**Step 1: Add restrained support-plan styling**

Add a responsive three-card grid that remains light/cream, stacks Essential → Standard → Premium at mobile widths, and does not introduce a dark pricing wall, tabs or horizontal scrolling.

**Step 2: Add exact support copy and plans**

Insert `section#ongoing-support` after the one-off process and before `#work`. Include the exact heading and introductory copy, the three legacy plans with every price, cadence, response term, adjustment allowance, update/queue entitlement and best-for qualifier unchanged, plus a CTA that invites a discussion after a first project and targets `#contact`.

**Step 3: Run content/order/framing checks**

Run the verifier. Expected: plans and support copy are exact, support follows one-off process, and the non-required subscription sentence is present while exclusive or mandatory framing is absent.

### Task 6: Complete robust local source validation

**Objective:** Verify static-site correctness before rendering or committing implementation.

**Files:**
- Test: `/tmp/verify-ai-services-one-off.py` (temporary only; do not commit)
- Inspect: `index.html`

**Step 1: Complete the ad-hoc verifier**

The script must fail non-zero for missing/duplicate exact copy or prices, prohibited exclusive framing, stale subscription-only hero wording, unresolved `#id` links, missing local demo/link files, broken HTML parser structure, visible surname occurrences outside functional email addresses, incorrect order of new sections, or unsupported stale page wording.

**Step 2: Run the verifier**

Run:
```bash
python3 /tmp/verify-ai-services-one-off.py /home/simon/ai-services/index.html
```

Expected: PASS with checked exact strings, anchors, source order, HTML parse status, surname scan and framing scan reported.

**Step 3: Inspect the diff**

Run:
```bash
git diff --check
git diff -- index.html
git status --short
```

Expected: only `index.html` is changed after the plan commit, with no whitespace errors or unrelated edits.

### Task 7: Test the rendered site in desktop and mobile browsers

**Objective:** Exercise the actual static page at desktop and 390px mobile widths.

**Files:**
- Serve: `/home/simon/ai-services/index.html`
- Test: `/tmp/verify-ai-services-one-off.py`

**Step 1: Start a local static server**

Run:
```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Expected: `http://127.0.0.1:8765/` serves the candidate page.

**Step 2: Browser-test desktop**

At a desktop viewport, inspect the hero, one-off cards, process, support cards, work and contact sections. Exercise new project and support CTAs, confirm text is visible, the seventh one-off card is intentionally placed, and browser console has no errors.

**Step 3: Browser-test 390px mobile**

At 390px width, inspect source-order stacking, tappable CTA controls, no horizontal overflow, visible text/prices, section hierarchy, and no console errors. Exercise fragment links from hero/navigation.

**Step 4: Record actual browser evidence**

Keep screenshots or browser-driver output plus measured overflow and console/link results for the release report.

### Task 8: Commit, push and verify the actual Pages deployment

**Objective:** Publish only the reviewed plan and implementation to the configured Pages source, then prove the live revision.

**Files:**
- Modify: `index.html`
- Commit: plan and implementation commits

**Step 1: Commit the reviewed implementation**

Run:
```bash
git add index.html
git commit --author='Simon Fung <simonfungwork@gmail.com>' -m 'feat: lead with one-off projects and optional support'
git push origin main
```

Expected: push advances remote `main`; no Pages configuration change is needed because source is already `main` at `/`.

**Step 2: Poll GitHub Pages build status**

Query the Pages builds API until a `built` deployment records the implementation SHA. If a build fails or remains stale, capture the API evidence and stop rather than claiming release.

**Step 3: Verify the cache-busted live revision**

Fetch:
```bash
curl -sSL -H 'Cache-Control: no-cache' 'https://492kw.github.io/ai-services/?v=<implementation-sha>'
```

Expected: HTTP 200 and returned HTML contains all exact entry, one-off and support content, has no stale/mandatory/exclusive framing, and exposes both `#one-off-projects` and `#ongoing-support`.

**Step 4: Browser-check the same live cache-busted URL**

Repeat desktop and 390px checks against the live URL. Confirm the rendered live revision is the combined current repository design plus the new primary one-off and secondary support model.

**Step 5: Final Git evidence**

Run:
```bash
git status --short --branch
git log --oneline --decorate -4
```

Expected: clean `main` aligned with `origin/main`, with both the documentation-plan and implementation commits present.
