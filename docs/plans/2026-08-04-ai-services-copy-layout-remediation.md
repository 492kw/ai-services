# AI Services copy and layout remediation — 2026-08-04

## Scope

Refresh the existing GitHub Pages homepage without changing its approved cream-and-copper identity, navigation hierarchy, one-off-first funnel, seven one-off services/prices, or subscription prices and entitlements.

## Findings from the deployed baseline

- The header brand, metadata, structured data, hero microcopy, contact CTA and footer use “Simon”.
- Several headings and descriptions read as generic or slogan-like rather than plain business copy.
- The seventh one-off service is given a desktop-only special placement with `.one-off-card:last-child { grid-column:2 / span 2; }`. It makes card 07 twice as wide and offset beneath cards 05–06; this is the source of its accidental appearance. The fixed 145px card height also leaves too little resilience for longer service names at narrower widths.

## Remediation

1. Replace the brand exactly with `AI Services`; update title, social metadata, image alt text and JSON-LD to the same business identity. Keep the functional email address unchanged.
2. Rewrite public copy in a warm, plain-speaking Australian voice. Use first-person singular only in the introductory/contact context, remove third-person proprietor wording, filler and slogan-style phrasing, and retain legitimate service references to AI.
3. Make the one-off grid a responsive two-column layout on wider screens and one column on small screens. Remove every special last-card placement rule. Use a shared auto row height with enough padding/minimum height so headings and price lines remain inside their cards.
4. Check local HTML, links, copy constraints and all requested rendered viewports. Capture durable full-page screenshots and programmatically verify layout, fragment links, overflow, clipping, contrast and browser errors.
5. Commit only intended source files, push `main`, poll GitHub Pages for that commit, then repeat the checks against a cache-busted live URL.
