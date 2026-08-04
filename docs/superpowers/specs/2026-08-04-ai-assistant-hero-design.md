# AI assistant hero design specification

**Status:** Approved design specification only. This document authorises neither implementation nor deployment.

**Purpose:** Make the first-contact message on the AI Services home page clearly about an AI assistant working alongside a small-business team. The new message replaces the current hero proposition and its project-screenshot panel; it must not become an additional competing section.

## Approved hero copy

Use these two lines exactly, including punctuation and capitalisation:

> Your AI assistant, working in your office.
>
> Like adding a reliable team member—available 24/7, never off sick, and focused on the repetitive work that holds your business back.

The first line is the sole page `h1` and is the dominant first-contact message. The second line is the primary supporting paragraph directly below it. Do not split, paraphrase, qualify, or add marketing claims to either approved line.

## Current-state findings

### Repository and baseline

- Repository: `/home/simon/ai-services`
- Remote: `https://github.com/492kw/ai-services.git`
- Branch at design time: `main`, tracking `origin/main`.
- Working tree at design time: clean.
- Baseline commit at design time: `c77e0a51b601faa88eca0bbf828dfc4dbfc4cf33` (`Repair project and case study grid layout`).
- The recent preceding commits are `b387b16` (`Refine AI Services copy and one-off project grid`) and `2c5ee19` (`feat: lead with one-off projects and optional support`).

### Current hero structure in `index.html`

The current first content element is `section.wrap.hero#top` at line 47. It is a two-column CSS grid defined at line 30 (`1.03fr .97fr`, `3rem` gap) and becomes one column at `max-width:900px`.

Its left column contains, in order:

1. Eyebrow: `Brisbane + remote Australia`.
2. Current `h1`: `Practical tools for work that slows you down.` with the latter phrase in copper.
3. Introductory paragraph about practical web tools and automation.
4. Primary and secondary calls to action: `Start a small project` to `#one-off-projects`, and `See working examples` to `#work`.
5. An `entry-copy` callout headed `Start with a focused first project.`
6. A short non-sensitive-enquiry microcopy paragraph.

Its right column is `aside.hero-panel`, labelled `Preview of practical software projects`. It contains the project image `assets/portfolio/tennis-app.png`, alt text describing the tennis allocation application, and captions `real project screenshot` and `working browser tool`.

The existing page already has a later `#work` section containing the tennis-app screenshot as a working example. The existing `#approach` section also uses the wording “slowing work down” in body copy, but the current hero H1 is the dominant occurrence of the “work that slows you down” proposition.

## Design and content changes for the later implementation

### 1. Replace the hero proposition, not the page structure

Keep the existing hero as the first page section, its `#top` anchor, one-H1 structure, left/right responsive grid, eyebrow, and existing call-to-action destinations. Replace the current H1 and its adjacent introductory paragraph with the approved hero copy.

- Replace the current H1 in full with `Your AI assistant, working in your office.`
- Remove the current copper-highlighted span treatment from the H1. The approved sentence must read continuously and must not imply that only part of the proposition is important.
- Put the approved supporting line in the hero’s main introductory paragraph directly below the H1.
- Retain `Brisbane + remote Australia` as the contextual eyebrow unless a later, separately approved content change replaces it.
- Retain the current CTA labels and targets: `Start a small project` → `#one-off-projects`; `See working examples` → `#work`.
- Retain the focused-first-project callout and non-sensitive-enquiry microcopy below the CTAs. They provide the next step after the new hero proposition and must remain visually secondary to it.

### 2. Demote the competing “tasks that slow your business down” proposition

The wording and hierarchy must make the approved AI-assistant proposition the clear first-contact thesis.

- Remove the current hero phrase `Practical tools for work that slows you down.` entirely; it must not remain in the H1, a hero heading, or an equivalent high-emphasis callout.
- Do not create a new “Tasks that slow your business down” section, banner, badge, or alternative H2 near the hero.
- The later `#approach` body phrase about a hand-off, repetition, or decision “slowing work down” may remain only as explanatory process copy. It must not be promoted to a heading, visually highlighted phrase, or early-page competing proposition.
- Keep the existing service, one-off-project, support, work, approach, scope, and contact sections in their current order. This change is a hero reframing, not a new content journey.

### 3. Replace the current project-screenshot area with an office-assistant visual panel

Replace the current `aside.hero-panel` project preview completely. Do not add a second hero panel or a separate visual section.

The new right-hand panel must be a warm, light office-assistant illustration constructed from semantic HTML and CSS within `index.html`; it must not require a new image asset. Its job is to make the AI-assistant idea immediately legible without looking like a software dashboard or a stock-photo substitute.

Use this precise visual direction:

- Keep the existing light `--surface` panel, warm cream page, copper border/accent, rounded corners, and restrained shadow so the panel belongs to the current design system.
- Replace the `figure`, screenshot image, and captions with a compact illustrative scene: a paper-like task sheet, a small desk/monitor shape, a copper status marker, and several short, non-readable task lines. The composition should suggest an assistant quietly clearing routine office work.
- Use only abstract marks, short decorative lines, and generic non-readable labels in the illustration. Do not invent client names, results, messages, metrics, testimonials, logos, or claims.
- Give the panel an accessible text alternative using a concise visible or screen-reader-only description such as “Illustration of an AI assistant organising routine office tasks.” Decorative child shapes and lines must be hidden from assistive technology.
- Do not retain `assets/portfolio/tennis-app.png`, its screenshot alt text, or the `real project screenshot` / `working browser tool` captions in the hero. The image remains available in the later working-examples section.
- The panel must be visually subordinate to the H1: it supports the message rather than competing with it. Avoid animation, live status indicators, counters, charts, code snippets, fake chat bubbles, or dense dashboard UI.

