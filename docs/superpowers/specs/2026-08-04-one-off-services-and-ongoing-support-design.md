# One-off services and ongoing support design specification

**Status:** Approved design specification only — no website implementation, deployment, or push is authorised by this document.

**Purpose:** Change the public site’s commercial journey so a visitor can begin with a low-risk, fixed-scope project, see a useful result, and then choose ongoing support only if it is useful. One-off work and support must be presented as complementary stages, never as an either/or choice.

## Context and release boundary

- Repository: `/home/simon/ai-services`
- Current local repository design: cream paper background, copper accents, dark ink typography, light bordered cards, rounded controls, responsive grids and the existing practical-consulting tone in `index.html`.
- There is a repository/live mismatch. The implementation release must deploy the combined current repository design **and** this one-off-project model **and** the secondary ongoing-support model together. Do not deploy only one model or rely on the currently live page as the implementation baseline.
- This is a design specification. The current task must create only this document and make a local documentation commit. It must not change `index.html`, assets, configuration, deployment settings, or the live GitHub Pages site.

## Visitor journey and message hierarchy

The primary journey is:

> Small problem → simple one-off project → useful result → optional ongoing support

The page must make this sequence clear in its heading order, visual order and calls to action:

1. A visitor identifies a small, specific operational problem.
2. The visitor is invited to start with a clearly scoped project and one-time payment.
3. The visitor sees the seven fixed-scope service categories and typical price ranges.
4. The visitor understands the scope/price/deliverables/completion-date agreement before work starts.
5. Only after the one-off services and process does the visitor encounter ongoing support as an optional continuation.

Do not use choice language such as “one-off or subscription”, “choose a plan to get started”, “subscription required”, or wording that implies support is a prerequisite for the one-off project. Do not hide ongoing support; it is a legitimate secondary offer after a useful first result.

## Required entry copy

Place this copy prominently near the first project-oriented CTA in the hero or immediately following introductory services content. It must appear verbatim, including punctuation:

> Start with one useful improvement.
>
> Begin with a clearly scoped project, a one-time payment and an agreed completion date. It’s a practical, low-risk way to see what works before making a larger commitment.

The nearby CTA should take the visitor to the one-off services section (for example, `href="#one-off-projects"`) rather than jumping directly to subscription support. A secondary CTA may continue to point to work examples or contact.

## Primary section: one-off projects

### Section heading and supporting copy

Add the primary commercial section after the existing service introduction and before the existing examples/process content. Use a stable anchor such as `id="one-off-projects"`.

The heading must be exactly:

> One-off projects with a clear finish line

Its supporting copy must be exactly:

> Start with the simplest useful implementation. Before work begins, we’ll agree on the scope, price, deliverables and completion date.

Use a section kicker only if it reinforces the fixed-scope, low-risk offer without contradicting the required copy.

### Exact service list

Render the following seven items exactly. Preserve the service names, currency marks, dash punctuation and ranges. These are typical project ranges, not subscription prices.

1. Small-business AI consultation — $250–$500
2. AI workflow assessment — $350–$750
3. Website setup or repair — $500–$1,500
4. Local AI installation — $750–$2,000
5. Home technology and parental-control setup — $250–$600
6. Small-business security review — $400–$1,000
7. Email, document or quoting automation — $750–$2,500

Use readable service cards or a compact, searchable-at-a-glance price list consistent with the existing cream/copper card system. Each item must be legible without hover interaction. Do not introduce fabricated deliverables, time estimates, guarantees, or feature lists for an individual service category.

### Required qualification

Place this qualification immediately below the one-off service list, before the process details or CTA. It must appear verbatim:

> Prices are typical ranges. Your final scope, fixed price, inclusions and completion date are agreed in writing before work starts.

### One-off process

Follow the price qualification with a short process that makes the fixed-scope agreement tangible. Reuse the current practical-process visual language where possible, but make the steps specific to the first project:

1. Discuss the small problem and desired useful outcome.
2. Agree in writing on scope, price, inclusions, deliverables and completion date.
3. Build and test the simplest useful implementation.
4. Complete the agreed handover and identify whether any next improvement is worthwhile.

The one-off process may update or sit immediately before the current broader `#approach` content. It must not promise perpetual changes, unspecified scope, or support entitlements.

## Secondary section: optional ongoing support

Place this section after the one-off services and one-off process. Use a stable anchor such as `id="ongoing-support"`. Its visual weight should be clearly secondary to the one-off section while remaining easy to find: a cream/light card group, restrained copper labels and existing dark-ink text are preferred. Do not use a dark, high-pressure pricing wall.

The heading must be exactly:

> Support after your first project

The introductory copy must be exactly:

> If the first project proves useful, ongoing support is available to keep your systems monitored, maintained and improving. There is no requirement to subscribe after a one-off project.

### Legacy support plans retained as factual secondary content

Reintroduce these existing support plans as factual secondary information. Preserve every included entitlement and “best for” qualifier. Do not relabel them as mandatory starting plans.

The rendered plan copy must preserve these factual legacy plans verbatim:

- Essential $100/mo + GST (monthly monitoring, next-business-day response, 1 adjustment/month, quarterly updates, best for 1 automation)
- Standard $180/mo + GST (weekly monitoring, same-business-day response, 3 adjustments/month, monthly updates/check-in, best for 1–3 automations)
- Premium $500/mo + GST (daily monitoring/alerts, within-4-hours response, unlimited adjustments, rolling updates, priority feature queue, best for 3+ automations)

A comparison table or cards may format the same information for scanning, but must not omit or alter any listed entitlement. “Within-4-hours” is the stated response target; do not add unsupported availability qualifications. Use a contact CTA phrased as an invitation to discuss support after a first project, not to select or purchase a plan online.

