---
name: logistics-workbench
description: Create or refine a professional logistics operations workbench that extends an existing AI Harness or business platform with order intake, settlement reconciliation, proof-of-delivery, and TMS entry points. Use for logistics-workbench UI planning, HTML prototypes, or implementation; preserve the host product shell and visual style unless the user requests a replacement.
---

# Logistics Workbench

Design a logistics operations workspace as an extension of the user's existing Harness or business platform. Keep the host product recognizable: retain its brand, navigation, account controls, workspace controls, and existing tools. Add the logistics capabilities as a plugin or clearly grouped extension; do not turn the workbench into a separate replacement shell unless asked.

## Understand the shell and scope

- Inspect any supplied screenshots, open page, files, or repository before choosing layout and implementation.
- Identify which host navigation and controls must remain. Place logistics features within the host's existing extension/plugin model when available.
- Match the host's color palette and component style. When the user asks for the light Harness look, use a light neutral surface, restrained borders, and the host's existing accent color instead of introducing a dark standalone sidebar.
- Use the user's product name and TMS URL when provided. Keep sample companies, names, dates, counts, and addresses clearly fictional in prototypes.

## Shape the logistics information architecture

A practical starting structure is:

- **Order processing:** accept image/screenshot, spreadsheet, and pasted-text inputs; extract standard order fields; expose uncertain or missing fields for review; require a user confirmation step before presenting an order as ready for TMS submission.
- **Settlement reconciliation:** organize the dispatch schedule, rate card, customer settlement statement, and driver settlement statement; show matching coverage, amount differences, unmatched records, and review actions; support a result spreadsheet after review.
- **Proof of delivery:** accept receipt images, extract delivery information, propose an order/waybill association, let users resolve uncertain matches, and show archive status.
- **TMS application:** provide a configurable URL entry point. Choose a link, embedded view, or deeper integration based on the user's existing system and request; do not imply that URL configuration alone creates an API integration.

Keep review and confirmation visible in each workflow. AI can extract, match, and summarize; the UI should make uncertain values and user decisions easy to inspect.

## Build the prototype or implementation

- Follow the requested deliverable. For a standalone HTML prototype, make it self-contained where practical and use responsive HTML/CSS/JavaScript. In an existing product repository, follow its framework, conventions, and design system.
- A useful first screen includes operational counts, the three workflow entry points, recent processing activity, items needing attention, and TMS connection status.
- Make important paths demonstrable: switch between modules; choose image/spreadsheet/text input for orders; preview structured fields; show the four settlement inputs and discrepancy summary; show receipt matching and unresolved cases; configure the TMS URL.
- If backend services are not available, use clearly labelled sample data and lightweight simulated interactions. Do not claim that uploads, AI processing, persistence, or TMS submission are live.
- Keep reusable visual elements consistent: spacing, type scale, button hierarchy, status labels, empty states, and confirmation affordances.

## Deliver and refine

- Make the artifact easy to open and review. If a preview environment is available, open the finished prototype there.
- Summarize what the prototype covers and distinguish simulated behavior from connected functionality.
- Treat feedback as a refinement of the current work: preserve agreed host-shell constraints and update only the areas the user steers.

## Reference implementation

`assets/logistics-workbench.html` is the HTML prototype created for this workflow. Use it as a starting point or visual reference when useful; adapt its mock data, labels, and interactions to the user's actual product rather than treating them as fixed requirements.
