---
name: cv-optimizer
description: >
  **WORKFLOW SKILL** — End-to-end ATS-optimized CV and motivation letter generation from a job offer.
  USE FOR: tailoring a LaTeX CV to a specific job posting; generating a personalized motivation letter;
  extracting keywords from job offers; ATS optimization; career document generation.
  PRODUCES: (1) JSON keyword analysis, (2) tailored .tex CV, (3) motivation letter .tex file.
  INPUTS: a job offer text file and the original cv.tex.
  DO NOT USE FOR: creating a CV from scratch; general LaTeX editing; non-job-related documents.
argument-hint: 'Path to the job offer text file (e.g., offres/scrum_master_28487)'
---

# CV Optimizer — ATS-Tailored CV & Motivation Letter

Generate an ATS-optimized CV (.tex) and a personalized motivation letter from a job offer,
using the candidate's original CV as source of truth.

## When to Use

- You have a job offer (text file) and want to tailor your CV for it
- You want to generate a motivation letter aligned with a specific posting
- You need to maximize ATS (Applicant Tracking System) keyword matching
- You want the full pipeline: parse offer → optimize CV → generate letter

## Required Inputs

| Input | Description |
|-------|-------------|
| **Job offer file** | Text file containing the full job posting (in `offres/` folder) |
| **Original CV** | `cv.tex` — the candidate's master CV in LaTeX |

## Workflow — 3 Phases

### Phase 1: Parse Job Offer → JSON Analysis

**Goal**: Extract keywords, competences, and themes from the job offer.

1. Read the job offer file provided by the user
2. Extract 10–20 keywords preserving exact spelling from the offer (case, accents, plurals)
3. Count exact occurrences (case-insensitive literal match)
4. Group keywords by theme (e.g., Frameworks Agile, Soft Skills, Outils & gouvernance)
5. Assign priority: High / Medium / Low based on frequency and role importance
6. Merge keyword variants under same item (e.g., "Scrum" + "scrum master")
7. Extract `competences_extracted` (soft skills, methodological, technical)
8. For each High keyword, generate 1 CV phrase suggestion (max 140 chars)
9. Create JSON file: `offres/analyse/{offer_name}.json`

**JSON structure**: See [parse-offre reference](./references/parse-offre-format.md)

**Output to user**: Brief recommendations (top 5 keywords, ATS tips, pitfalls to avoid)

### Phase 2: Optimize CV → Tailored .tex

**Goal**: Adapt the original CV to maximize ATS match for this specific offer.

1. Read the JSON analysis from Phase 1
2. Read the original `cv.tex`
3. Score keywords: `score = occurrences × priority_weight` (High=3, Medium=2, Low=1)
4. Classify: `must_insert` (score ≥ 6, max 8) and `nice_to_have` (next by score, max 10)
5. Apply keyword integration following the **ATS hierarchy**:
   - Title: 1-2 major keywords
   - Professional profile: 3-4 `must_insert` keywords
   - Skills section: organize by `grouped_by_theme`
   - Experience: enrich 1-2 bullets per position
6. Disseminate `competences_extracted` contextually (never as isolated lists):
   - Profile: 20-30% | Value Proposition: 15-20% | Skills: 30-40% | Experience: 30-40%
   - Techniques: enrichment, expansion, business context addition
7. Preserve EXACT spelling of offer terms (case, accents, hyphens, plural)
8. Create file: `{source}_tailored.tex`

**Strict rules**:
- NEVER invent experiences, dates, companies, or metrics
- NEVER modify existing job titles
- ONLY reformulate existing content
- Mark unverifiable data as `[À VÉRIFIER]`
- Style: RH telegraphic — each bullet starts with action verb (infinitive), no pronouns

**Quality targets**:
- CV ≤ 2 pages
- Page 1 must contain: header + professional profile + key skills
- Keyword density: 2-3%
- 100% of `competences_extracted` must appear (exact spelling)

**Output to user**: JSON summary with changelog and validation checklist

### Phase 3: Generate Motivation Letter → .tex

**Goal**: Produce a personalized, ATS-aligned motivation letter.

1. Read the job offer, the tailored CV from Phase 2, and the JSON analysis
2. Generate a 380–450 word letter in plain text with 4–5 paragraphs:
   - **P1 (Hook)**: Position mention, company, key differentiator
   - **P2 (Current role alignment)**: Current role from CV, 1-2 quantified achievements
   - **P3 (Career depth)**: Past relevant experience, progression, value alignment
   - **P4 (Human dimension)**: Soft skills, culture fit, 2 suggestions from analysis
   - **P5 (Conclusion)**: Value synthesis, availability, polite closing
3. Integrate each High keyword at least once (max 3 repetitions for core terms)
4. Extract 3-5 quantified achievements from CV
5. Create file: `lm_{role_title}_{post_id}.tex` with LaTeX formatting

**Style rules**:
- Action verbs: Faciliter, Coordonner, Piloter, Optimiser, Déployer
- Prefer: "J'apporte", "Je mets en place", "Je structure"
- Avoid: "Je suis passionné", clichés, unproven claims
- Max ~28 words per sentence, no bullet lists, no markdown

**Output to user**: Plain text letter in chat + .tex file created

## Quality Checklist (Applied After Each Phase)

### Phase 1
- [ ] JSON created in `offres/analyse/`
- [ ] 10-20 keywords extracted with exact spelling
- [ ] `competences_extracted` array populated
- [ ] `suggestions_cv` provided for High keywords

### Phase 2
- [ ] File `{source}_tailored.tex` created
- [ ] Ends with `\end{document}`
- [ ] All `must_insert` keywords present
- [ ] 100% of `competences_extracted` included (exact spelling)
- [ ] Balanced distribution across CV sections
- [ ] Valid, compilable LaTeX
- [ ] ≤ 2 pages target

### Phase 3
- [ ] 380-450 words
- [ ] All High keywords used at least once
- [ ] 1-3 quantified achievements included
- [ ] Final paragraph calls for interview
- [ ] No bullet lists in output
- [ ] .tex file created with correct name

## File Naming Conventions

| Output | Pattern | Example |
|--------|---------|---------|
| JSON analysis | `offres/analyse/{offer_id}.json` | `offres/analyse/scrum_master_28487.json` |
| Tailored CV | `{source}_tailored.tex` | `scrum_master_28487_tailored.tex` |
| Motivation letter | `lm_{role}_{post_id}.tex` | `lm_scrum_master_28487.tex` |

## LaTeX Standards

- Font: Times New Roman (`mathptmx`)
- Margins: 0.7in (`geometry`)
- Compact spacing: `noitemsep`, `topsep=2pt`
- Encoding: UTF-8 (`inputenc`)
- Sections: `\section*{}` (unnumbered)
- ATS highlighting: `\highlight{}` or `\textbf{}`

## Authenticity — Non-Negotiable

- Source CV (`cv.tex`) is the **single source of truth**
- Every fact in the tailored CV must trace back to `cv.tex`
- Every achievement in the letter must trace back to `cv.tex`
- No fabricated metrics, dates, companies, or experiences
- Language is French
