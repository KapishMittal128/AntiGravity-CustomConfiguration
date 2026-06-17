# PROJECT STATE & ARCHITECTURE (Context Scaffold)

> **CORE DIRECTIVE:** This file is the absolute source of truth for the project. It persists across sessions. 
> Whenever an agent is invoked, they must read this file to understand the environment, the stack, and the constraints.
> **DO NOT** use this as a task list (use `task.md` for that). **DO** update this when architectural decisions are made.

---

## 1. SYSTEM ARCHITECTURE
* **Frontend:** [e.g., Next.js 14 App Router, React, TailwindCSS]
* **Backend:** [e.g., Node.js, Express, Prisma]
* **Database:** [e.g., PostgreSQL via Supabase]
* **Deployment:** [e.g., Vercel, Railway]

## 2. DESIGN SYSTEM
* **Color Palette:** 
  * Primary: `#000000`
  * Secondary: `#FFFFFF`
  * Accent: `[TBD]`
* **Typography:** 
  * Headings: `Inter`
  * Body: `Inter`
* **Spacing/Radius:** [e.g., 8px grid, fully rounded buttons]
* **Vibe/Keywords:** [e.g., Minimal, Brutalist, Premium SaaS]

## 3. ARCHITECTURAL DECISIONS (ADRs)
*(Log major technical decisions here so future agents do not question them)*
* **[Date] - Decision:** [Brief explanation of why a tech choice was made]

## 4. KNOWN CONSTRAINTS & GOTCHAS
*(Log weird project quirks, specific library versions, or things that break often)*
* [Constraint 1]

## 5. CURRENT MACRO-PHASE
* [ ] **Planning** (Defining the architecture)
* [ ] **Building** (Active development)
* [ ] **Auditing** (Review, QA, Polish)
* [ ] **Shipping** (Deployment readiness)
