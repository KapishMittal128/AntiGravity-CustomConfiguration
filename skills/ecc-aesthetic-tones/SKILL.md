---
name: ecc-aesthetic-tones
description: Styling presets and layout constraints for minimalism, brutalism, soft, Art Deco, Magazine, Retro-Futuristic, Organic, and Neo-Corporate style packs. Use when defining the visual theme, typography pairings, border weights, and spacing tokens of a frontend.
version: "1.0.0"
verified_date: 2026-06-01
category: design
---

# Aesthetic Tones & Style Systems

## Purpose
Provide precise, copy-pasteable design engineering specifications, styling tokens, border-radius constraints, and typography pairings for eight highly distinct and premium visual style packs.

## When to Use This Skill
- Choosing and structuring the design system (CSS/Tailwind tokens) for a frontend project.
- Calibrating layout symmetry, border thickness, card geometry, and typography pairings.
- Building custom window frames, container mockups, or editorial presentation layouts.

## Output Format / Delivery
Produce highly cohesive, custom CSS styles or Tailwind configuration variables aligned strictly to one of the eight designated style packs. Always enforce the layout constraints and spacing ratios specified for the selected pack.

## Behavior Rules
1. **Never mix components from different style packs** — a single page or project must commit 100% to one cohesive aesthetic.
2. **Never hardcode hex values outside the selected pack's token definitions**.
3. **Always use rounded-full and soft drop-shadows only on Soft/Fluid styling** — never mix generous rounded corners with Brutalist design.
4. **Never allow default system styling to slip into production** — standard black-to-white gradients and placeholder emojis are strictly banned.

## Maintenance Notes
This skill is locked for style pack specifications. Update if additional premium packs or styling utilities are established.

---

## Phase 1: Style Pack - Premium Utilitarian Minimalism

Best suited for editorial portfolios, document-style landing pages, clean workspace products, and clean developer utilities.

### Color & Token Structure
* **Canvas / Page Background**: Pure White (`#FFFFFF`) or Warm Bone/Off-White (`#F7F6F3` or `#FBFBFA`).
* **Interactive Surfaces (Cards, Elements)**: Pure White (`#FFFFFF`) or Crisp Off-White (`#F9F9F8`).
* **Structural Borders & Dividers**: Crisp Light Gray (`#EAEAEA` or `rgba(0,0,0,0.06)`). Enforce exact `1px solid` boundaries.
* **Typography Base**: Charcoal Off-Black (`#111111` or `#2F3437`) with a generous line-height of `1.6` for legibility. Muted text: `#787774`.
* **Accent Pastels**: Exclusively use low-saturation, washed-out pastels for status tags, badging, and metadata backgrounds:
  * **Pale Red**: Background `#FDEBEC` (Text color: `#9F2F2D`)
  * **Pale Blue**: Background `#E1F3FE` (Text color: `#1F6C9F`)
  * **Pale Green**: Background `#EDF3EC` (Text color: `#346538`)
  * **Pale Yellow**: Background `#FBF3DB` (Text color: `#956400`)

### Layout Constraints
* **Borders**: Strictly keep border-radius tight, capping corners at `8px` or `12px` maximum.
* **Primary CTAs**: Solid carbon background (`#111111`) with white text. Tiny radius (`4px` to `6px`). No heavy drop shadows. Hover states must trigger a subtle opacity shift or scale reduction (`scale-[0.98]`).
* **Keyboard Micro-UIs**: Render keyboard shortcuts inside `<kbd>` elements styled with `border-1 border-[#EAEAEA]`, `bg-[#F7F6F3]`, and matching `font-mono`.
* **Dividers**: Accordions and lists must drop container card shapes, separating elements only with a `border-b border-[#EAEAEA]`.

---

## Phase 2: Style Pack - Brutalist / Raw

Best suited for developer tooling, high-impact agency landing pages, raw markdown blogs, and technical manifestos.

### Color & Token Structure
* **Canvas / Page Background**: Absolute White (`#FFFFFF`) or High-Contrast Stark Cream (`#FFFDF9`).
* **Surfaces & Layout Grids**: Plain flat cards with no background tints.
* **Structural Borders**: Thick, bold black lines (`border-2 border-black` or `border-[3px] border-black`).
* **Typography Base**: True Black (`#000000`). Monospace fonts (`font-mono`) are encouraged for both header display and body elements.

### Layout Constraints
* **Corners**: Hard zero-radius corners (`rounded-none`) across all cards, buttons, input fields, and UI cells.
* **Accent Colors**: Pure secondary primary tones (e.g. Saturated Neon Yellow `#FFFF00`, Neon Lime `#00FF00`, or Electric Cyan `#00FFFF`) used sparingly as background-block fills.
* **Interactive Shadows**: Zero drop shadow blur. Use hard offset shadows (`shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]`) that collapse on active state (`translate-x-[2px] translate-y-[2px] shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]`).

---

## Phase 3: Style Pack - Soft / Fluid (Liquid Glass)

