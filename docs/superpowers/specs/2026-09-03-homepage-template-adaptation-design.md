# Homepage Template Adaptation Design

**Date:** 2026-09-03

## Goal

Adapt the existing personal homepage in this repository so it closely matches the visual structure and information hierarchy of [https://jianshuod.github.io/jianshuod/](https://jianshuod.github.io/jianshuod/) while preserving Yijing Liu's own facts, publications, links, and supporting sections.

## Confirmed Direction

- Use the reference homepage as the source of truth for layout and styling.
- Preserve all existing sections: `About`, `Publications`, `Education`, `Awards`, `Academic Services`, `Presentations`, `Teaching`, and `Misc`.
- Add a `News` section between `About` and `Publications`.
- Keep the page as a single static homepage.
- Preserve factual content and working links; do not import the template owner's biography or publication records.

## Structural Changes

### Sidebar

- Replace the current boxed sidebar card with the reference template's simpler left column.
- Keep Yijing Liu's photo, English and Chinese names, affiliation, and primary links.
- Use the reference-style profile link cluster instead of icon-only social links.

### Main Navigation

- Replace the current sidebar contents navigation with the reference-style sticky top navigation.
- Include links for:
  - `About Me`
  - `News`
  - `Publications`
  - `Education`
  - `Awards`
  - `Services`
  - `Presentations`
  - `Teaching`
  - `Misc`

### Main Content

- Use the reference page's flat editorial layout rather than boxed content cards.
- Reorder the page to:
  1. `About Me`
  2. `News`
  3. `Publications`
  4. `Education`
  5. `Awards`
  6. `Academic Services`
  7. `Presentations`
  8. `Teaching`
  9. `Misc`

## Publications Treatment

- Follow the reference template's publication row pattern:
  - title first
  - venue on a dedicated metadata line
  - authors on the next line
  - resource links below
- Remove the current left-hand venue column.
- Keep Yijing Liu visually emphasized in author lists.
- Standardize resource labels to the reference style, with `PDF`, `PPT`, and `DOI` where the link exists.
- Do not invent missing resources. If no presentation link exists, omit `PPT`.

## News Section

- Add a compact `News` section using factual milestones already present in the homepage content.
- Initial entries may be derived from:
  - NTU visiting researcher start in February 2026
  - IMC 2025 presentation
  - USENIX Security 2024 presentation

## Styling

- Use the reference site's typography, spacing, navigation, and publication styling as closely as practical.
- Prefer the reference's lighter editorial look over the current heavier card treatment.
- Keep dark mode and back-to-top behavior.

## Verification

- Add regression checks for:
  - section order
  - top navigation contents
  - reference-style profile links
  - reference-style publication markup
  - `PPT` label normalization where presentation links exist
- Manually verify the page in a browser on desktop and mobile widths.
