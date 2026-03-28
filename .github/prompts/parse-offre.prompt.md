---
mode: agent
tools:
  - create_file
  - read_file
description: >
  Extrait les 10–20 mots-clés les plus pertinents d'une offre d'emploi,
  compte leurs occurrences, les regroupe par thématique et génère un JSON
  structuré pour alimenter le prompt optimize-cv-from-json.
---

# Parsing d'Offre d'Emploi — Extraction de Mots-Clés ATS

## Rôle

Expert en recrutement IT et parsing d'offres d'emploi en français.
Ta mission est d'extraire, compter et structurer les mots-clés d'une offre
pour optimiser un CV via les systèmes ATS.

## Entrée

- `${job_file}` : fichier texte contenant l'intégralité de l'offre d'emploi

## Consignes

1. Retourner du JSON uniquement (aucun commentaire dans le fichier de sortie).
2. Inclure entre 10 et 20 mots/expressions, en préservant l'orthographe exacte de l'offre (casse, accents, pluriel).
3. Comptage exact d'occurrences (match littéral, insensible à la casse).
4. Regrouper par thématiques pertinentes au domaine du poste (ex. Frameworks Agile, Outils & gouvernance, Soft skills, etc.).
5. Attribuer une priorité (High, Medium, Low) selon fréquence et importance pour le rôle.
6. Regrouper les variantes sous le même item et sommer les occurrences (ex. "Scrum" + "scrum master").
7. Pour chaque mot-clé High, proposer 1 phrase CV courte (max 140 caractères) intégrant naturellement le mot-clé.
8. Extraire les compétences (soft skills, méthodologiques, techniques) mentionnées ou implicites dans l'offre dans le champ `competences_extracted`.

## Format JSON attendu

```json
{
  "source": "<titre_offre_ou_identifiant>",
  "top_keywords": [
    {
      "keyword": "Scrum",
      "occurrences": 3,
      "category": "Frameworks Agile",
      "priority": "High"
    }
  ],
  "grouped_by_theme": {
    "Frameworks Agile": ["Scrum", "SAFe"],
    "Planification & Backlog": ["priorisation", "raffinement"]
  },
  "competences_extracted": [
    "Communication",
    "Amélioration continue",
    "Résolution de problèmes"
  ],
  "suggestions_cv": [
    {
      "keyword": "Scrum",
      "suggestion": "Facilite cérémonies Scrum et PI planning pour accélérer livraison et améliorer qualité."
    }
  ]
}
```

## Sortie

1. **Fichier JSON** : Créer `offres/analyse/${job_file}.json` avec la structure ci-dessus.
2. **Recommandations dans le chat** : Après la création du fichier, fournir un résumé concis :
   - **À prioriser côté CV** : top 5 mots-clés à intégrer absolument
   - **Pour les ATS** : conseils de placement stratégique
   - **Phrases optimisées** : 2–3 exemples de reformulation
   - **À éviter** : pièges courants pour cette offre
   - **Conseil final** : orientation générale pour l'optimisation