Best suited for premium consumer apps, Apple-adjacent product releases, glassmorphism overlays, and elegant SaaS landing pages.

### Color & Token Structure
* **Canvas / Background**: Diffusion mesh gradients, layered radial lights, or subtle dark-mode space grids (`bg-zinc-950` with radial accents).
* **Surfaces (Liquid Glass)**: Layered glass cards (`bg-white/5` or `bg-black/40` with `backdrop-blur-md`).
* **Structural Borders**: 1px inner refraction edge (`border-white/10`) coupled with a subtle inner highlight overlay (`shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`).
* **Typography Base**: Soft Off-White (`#F8FAFC`) or Slate Gray (`#E2E8F0`).

### Layout Constraints
* **Corners & Curves**: Soft, generous curves (`rounded-2xl` or `rounded-3xl` for cards, `rounded-full` for badges/buttons).
* **Diffused Shadows**: Multi-layered, tinted drop shadows (`shadow-[0_8px_30px_rgb(0,0,0,0.12)]`).
* **Spring Physics**: Enforce Framer Motion default spring curves (`stiffness: 100, damping: 20`) for all entrance transitions.

---

## Phase 4: Faux OS Window Chrome Specification

When showcasing product screens or mockup dashboards inside landing pages or portfolios, wrap the layout in a clean mock window shell rather than a generic div:

```html
<div class="overflow-hidden border border-[#EAEAEA] rounded-lg bg-white shadow-sm">
  <!-- Window Header / macOS Controls -->
  <div class="flex items-center gap-1.5 px-4 py-3 bg-[#F7F6F3] border-b border-[#EAEAEA]">
    <div class="w-2.5 h-2.5 rounded-full bg-[#E4E4E4]"></div>
    <div class="w-2.5 h-2.5 rounded-full bg-[#E4E4E4]"></div>
    <div class="w-2.5 h-2.5 rounded-full bg-[#E4E4E4]"></div>
    <!-- Mock Title Bar (Optional) -->
    <span class="mx-auto text-[11px] font-mono text-[#A8A7A4] tracking-wide translate-x-[-12px]">preview.app</span>
  </div>
  <!-- Window Viewport -->
  <div class="p-6">
    <!-- Component UI goes here -->
  </div>
</div>
```

---

## Phase 5: Style Pack - Art Deco / Geometric Luxury

Best suited for premium fintech, luxury e-commerce, high-end hospitality, and awards ceremony sites.

### Color & Token Structure
* **Canvas / Background**: Rich dark navy (`#0A0E1A`) or champagne cream (`#F5F0E8`).
* **Surfaces**: Matte cards with subtle gold-tinted borders (`border-[#C9A96E]/20`).
* **Structural Borders**: Thin gold lines (`#C9A96E`) used sparingly — max 3 per section.
* **Typography Base**: High-contrast cream (`#F5F0E8`) on dark, or charcoal (`#1A1A2E`) on light. Display: condensed serif (e.g., `Playfair Display`, `Cormorant Garamond`). Body: geometric sans (`Outfit`, `Satoshi`).
* **Accent**: Warm gold (`#C9A96E`) for CTAs, highlights, and dividers.

### Layout Constraints
* **Corners**: Sharp zero-radius on cards and panels. Rounded-full on CTAs and badges only.
* **Decorative Lines**: Geometric dividers (thin horizontal rules with diamond/circle midpoints via SVG).
* **Symmetry**: Art Deco demands strict axial symmetry. Center-aligned hero sections allowed here (exception to the general Antigravity asymmetry rule).
* **Shadows**: No drop shadows. Use border-based separation exclusively.
* **Typography Scale**: Oversized display headings (`text-7xl md:text-8xl`) paired with small-caps tracking-wide body text.

---

## Phase 6: Style Pack - Magazine / Editorial

Best suited for media publications, long-form content sites, literary magazines, and journalism platforms.

### Color & Token Structure
* **Canvas / Background**: Warm paper-white (`#FDFBF7`) or deep ink (`#1A1A1A`).
* **Surfaces**: No card backgrounds. Content separated by whitespace and typographic hierarchy alone.
* **Structural Borders**: Hairline rules only (`border-b border-black/10` light mode, `border-white/10` dark mode).
* **Typography Base**: Serif for headlines and body (`Cormorant Garamond`, `Lora`, `Newsreader`). Sans-serif for UI chrome only. Generous line-height (`leading-[1.75]` for body, `leading-tight` for display).
* **Accent**: Single restrained hue — muted red (`#B44D4D`) for links and pull quotes.

### Layout Constraints
* **Multi-Column Text**: Use CSS `columns: 2` for body content on desktop. Single column on mobile.
* **Pull Quotes**: Large italic text inset with left border (`border-l-4 border-accent pl-6 italic text-2xl`).
* **Image Treatment**: Full-bleed images with caption underneath (`text-xs text-muted italic`). No rounded corners on editorial images.
* **Drop Caps**: First letter of lead paragraph: `first-letter:text-6xl first-letter:font-serif first-letter:float-left first-letter:mr-3 first-letter:mt-1`.
* **Whitespace**: Aggressive vertical spacing between sections (`py-24 md:py-32`). Content breathes.

