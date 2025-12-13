# Exploration 3D Pédagogique — Moteur (GLB + model-viewer)

Outil d'exploration 3D pédagogique permettant l'inspection interactive de composants mécaniques en vue d'une préparation procédurale avant manipulation réelle.

## Objectif

Permettre aux apprenants de :
- Inspecter librement un moteur et ses sous-ensembles
- Isoler des pièces ou groupes de pièces
- Comprendre la structure et l'ordre procédural
- Se préparer cognitivement avant manipulation en atelier

> **Note :** Cet outil est un dispositif de visualisation interactive, pas une simulation gestuelle ou mécanique.

## Fonctionnalités

- Affichage de modèles 3D (format GLB)
- Rotation libre (souris / tactile / contrôleurs VR)
- Zoom / dézoom
- Recentrage de la vue
- Isolation de sous-ensembles
- Vue éclatée
- Hotspots cliquables avec informations techniques

## Stack technique

| Composant | Technologie |
|-----------|-------------|
| Viewer 3D | `<model-viewer>` (Web Component) |
| Format 3D | GLB (Blender / photogrammétrie) |
| Interface | HTML / CSS / JavaScript |

## Plateformes cibles

- Desktop (navigateur web)
- Mobile (navigateur web)
- Meta Quest (navigateur VR)

## Structure du projet

```
/
├── README.md           # Ce fichier
├── claude.md           # Spécifications du projet
├── index.html          # Page principale
├── assets/
│   ├── models/         # Fichiers GLB
│   ├── images/         # Images et icônes
│   └── styles/         # Feuilles de style CSS
├── js/                 # Scripts JavaScript
└── blender/            # Fichiers sources Blender
```

## Installation

1. Cloner le dépôt
2. Servir les fichiers via un serveur HTTP local

```bash
# Avec Python
python -m http.server 8000

# Avec Node.js (npx)
npx serve
```

3. Ouvrir `http://localhost:8000` dans le navigateur

## Modèles 3D

### Organisation recommandée (Multi-GLB)

Chaque état du moteur correspond à un fichier GLB distinct :
- `engine_full.glb` — Moteur complet
- `engine_no_cover.glb` — Sans capot
- `engine_no_belt.glb` — Sans courroie
- etc.

### Contraintes sur les GLB

- Échelle cohérente entre les fichiers
- Orientation stable
- Groupes fonctionnels nommés clairement
- Optimisation du poids (compression, LOD si nécessaire)

## Compatibilité VR

L'application fonctionne en mode VR immersif via le navigateur Meta Quest.
Les contrôleurs permettent la rotation et le zoom du modèle.

## Public cible

Formation professionnelle : maintenance, technique, véhicules électriques.

## Licence

À définir.

---

*Projet développé dans un cadre de formation professionnelle.*
