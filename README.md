# CV Eric MAYEUX - LaTeX Version

Ce projet contient votre CV en format LaTeX, permettant une génération professionnelle en PDF optimisée pour les systèmes ATS (Applicant Tracking Systems).

## Structure du projet

- `cv.tex` - Votre CV en LaTeX (source principale)
- `build_cv.py` - Script Python pour compiler le CV
- `extract_cv.py` - Script pour extraire le texte du PDF original
- `cv-old/` - Dossier contenant votre CV PDF original

## Option 1 : Compilation locale (Recommandé)

### Prérequis
1. **Installer MiKTeX** (distribution LaTeX pour Windows)
   - Télécharger depuis : https://miktex.org/download
   - Installer avec l'option "Install missing packages on-the-fly: Yes"
   - Redémarrer votre terminal après l'installation

### Compilation

**Méthode 1 : Avec Python**
```powershell
python build_cv.py
```

**Méthode 2 : Directement avec pdflatex**
```powershell
pdflatex cv.tex
pdflatex cv.tex  # Deuxième fois pour les références
```

Le PDF sera généré : `cv.pdf`

## Option 2 : Compilation en ligne (Sans installation)

### Utiliser Overleaf
1. Aller sur https://overleaf.com
2. Créer un compte gratuit
3. Créer un nouveau projet → "Upload Project"
4. Uploader votre fichier `cv.tex`
5. Cliquer sur "Recompile"
6. Télécharger le PDF généré

## Modifier votre CV

### Sections principales dans cv.tex :

1. **En-tête** : Nom, titre, coordonnées
2. **Résumé professionnel** : Votre pitch
3. **Compétences Clés** : Technologies et soft skills
4. **Réalisations** : Vos succès majeurs
5. **Expérience Professionnelle** : Vos postes avec détails
6. **Formations** : Vos certifications et formations
7. **Formation Académique** : Vos diplômes
8. **Langues** : Français, Anglais

### Conseils pour les modifications :

- **Ajouter une nouvelle expérience** :
```latex
\subsection*{Titre du poste} \hfill \textit{Date début - Date fin}\\
\textit{Entreprise (Ville)}\\
Description brève
\begin{itemize}
    \item Réalisation 1
    \item Réalisation 2
\end{itemize}
```

- **Modifier le texte** : Simplement éditer le texte entre les accolades `{...}`
- **Ajouter des items** : Ajouter une ligne `\item Nouveau point` dans une liste

## Optimisation ATS

Votre CV est déjà optimisé pour les ATS :
✓ Structure claire avec sections standards
✓ Pas de tableaux complexes ou images
✓ Police simple et lisible
✓ Mots-clés techniques bien placés
✓ Format chronologique inversé
✓ Pas de caractères spéciaux problématiques

## Personnalisation

### Changer les marges :
```latex
\usepackage[margin=0.75in]{geometry}  % Changer 0.75in
```

### Changer la police :
Ajouter après `\usepackage[T1]{fontenc}` :
```latex
\usepackage{helvet}  % Pour Helvetica
\renewcommand{\familydefault}{\sfdefault}
```

## Support

Si vous rencontrez des erreurs :
1. Vérifier que MiKTeX est bien installé : `pdflatex --version`
2. Consulter le fichier `cv.log` pour les détails des erreurs
3. Les erreurs courantes :
   - "Package not found" → MiKTeX téléchargera automatiquement si configuré correctement
   - "Undefined control sequence" → Vérifier la syntaxe LaTeX

## Versions

- **2025-DirQ** : Version actuelle (Directeur Assurance Qualité)
- Source originale : `cv-old/CV Eric MAYEUX 2025 DirQ.pdf`

---

**Créé le** : Octobre 2025
**Format** : LaTeX → PDF
**Optimisé** : ATS-friendly