---

## Phase 7: Style Pack - Retro-Futuristic / Synthwave

Best suited for gaming platforms, creative dev tools, music/audio apps, and experimental showcases.

### Color & Token Structure
* **Canvas / Background**: Deep space black (`#0D0221`) with radial gradient accents of neon purple (`#7B2FBE`).
* **Surfaces**: Dark glass cards (`bg-white/5 backdrop-blur-lg`) with neon border glow (`border-[#FF2D95]/30 shadow-[0_0_15px_rgba(255,45,149,0.15)]`).
* **Structural Borders**: Neon glow borders. Use `box-shadow` for glow effect, not thick borders.
* **Typography Base**: Off-white (`#E8E0F0`) for body. Display: monospace or geometric (`Space Grotesk`, `Orbitron`, `JetBrains Mono`).
* **Accent Palette**:
  * Neon Pink: `#FF2D95`
  * Electric Cyan: `#00F0FF`
  * Ultraviolet: `#7B2FBE`
  * Neon Yellow (sparingly): `#FFE500`

### Layout Constraints
* **Grid Lines**: Visible CSS grid lines as decorative elements (`border-white/5`).
* **Scanline Overlay**: Optional subtle scanline texture via CSS (`repeating-linear-gradient(0deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 3px)`).
* **CTA Buttons**: Neon-bordered with glow on hover. `border-[#FF2D95] shadow-[0_0_20px_rgba(255,45,149,0.4)]` on hover.
* **Interactions**: Aggressive hover effects. Scale `1.05` + glow expansion.

---

## Phase 8: Style Pack - Organic / Natural

Best suited for wellness brands, sustainability platforms, food/agriculture, and eco-conscious products.

### Color & Token Structure
* **Canvas / Background**: Warm linen (`#F4F0E6`) or soft sage-tinted white (`#F0F4F0`).
* **Surfaces**: Earth-toned cards (`bg-[#E8E0D4]` or `bg-[#DDE5D9]`) with no border — separated by spacing.
* **Structural Borders**: None. Use whitespace and background tint changes to separate sections.
* **Typography Base**: Warm dark brown (`#3D3024`) or deep forest green (`#1A3C2A`). Display: rounded friendly sans (`Nunito`, `Quicksand`) or organic serif (`Lora`). Body: clean sans with generous leading.
* **Accent**: Muted earth tones — terracotta (`#C67B5C`), sage green (`#7A9E7E`), or clay (`#B8860B`).

### Layout Constraints
* **Corners**: Generous radius everywhere (`rounded-2xl` cards, `rounded-full` buttons and avatars).
* **Shadows**: Warm-tinted soft shadows (`shadow-[0_4px_20px_rgba(60,40,20,0.08)]`).
* **Illustration Style**: Hand-drawn line art or watercolor textures. No sharp vector icons.
* **Photography**: Natural light, desaturated slightly, warm color grade.
* **Spacing**: Extra-generous padding (`p-8 md:p-12`). Content should feel unhurried.

---

## Phase 9: Style Pack - Neo-Corporate / Enterprise

Best suited for B2B SaaS, enterprise platforms, fintech dashboards, and compliance-heavy industries.

### Color & Token Structure
* **Canvas / Background**: Pure white (`#FFFFFF`) light mode, deep navy (`#0F172A`) dark mode.
* **Surfaces**: Clean white cards with subtle border (`border-zinc-200 dark:border-zinc-800`). Slight shadow (`shadow-sm`).
* **Structural Borders**: Precise 1px borders in neutral gray (`border-zinc-200`).
* **Typography Base**: Near-black (`#0F172A`) light mode, near-white (`#F1F5F9`) dark mode. Font: `Geist`, `Inter`, or `IBM Plex Sans`. Monospace for data: `Geist Mono` or `IBM Plex Mono`.
  * **Note**: `Inter` is permitted exclusively within this tone for dashboard/data-heavy contexts. This is an exception to the `ui-design-expert` typography ban.
* **Accent**: Conservative single accent — blue (`#2563EB`) or teal (`#0D9488`). No gradients on backgrounds.

### Layout Constraints
* **Corners**: Tight and consistent (`rounded-lg` everywhere — no mixing radii).
* **Density**: Higher information density than consumer products. Use 12px/14px body text where appropriate.
* **Tables**: Styled with alternating row backgrounds (`even:bg-zinc-50 dark:even:bg-zinc-900`). Column headers left-aligned for text, right-aligned for numbers.
* **CTAs**: Solid background, no glow, no gradient. `bg-primary text-white rounded-lg px-4 py-2 font-medium`.
* **Shadows**: Minimal. `shadow-sm` on cards, `shadow-md` on modals. No decorative shadows.
* **Data Display**: Monospace numbers. Right-align financial figures. Use `tabular-nums` for numeric columns.
