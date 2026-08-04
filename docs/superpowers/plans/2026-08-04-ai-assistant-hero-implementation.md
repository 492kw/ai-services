# AI assistant hero implementation plan

## Purpose

Implement the approved AI-assistant hero in the existing static AI Services home page, preserving the current design system, CTA destinations, later working-example screenshot, and all unrelated page content.

## Scope and file changes

- Modify `index.html` only for the approved hero copy, CSS/HTML office-assistant illustration, and related responsive styling.
- Add `scripts/verify-ai-assistant-hero.py` as a dependency-free, repo-owned static verification script. It will parse `index.html` with Python standard-library `html.parser`, inspect all local `href`/`src` targets, and fail with explicit messages for the hero acceptance conditions.
- Do not alter `assets/`, demos, page metadata, navigation, other sections, or third-party dependencies.

## Implementation steps

1. Establish the clean baseline and intended branch.
   - Run `git status --short --branch`, `git log --oneline --decorate -5`, and `git diff --check`.
   - Stop if the tree is not clean or `main` is not based on approved commit `e97e3e06278fa8310c94f52f1145939b081018b9`.

2. Replace the existing hero copy in `index.html`.
   - Keep `section.wrap.hero#top`, the eyebrow, `aria-labelledby`, CTA labels and targets, entry callout, and microcopy in their existing order.
   - Make the sole hero H1 exactly `Your AI assistant, working in your office.` with no accent span.
   - Replace the adjacent introductory paragraph with exactly `Like adding a reliable team member—available 24/7, never off sick, and focused on the repetitive work that holds your business back.`
   - Do not change the later explanatory `#approach` body copy.

3. Replace only the hero visual content with a semantic CSS/HTML illustration.
   - Remove the hero `figure`, tennis screenshot, image alt text, and two screenshot captions.
   - Keep the existing `.hero-panel` shell and create one labelled panel, for example an `aside` with `aria-label="Illustration of an AI assistant organising routine office tasks."`.
   - Add a paper-like task sheet, small desk/monitor shape, copper status marker, and generic non-readable task marks as static child elements with `aria-hidden="true"`.
   - Add narrowly scoped CSS under the existing hero styles. Use existing custom properties (`--surface`, `--paper`, `--soft`, `--line`, `--copper`, `--ink`, `--muted`) and retain light surface, copper border/accent, round corners, and restrained shadow.
   - Size the panel so it remains secondary to the H1, uses the existing desktop grid, and follows the current one-column copy-then-panel rule at `max-width:900px`; add only necessary small-screen sizing safeguards.

4. Add `scripts/verify-ai-assistant-hero.py`.
   - Parse the page structurally and identify the `section#top` subtree.
   - Assert exactly one page H1 and the exact approved H1/supporting line once each in the hero.
   - Assert the old H1 and old screenshot asset/reference/caption strings are absent from the hero while the tennis image remains in the later `#work` section.
   - Assert hero CTA labels/fragment targets resolve to IDs, panel accessibility label is present, decorative illustration descendants are hidden, and no external image or new hero image is used.
   - Assert every local root-relative or relative `href`/`src` target resolves on disk, excluding fragment, mailto, telephone, data, and HTTP(S) URLs.
   - Assert visible title/metadata/body branding contains AI Services and does not expose Simon’s name outside functional email addresses.
   - Print a deterministic pass/fail summary and nonzero exit status on a failure.

5. Run static checks and inspect the change.
   - Run `python3 scripts/verify-ai-assistant-hero.py`.
   - Run `python3 -m py_compile scripts/verify-ai-assistant-hero.py`, `git diff --check`, and `git diff -- index.html scripts/verify-ai-assistant-hero.py`.

6. Run browser-based local verification.
   - Start the static server with `python3 -m http.server 8000 --bind 127.0.0.1` from the repository root.
   - Use a real Chromium/Firefox browser and browser screenshot tooling to capture full-page renders at 1440, 1024, 768, and 390 CSS pixels under `artifacts/ai-assistant-hero/local/` (untracked local evidence only).
   - At each size, inspect hierarchy, overflow, clipping, overlap, light backgrounds with opaque dark text, and the one-column copy-before-panel mobile layout. At 390 px, keyboard-tab to both hero CTA links and verify visible focus and independent tappable controls. Inspect the browser console for errors.
   - Repair only hero/check issues discovered, then repeat all checks and screenshots.

7. Commit and publish only after checks pass.
   - Commit this plan first with `git -c user.name='Simon Fung' -c user.email='simonfungwork@gmail.com' commit`.
   - Commit implementation and verification script with the same identity after reviewing `git diff --stat`, `git diff --check`, and `git status --short` to ensure only `index.html` and `scripts/verify-ai-assistant-hero.py` are tracked implementation changes.
   - Push `main` with `git push origin main`.

8. Verify deployment.
   - Poll the GitHub Pages workflow/run or the live URL until deployed.
   - Use cache-busted requests to `https://492kw.github.io/ai-services/` to require HTTP 200, exact approved H1/supporting line, and absence of the old H1 in live HTML.
   - Check live local assets/links from parsed HTML and capture full-page live screenshots at 1440, 1024, 768, and 390 CSS pixels under `artifacts/ai-assistant-hero/live/`.
   - When available, compare the deployed GitHub Pages source/deployment commit to the pushed implementation commit.

## Self-review checklist

- The plan limits page implementation changes to the approved hero and keeps the later tennis case study intact.
- The verification script is a minimal implementation necessity, uses no dependencies, and checks every requested static requirement.
- Browser checks cover all requested viewport sizes, focus visibility, layout, console errors, local and live evidence.
- Commit identity, diff review, push, deployment polling, cache-busted live-content checks, and final status are explicit.