### 4. Layout hierarchy

At desktop widths, retain the two-column hero. Give the left copy column enough width for the approved H1 and supporting line to remain the strongest visual element. The office-assistant panel occupies the existing right-column location and approximately the same visual footprint as the current hero panel; it must not increase the hero to the point that the one-off-project CTA is pushed below the initial viewport on common laptop layouts.

Within the left column, maintain this order:

1. Brisbane/remote eyebrow.
2. Approved H1.
3. Approved supporting line.
4. Existing project and examples CTAs.
5. Existing focused-first-project callout.
6. Existing non-sensitive-enquiry microcopy.

Do not introduce another H1. Preserve an unbroken semantic heading sequence across the remainder of the page.

## Responsive and accessibility requirements

- At widths above 900 px, retain the existing two-column hero arrangement with readable whitespace between copy and the illustration.
- At 900 px and below, preserve the existing single-column hero behaviour: copy first, then the office-assistant panel. Do not reorder the panel before the approved copy.
- At 375 px wide and above, the H1, supporting paragraph, CTA buttons, callout, and visual panel must fit without horizontal scrolling, clipping, overlap, or text that relies on truncation.
- Preserve the existing mobile hero padding and the current CTA wrapping behaviour. Ensure both buttons remain separately tappable with their existing minimum 46 px control height.
- Keep the existing `:focus-visible` treatment and skip link. Keyboard order must follow the visible order: navigation, hero CTAs, then subsequent page controls.
- Preserve sufficient contrast for the H1, supporting text, copper accents, panel border, and any illustration shapes. Copper must not be the only cue that communicates a task state or meaning.
- Treat all abstract illustration pieces as decorative (`aria-hidden="true"` or equivalent). Provide one meaningful label for the panel as a whole; do not expose a list of ornamental elements to screen readers.
- Retain the existing reduced-motion rule. The new visual panel must be static; do not add motion that would need an additional reduced-motion exception.

## Scope exclusions

This approved step creates only this design document and a local documentation commit.

The later implementation may modify `index.html` only, unless a demonstrable implementation necessity is separately approved. It must not:

- edit, create, remove, or replace files under `assets/`;
- edit the demos, `404.html`, `social-card.png`, favicon, robots file, sitemap, GitHub Pages configuration, or repository settings;
- change metadata, Open Graph content, navigation labels, CTA labels/destinations, service pricing, support-plan content, contact details, or later page sections beyond the explicitly stated hero-copy and hero-panel change;
- push, deploy, publish, or otherwise change the live GitHub Pages site;
- add analytics, external fonts, JavaScript dependencies, stock imagery, animation libraries, or third-party embeds.

## Acceptance criteria for the later implementation

### Content and hierarchy

- [ ] The page has exactly one H1, and it is exactly `Your AI assistant, working in your office.`
- [ ] The approved supporting line appears verbatim directly below the H1: `Like adding a reliable team member—available 24/7, never off sick, and focused on the repetitive work that holds your business back.`
- [ ] The old hero H1 `Practical tools for work that slows you down.` is absent.
- [ ] No new heading, card, banner, or early-page section presents “tasks/work that slow your business down” as a competing first-contact message.
- [ ] The hero remains the first content section and retains the existing eyebrow, CTA labels, CTA targets, focused-first-project callout, and non-sensitive-enquiry microcopy.
- [ ] The remaining page sections retain their current order and content except for the specific hero replacement described here.

### Visual panel and responsive rendering

- [ ] The previous tennis screenshot and its two captions are removed from the hero and remain available only in the later working-examples content.
- [ ] The existing hero right-column area contains one warm, light, office-assistant illustration panel made with semantic HTML and CSS, with no new image asset or external dependency.
- [ ] The panel uses the current cream/copper/light-surface/dark-ink visual language and is visually subordinate to the H1.
- [ ] At desktop width, the hero remains a two-column layout; at 900 px and below, it is one column with copy before panel.
- [ ] At 375 px wide, the hero has no horizontal overflow, overlap, clipped text, clipped buttons, or inaccessible controls.
- [ ] The illustration is static and does not add animations or motion effects.

### Accessibility and validation

- [ ] The hero’s single H1, panel label, and decorative child elements have the required semantics: a meaningful panel description and hidden ornamental pieces.
- [ ] Keyboard focus remains visible and tab order follows the visual reading order.
- [ ] The skip link and every existing changed-adjacent anchor/CTA still resolve to a valid page ID.
- [ ] Check desktop and mobile rendering in a real browser before any implementation commit.
- [ ] Run an available local HTML validator or parser/link-check fallback and record its actual output; do not claim formal validation if no validator is installed.

## Specification self-review

- No placeholders, TODOs, lorem ipsum, fabricated office content, fake metrics, testimonials, client names, or unsupported performance claims are permitted.
- The approved copy is quoted exactly in the dedicated copy section and repeated exactly in acceptance criteria.
- The visual requirement is unambiguous: replace the existing hero screenshot panel in place with one CSS/HTML office-assistant illustration panel; do not add a second section or a new asset.
- The message hierarchy is unambiguous: the AI-assistant H1 is primary; “work that slows you down” is removed from hero-level emphasis and may remain only as later explanatory body copy.
- The scope boundary is unambiguous: this design-document commit must not alter the site, assets, or deployment, and no push is authorised.
