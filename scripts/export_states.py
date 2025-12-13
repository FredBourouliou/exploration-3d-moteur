"""
Script Blender — Export des 3 états procéduraux du moteur
État A : Moteur complet
État B : Sans cache culbuteurs ni filtre à air
État C : Moteur ouvert (+ sans cache distribution)
"""

import bpy
import os

# ===========================================
# CONFIGURATION
# ===========================================

# Chemin de sortie
output_dir = os.path.dirname(bpy.data.filepath)
assets_dir = os.path.join(output_dir, "assets", "models")
os.makedirs(assets_dir, exist_ok=True)

# Mapping des noms descriptifs
RENAME_MAP = {
    "engine": "ensemble_moteur",
    "engine.001": "cache_culbuteurs",
    "engine.002": "arbre_a_cames",
    "engine.003": "collecteurs_echappement",
    "engine.004": "bloc_moteur",
    "engine.005": "filtre_a_air",
    "engine.006": "cables_allumage",
    "engine.007": "durites",
    "engine.008": "visserie",
    "engine.009": "residue_a_supprimer",
    "engine.010": "reservoir",
    "engine.011": "cache_distribution",
}

# Définition des états (pièces à MASQUER pour chaque état)
STATES = {
    "A": {
        "name": "engine_full",
        "description": "Moteur complet",
        "hide": []  # Rien de masqué
    },
    "B": {
        "name": "engine_no_cover",
        "description": "Sans cache culbuteurs",
        "hide": ["engine.001", "engine.005"]  # Cache culbuteurs + filtre à air
    },
    "C": {
        "name": "engine_open",
        "description": "Moteur ouvert",
        "hide": ["engine.001", "engine.005", "engine.011"]  # + cache distribution
    }
}

# ===========================================
# FONCTIONS
# ===========================================

def rename_objects():
    """Renomme les objets avec des noms descriptifs"""
    print("\n📝 RENOMMAGE DES OBJETS")
    print("-" * 40)

    for old_name, new_name in RENAME_MAP.items():
        if old_name in bpy.data.objects:
            obj = bpy.data.objects[old_name]
            obj.name = new_name
            print(f"  {old_name} → {new_name}")
        else:
            print(f"  ⚠️ {old_name} non trouvé")

def set_visibility(hide_list, hide=True):
    """Masque ou affiche les objets de la liste"""
    for old_name in hide_list:
        new_name = RENAME_MAP.get(old_name, old_name)
        if new_name in bpy.data.objects:
            obj = bpy.data.objects[new_name]
            obj.hide_set(hide)
            obj.hide_render = hide
            # Important pour l'export GLB
            obj.hide_viewport = hide

def export_glb(filename, description):
    """Exporte la scène visible en GLB"""
    filepath = os.path.join(assets_dir, filename)

    # Supprimer le résidu avant export
    if "residue_a_supprimer" in bpy.data.objects:
        bpy.data.objects["residue_a_supprimer"].hide_set(True)
        bpy.data.objects["residue_a_supprimer"].hide_viewport = True

    # Masquer aussi le Plane (sol) s'il existe
    if "Plane" in bpy.data.objects:
        bpy.data.objects["Plane"].hide_set(True)
        bpy.data.objects["Plane"].hide_viewport = True

    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_format='GLB',
        use_visible=True,  # Exporter uniquement les objets visibles
        use_selection=False,
        export_apply=True,
        export_texcoords=True,
        export_normals=True,
        export_materials='EXPORT'
    )

    print(f"  ✅ {filename} ({description})")

def reset_visibility():
    """Remet tous les objets visibles"""
    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_render = False
        obj.hide_viewport = False

# ===========================================
# EXÉCUTION
# ===========================================

print("\n" + "=" * 60)
print("EXPORT DES ÉTATS PROCÉDURAUX")
print("=" * 60)

# Étape 1 : Renommer les objets
rename_objects()

# Étape 2 : Exporter chaque état
print("\n📦 EXPORT DES GLB")
print("-" * 40)

for state_id, state_config in STATES.items():
    # Réinitialiser la visibilité
    reset_visibility()

    # Masquer les pièces pour cet état
    set_visibility(state_config["hide"], hide=True)

    # Exporter
    export_glb(
        f"{state_config['name']}.glb",
        state_config['description']
    )

# Réinitialiser pour terminer
reset_visibility()

print("\n" + "=" * 60)
print("EXPORT TERMINÉ")
print(f"Fichiers dans : {assets_dir}")
print("=" * 60)