## Navigation, links and calls to action

- Add an in-page navigation item or clearly visible route to `#one-off-projects` if it fits the current navigation without crowding mobile layout.
- The primary project CTA must land on `#one-off-projects`.
- A support CTA, if used, must land on `#ongoing-support`.
- Keep existing demonstration links (`social-tennis-program.html`, `ocr-demo/`, `tradie-demo/`, `website-demo/`) and the contact email action working.
- Keep the skip link and existing in-page anchors valid. Update any changed anchor references so no link resolves to a missing target.
- Keep contact language focused on a short, non-sensitive outline; do not ask visitors to send passwords, complete client records or sensitive documents.

## Visual and responsive direction

Maintain the current repository design rather than introducing a new visual theme:

- Cream/off-white page background, warm copper accents, dark opaque text, light surfaces and restrained shadows.
- Existing rounded cards, border treatment, typographic scale and button style.
- One-off service cards: use a responsive grid that presents seven items cleanly. On desktop, use an intentional asymmetric or three-column arrangement that avoids a visually orphaned seventh card; on mobile, stack to one column in the source journey order.
- Support plans: use three clearly differentiated but equally readable cards or a compact comparison layout. On mobile, stack Essential, Standard, Premium in that order with no horizontal scrolling.
- Price and response terms must retain readable contrast and not rely on copper alone to convey meaning.
- Do not use pop-ups, carousels, accordions, tab-only content, hover-only pricing details, countdowns, “limited spots” urgency, or dark neon/gaming styling.
- Keep keyboard focus visible, semantic heading order correct and reduced-motion behaviour intact.

## Implementation scope for the later build

The later implementation should normally modify only `index.html` unless a link validation or deployment configuration issue demonstrably requires a minimal additional change. Do not alter the demonstrations, assets, unrelated public pages, social card, robots file or sitemap solely for this offer change.

Recommended implementation sequence:

1. Inspect the current `index.html`, current deployed Pages response and all current in-page links; record the repository/live mismatch before editing.
2. Add the primary entry copy and route its CTA to `#one-off-projects`.
3. Add the one-off section, exact services, qualification and one-off process.
4. Add the secondary `#ongoing-support` section, exact copy and three factual support plans after the one-off process.
5. Update navigation/CTA targets and responsive CSS while retaining the current cream/copper design system.
6. Validate locally before committing.
7. Commit the implementation separately from this specification, push only when separately authorised, then poll GitHub Pages and perform cache-busted live checks.

## Acceptance tests for the later implementation

### Content and framing

- [ ] The two required entry-copy sentences are present verbatim.
- [ ] `One-off projects with a clear finish line` is present verbatim as the primary section heading.
- [ ] Its required supporting copy is present verbatim.
- [ ] All seven one-off service names and price ranges are present exactly once in the public offer section.
- [ ] The required one-off price qualification is present verbatim.
- [ ] `Support after your first project` appears after the one-off service list and one-off process.
- [ ] The required ongoing-support copy is present verbatim.
- [ ] Essential, Standard and Premium retain the stated prices, monitoring cadence, response target, adjustment allowance, update cadence/feature queue and best-for qualification.
- [ ] The page describes the journey as small problem → simple one-off project → useful result → optional ongoing support.
- [ ] No page wording frames one-off work and ongoing support as exclusive choices or makes subscription support mandatory.

### Local rendering and links

- [ ] Open the changed site locally using a static server bound to a safe local port, then test desktop and mobile viewport widths.
- [ ] At desktop width, the new one-off and support sections have no collisions, clipped prices, orphaned CTA, unreadable contrast or unintended horizontal scrolling.
- [ ] At mobile width (at least 375 px), the service list and support plans stack cleanly, buttons remain tappable, and no horizontal scrolling is introduced.
- [ ] Keyboard-tab through the skip link, navigation, new project CTA, support CTA, demo links and contact links; visible focus remains present.
- [ ] Programmatically verify every local `href` target either resolves to an existing local file or an existing in-page ID. Manually exercise every changed/new CTA.
- [ ] Run a local HTML validation/lint command available in the repository environment and record the actual output. If no validator is installed, use a documented parser/link-check fallback and state the limitation rather than claiming formal validation.

### Deployment verification after separate authorisation

- [ ] Push only the separately approved implementation commit.
- [ ] Poll GitHub Pages until the deployed revision is reachable; do not assume a successful push means Pages is updated.
- [ ] Fetch `https://492kw.github.io/ai-services/?v=` followed by the actual implementation commit SHA or an ISO-safe release timestamp after deployment, and verify the exact required copy, anchors and affected links in the returned live HTML.
- [ ] Perform a cache-busted browser check at desktop and mobile viewport widths against the same deployed URL.
- [ ] Confirm the live version contains the combined current repository design plus both the one-off and optional-support models, not a stale live design or one model alone.

## Self-review criteria

Before implementation, review the rendered page and source against this specification for:

- Placeholders, TODOs, lorem ipsum, fake testimonials, unsupported claims, fabricated deliverables or missing pricing details.
- Contradictions between a fixed-scope, one-time project and any “unlimited” or ongoing entitlement. “Unlimited adjustments” applies only to the Premium ongoing-support plan.
- Ambiguity about whether a visitor must subscribe after a first project; the answer must remain clearly no.
- Ambiguity about what is agreed in writing before work starts; scope, fixed price, inclusions, deliverables and completion date must be clear.
- Broken, stale or misleading navigation and CTA destinations.
- Any deviation from the current cream/copper visual direction or any regression in mobile/desktop usability.
- Repository/live mismatch: confirm the release candidate combines the current repository design and both commercial models before deployment.
