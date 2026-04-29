---
name: huashu-deck-pdf-export
description: PDF generation from web layouts
version: "2.0.0"
verified_date: 2026-04-29
category: core
---

# Web to PDF Export (Redesigned)

## Purpose
Generate high-fidelity, print-ready PDF layouts directly from the browser using strict CSS `@media print` rules.

## Hard Usage Rules (Tier 3: Strict Structural Constraints)
- **ALLOWED**: When building dashboards or reports that require print/PDF capabilities.
- **FORBIDDEN**: Generating headless browser (Puppeteer) scraping scripts.
- **CONSTRAINT**: Must exclusively rely on native browser print APIs (`window.print()`).

## New Execution Strategy (Print-Stylesheet Enforcement)
1. **Abandon Puppeteer Scripting**: Do not generate backend Node.js scraping scripts to render PDFs.
2. **CSS Print Media**: Inject a strict `@media print` CSS layer into the application.
3. **Break Controls**: Enforce `break-inside: avoid` on all major container blocks (cards, charts, tables) to prevent layout tearing across pages.
4. **Fixed Layouts**: Rely on strict A4/16:9 CSS aspect ratios combined with `page-break-before` and `page-break-after`.

## Safety Guardrails & Patched Prevention
- **Print Script Patch**: Never generate headless browser scripts. Only generate print CSS media queries.
- **Z-Index Flattening Patch**: Ensure all sticky/fixed headers are reset to `position: static` within `@media print`.
- **Self-Rejection Clause**: If asked to write a Puppeteer or Playwright script for PDF generation, **ABORT OUTPUT** and enforce native browser printing.

## Maintenance Notes
- Complete redesign from v1. Deprecated Puppeteer automation in favor of robust CSS `@media print` engineering.