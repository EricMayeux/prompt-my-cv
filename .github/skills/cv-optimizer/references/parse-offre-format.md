# Parse-Offre JSON Format Reference

## Full JSON Structure

```json
{
  "source": "string — snake_case identifier derived from offer (e.g. scrum_master_28487)",
  "date_analyse": "YYYY-MM-DD",
  "poste": "Exact job title from the offer",
  "entreprise": "Company name if available",
  "top_keywords": [
    {
      "keyword": "Exact spelling from offer",
      "occurrences": 3,
      "priority": "High | Medium | Low",
      "variants": ["variant1", "variant2"]
    }
  ],
  "grouped_by_theme": {
    "Frameworks Agile": ["Scrum", "SAFe", "Kanban"],
    "Soft Skills": ["leadership", "communication"],
    "Outils & gouvernance": ["Jira", "Confluence"]
  },
  "competences_extracted": [
    "Exact competence phrase from offer — must appear verbatim in tailored CV"
  ],
  "suggestions_cv": [
    {
      "keyword": "keyword_name",
      "suggested_phrase": "Max 140 chars — actionable CV bullet suggestion"
    }
  ]
}
```

## Field Details

### top_keywords
- Extract 10–20 keywords from the job offer
- Count occurrences via case-insensitive literal match
- Priority assignment:
  - **High**: Appears 3+ times OR is in the job title OR is a mandatory requirement
  - **Medium**: Appears 2 times OR is in a "nice to have" section
  - **Low**: Appears once and is supplementary
- Merge variants under same entry (e.g., "Scrum" and "Scrum Master")

### competences_extracted  
- Soft skills, methodological competences, and technical competences
- Extracted as exact phrases from the offer text
- These MUST appear verbatim in the tailored CV — no paraphrasing

### suggestions_cv
- One suggestion per High-priority keyword
- Max 140 characters per suggestion
- Written as CV bullet format: starts with action verb (infinitive)
