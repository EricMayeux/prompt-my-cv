# Instructions Copilot — Projet CV LaTeX (prompt-my-cv)

## Contexte du projet

Ce projet gère la génération et l'optimisation de CV professionnels en LaTeX, ciblés pour les systèmes ATS (Applicant Tracking Systems). Le workflow repose sur 3 prompts chaînés :

1. **parse-offre** : Extraire les mots-clés d'une offre d'emploi → JSON d'analyse
2. **optimize-cv-from-json** : Adapter le CV LaTeX source aux mots-clés extraits → CV `.tex` optimisé
3. **lm** : Générer une lettre de motivation personnalisée à partir de l'offre, du CV et de l'analyse

## Structure du projet

```
prompt-my-cv/
├── .github/
│   ├── copilot-instructions.md    # Ce fichier
│   └── prompts/                   # Prompts Copilot réutilisables
│       ├── parse-offre.prompt.md
│       ├── optimize-cv-from-json.prompt.md
│       └── lm.prompt.md
├── aide_md/                       # Documentation d'analyse et de méthodologie
├── cv.tex                         # CV source principal (LaTeX)
├── cv_optimized.tex               # Version optimisée générique
├── *_tailored.tex                 # CV adaptés à des offres spécifiques
├── offres/                        # Offres d'emploi brutes (texte)
│   └── analyse/                   # JSON d'analyse générés par parse-offre
├── cv-final/                      # PDF finaux générés
├── cv-old/                        # Anciennes versions archivées
├── build_cv.py                    # Script de compilation LaTeX → PDF
└── README.md
```

## Conventions de nommage

### Fichiers CV générés
- Format : `{identifiant_offre}_tailored.tex`
- L'identifiant provient du champ `source` du JSON d'analyse (snake_case)
- Exemples : `scrum_master_28487_tailored.tex`, `Directeur_principal_GCE_tailored.tex`

### Fichiers d'analyse JSON
- Format : `{identifiant_offre}.json`
- Emplacement : `offres/analyse/`

### Lettres de motivation
- Format : `lm_{poste_cible}_{numero_offre}.tex`

## Standards LaTeX

- Police : Times New Roman (package `mathptmx` ou `times`)
- Marges : 0.7in (package `geometry`)
- Espacement compact : `noitemsep`, `topsep=2pt`
- Encodage : UTF-8 (`inputenc`)
- Sections : `\section*{}` (sans numérotation)
- Listes : `\begin{itemize}` avec `\item` débutant par un verbe d'action à l'infinitif
- Mise en évidence ATS : macro `\highlight{}` ou `\textbf{}` pour les mots-clés

## Règles de génération de contenu

### Authenticité (CRITIQUE)
- Ne JAMAIS inventer d'expériences, dates, entreprises ou métriques
- Ne JAMAIS modifier les intitulés de poste existants
- Seules les reformulations de contenu existant sont autorisées
- Toute donnée non vérifiable doit être marquée `[À VÉRIFIER]`

### Style rédactionnel
- Style RH télégraphique : chaque puce débute par un verbe d'action (infinitif) sans pronom
- Verbes privilégiés : Piloter, Faciliter, Implémenter, Coordonner, Optimiser, Déployer
- Pas de phrases creuses ni de clichés ("passionné", "candidat idéal", "team player dynamique")
- Maximum ~28 mots par phrase dans les lettres de motivation

### Optimisation ATS
- Densité mots-clés : 2-3% du contenu total
- Placement stratégique : début de sections, premiers bullets
- Préserver l'orthographe exacte des compétences de l'offre (casse, accents, pluriel)
- Enrichir par reformulation contextuelle, jamais par liste brute isolée

## Workflow des variables entre prompts

### parse-offre → optimize-cv-from-json
| Variable parse-offre (sortie) | Variable optimize (entrée) |
|-------------------------------|----------------------------|
| Fichier JSON généré           | `${job_analysis}`          |
| —                             | `${original_cv}` (cv.tex)  |

### parse-offre + optimize → lm
| Variable (source)  | Variable lm (entrée) |
|--------------------|----------------------|
| Offre brute        | `${offre}`           |
| CV tailored .tex   | `${cv}`              |
| JSON d'analyse     | `${analyse}`         |

## Sécurité et confidentialité

- Ne jamais inclure d'informations personnelles sensibles (NAS, numéro de permis, etc.) dans le CV
- Les coordonnées (email, téléphone) sont les seules données personnelles autorisées
- Ne pas stocker de mots de passe ou tokens dans le repo
- Les fichiers PDF finaux contenant des données personnelles ne doivent pas être commit (ajouter au .gitignore)

## Compilation

```powershell
# Compiler un CV spécifique
python build_cv.py                    # Compile cv.tex par défaut
pdflatex nom_fichier_tailored.tex     # Compile un CV spécifique
pdflatex nom_fichier_tailored.tex     # 2e passe pour références
```

## Contraintes techniques

- Privilégier la création de fichiers en blocs incrémentiels pour les fichiers LaTeX longs (200+ lignes)
- Le CV optimisé doit tenir sur 2 pages maximum (cible pour < 15 ans d'expérience)
- La Page 1 doit contenir : header, profil professionnel et compétences clés
- Format PDF final : texte extractible (pas de scan/image), pas de tableaux complexes
