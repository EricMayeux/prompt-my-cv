---
mode: agent
tools:
  - create_file
  - read_file
description: >
  Génère une lettre de motivation professionnelle en texte brut et fichier LaTeX,
  personnalisée pour le poste cible en utilisant l'offre, le CV et les mots-clés extraits.
---

# Génération de Lettre de Motivation

## Objectif

Produire une lettre de motivation professionnelle, personnalisée, convaincante et concise
(≈ 380–450 mots) pour le poste cible, basée sur :
- Le texte intégral de l'offre : `${offre}`
- Le contenu du CV LaTeX : `${cv}`
- Les mots-clés extraits (JSON analyse) : `${analyse}`

## Variables d'entrée

| Variable | Description | Défaut |
|----------|-------------|---------|
| `${offre}` | Contenu brut de l'offre (responsabilités, prérequis, culture) | — |
| `${cv}` | Contenu du CV LaTeX (expérience, réalisations, compétences) | — |
| `${analyse}` | JSON structuré (top_keywords, grouped_by_theme, suggestions_cv) | — |
| `${candidate_name}` | Nom du candidat | ERIC MAYEUX |
| `${target_role_title}` | Titre du poste cible | — |
| `${job_post_id}` | Numéro de l'offre | — |
| `${today_date}` | Date format long (ex: 28 octobre 2025) | date du jour |
| `${recruiter_or_manager_name}` | Nom du recruteur/gestionnaire | Madame, Monsieur |
| `${location}` | Localisation (omettre si non spécifié) | — |
| `${company_name}` | Nom de l'entreprise (omettre si non spécifié) | — |

## Contraintes de sortie

- Format : TEXTE BRUT UNIQUEMENT (pas de Markdown, pas de listes à puces, pas de caractères décoratifs)
- Style : professionnel, énergique, authentique, centré sur la valeur livrée
- Ton : assuré mais humble, orienté résultats + collaboration + amélioration continue
- Intégrer naturellement les mots-clés High de `${analyse}` sans sur-optimisation
- Zéro jargon inutile, max ~28 mots par phrase
- Pas de redondance entre paragraphes
- 4 à 5 paragraphes distincts séparés par une ligne blanche
- Aucune donnée factuelle non présente dans le CV ou l'offre

## Structure attendue

**Paragraphe 1 (Accroche ciblée) :**
- Mention du poste, du numéro, de l'entreprise
- Alignement immédiat sur la mission clé de l'offre
- Positionner un différenciateur personnel

**Paragraphe 2 (Alignement rôle / expérience actuelle) :**
- Rôle actuel tiré du CV
- Mettre en avant les réalisations alignées avec l'offre
- 1 à 2 réalisations chiffrées

**Paragraphe 3 (Historique pertinent / profondeur) :**
- Sélectionner les expériences passées qui renforcent le profil
- Montrer la continuité et la progression de carrière
- Relier à la valeur recherchée dans l'offre

**Paragraphe 4 (Dimension humaine / culture / soft skills) :**
- Collaboration, écoute, communication, résilience
- Intégrer 2 suggestions issues de `${analyse}.suggestions_cv`
- Montrer la posture : servant leader, coaching, sécurité psychologique

**Paragraphe 5 (Conclusion) :**
- Synthèse de la valeur apportée
- Disponibilité pour entretien
- Formule polie finale

## Intégration des mots-clés

- Utiliser chaque mot-clé High au moins une fois, sans en abuser
- Ne pas répéter un mot-clé plus de 2 fois (sauf termes clés du poste, max 3)
- Outils spécifiques (Jira, Confluence, etc.) : 1 mention naturelle dans le contexte

## Réalisations à intégrer

Extraire du CV les réalisations chiffrées les plus pertinentes pour le poste cible.
Sélectionner 3–5 réalisations qui démontrent l'adéquation avec l'offre.

## Style rédactionnel

- Verbes d'action : Faciliter, Coordonner, Piloter, Optimiser, Déployer, Aligner, Encadrer, Accélérer
- Préférer : "J'apporte", "Je mets en place", "Je structure", "Je crée les conditions de"
- Éviter : "Je suis passionné", "Je pense que", "candidat idéal", "team player dynamique"

## Interdits

- Pas de copier-coller brut d'un bloc du CV
- Pas de surenchère non prouvée (ne pas inventer des gains)
- Pas de clichés
- Pas de fautes d'accord

## Sorties

2 sorties distinctes :

1. **Sortie chat** : Texte de la lettre (plain text), sans balises, sans méta, sans JSON
2. **Fichier** : Créer `lm_${target_role_title}_${job_post_id}.tex` avec mise en forme LaTeX et mots importants en gras

## Contrôle qualité (checklist interne)

1. Tous les mots-clés High présents au moins une fois
2. Longueur respectée (380–450 mots)
3. 1–3 chiffres concrets intégrés
4. Paragraphe final appelle à entretien
5. Aucune liste à puces
6. Pas de répétition abusive d'un même mot (≤3 occurrences)
7. Ton professionnel et fluide
8. Cohérence chronologique
9. Aucune exagération non supportée
10. Vérifier la création du fichier et la réponse dans le chat
