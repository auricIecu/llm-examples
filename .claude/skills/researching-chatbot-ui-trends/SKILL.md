---
name: researching-chatbot-ui-trends
description: Researches the latest chatbot and conversational UI design trends across the web and produces a structured Spanish-language report with concrete examples and source citations. Use when the user asks about chatbot interface design, conversational UI patterns, modernizing a chat UI, "tendencias de diseño en chatbots", or wants design inspiration for an AI assistant interface.
allowed-tools: WebSearch, WebFetch
---

# Researching Chatbot UI Trends

## Overview

Performs a focused web research pass on current chatbot / conversational UI design trends, synthesizes findings from multiple substantive sources, and returns a Spanish-language report with actionable patterns and real citations.

The output language is **Spanish** because the primary user of this skill works in Spanish. Source articles are usually in English — translate the synthesis, do not just copy excerpts.

## When to Use

- "¿cuáles son las tendencias de diseño en chatbots?"
- "what's trending in chatbot / conversational UI?"
- "¿cómo modernizo la interfaz de mi chatbot?"
- The user is iterating on a chat UI and wants outside design inspiration

## Workflow

Copy this checklist into your response and tick items as you progress:

```
- [ ] Step 1: Run 3 targeted web searches (current year, then prior if sparse)
- [ ] Step 2: Pick 3–5 substantive sources and fetch them
- [ ] Step 3: Extract 5–7 distinct trends with concrete details
- [ ] Step 4: Write the Spanish report following the template
```

### Step 1 — Search

Use `WebSearch` with three angles. Adjust the year to the current one shown in the conversation context (do NOT hard-code a year here — read it from the system context):

1. `chatbot UI design trends <current_year>`
2. `conversational UI patterns OR AI assistant interface design`
3. `chatbot UX best practices site:nngroup.com OR site:smashingmagazine.com OR site:uxdesign.cc OR site:medium.com`

If the current-year searches return mostly listicles or thin content, repeat with `<current_year - 1>` and mark those sources as slightly older in the report.

### Step 2 — Fetch

Pick 3–5 sources that look most substantive (design publications, UX research firms, recognized agencies, primary sources from companies known for AI UX). Use `WebFetch` with a prompt like:

> "Extract the concrete chatbot / conversational UI design trends, patterns, and visual examples discussed in this article. List each as: trend name, what it is, why it matters, and any product example mentioned."

Skip clickbait listicles, SEO farms, and content with no concrete patterns.

### Step 3 — Extract

For each trend, capture:

- **Name** — one line
- **What it is** — 2–3 lines, concrete (visual/interaction detail, not vague adjectives)
- **Why it matters** — what user problem or goal it solves
- **Example** — product, app, or screenshot reference if the source provided one
- **Confidence** — `alta` if multiple sources mention it, `emergente` if only one

Aim for **5–7 distinct trends**, not 20 superficial ones. Merge duplicates across sources.

### Step 4 — Report (template)

```markdown
# Tendencias de diseño UI para chatbots — <mes> <año>

## Resumen ejecutivo
<2–3 oraciones con los hilos comunes entre las fuentes>

## Tendencias clave

### 1. <Nombre de la tendencia>
- **Qué es:** ...
- **Por qué importa:** ...
- **Ejemplo:** ...
- **Confianza:** alta | emergente

### 2. ...
(repetir para 5–7 tendencias)

## Ideas para este proyecto
<Solo si en la conversación hay un proyecto chatbot visible. 3–5 sugerencias accionables conectadas a las tendencias listadas, citando archivos del repo si aplica.>

## Fuentes
1. [<Título del artículo>](<URL>) — <publicación>, <fecha si visible>
2. ...
```

## Quality Rules

- **Citations must be real.** Never invent URLs or paraphrase from memory — every claim ties to a source you actually fetched in this run.
- **Date the report.** Use the date from the conversation context, not a guess.
- **Mark older references.** If a key source predates the current year, append `(referencia anterior)` to its trend.
- **No filler.** If a "trend" boils down to "use AI" or "be conversational", drop it — it's not a UI trend.
- **Tie back when possible.** If the conversation contains an active chatbot project, the "Ideas para este proyecto" section is required and must reference real files from the repo.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Citing 2022–2023 articles as current | Re-search with the current year; mark older as `(referencia anterior)` |
| 15 vague trends, all sounding the same | Merge duplicates, target 5–7 with concrete detail |
| Pretending a single blog post = consensus | Mark single-source trends as `emergente` |
| Writing the report in English | Translate to Spanish; sources stay in original language in the citation |
| Skipping the "Ideas para este proyecto" section when relevant | If a chatbot repo is open in the conversation, that section is required |
