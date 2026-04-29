---
name: huashu-html-to-pptx-conversion
description: PPTX generation from web data payloads
version: "2.0.0"
verified_date: 2026-04-29
category: core
---

# Data-to-PPTX Generation (Redesigned)

## Purpose
Programmatically generate PowerPoint (PPTX) presentations from underlying application data state, bypassing the DOM entirely.

## Hard Usage Rules (Tier 3: Strict Data-Mapping Constraints)
- **ALLOWED**: When exporting dashboard analytics, tables, or structured reporting data to PowerPoint.
- **FORBIDDEN**: Attempting to parse, scrape, or translate HTML/DOM elements into PPTX coordinates.
- **CONSTRAINT**: Must map directly from JSON state to `PptxGenJS` models.

## New Execution Strategy (Data-to-Presentation Mapping)
1. **Abandon DOM Scraping**: Do not attempt to map raw DOM nodes or CSS styles to `PptxGenJS` layouts.
2. **Data Extraction**: Extract the raw JSON payload powering the dashboard components.
3. **Transformation Pipeline**: Generate a pure JavaScript transformation function that translates the JSON data array directly into structured `PptxGenJS` slide models.
4. **Explicit Coordinates**: Define PPTX component coordinates (x, y, w, h) purely via mathematical offsets based on data arrays, completely ignoring visual HTML layouts.

## Safety Guardrails & Patched Prevention
- **DOM Parsing Patch**: Never use `document.querySelector` or DOM traversal to build PPTX slides. 
- **Self-Rejection Clause**: If the user requests to "convert this HTML to PPTX", **ABORT OUTPUT**. Emit: *"REJECTED: Skill is classified as Unsafe for HTML-to-PPTX. Supply the underlying JSON data payload to generate presentation slides."*

## Maintenance Notes
- Complete redesign from v1. Banned DOM-to-PPTX translation due to high failure rate, replacing it with strict JSON-to-PptxGenJS data modeling.