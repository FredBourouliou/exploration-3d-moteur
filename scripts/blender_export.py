"""
Script Blender pour :
1. Lister les objets et collections du fichier
2. Exporter le modèle complet en GLB
"""

import bpy
import os

# Chemin de sortie
output_dir = os.path.dirname(bpy.data.filepath)
assets_dir = os.path.join(output_dir, "assets", "models")

# Créer le dossier si nécessaire
os.makedirs(assets_dir, exist_ok=True)

print("\n" + "="*60)
print("ANALYSE DU FICHIER BLENDER")
print("="*60)

# Lister les collections
print("\n📁 COLLECTIONS:")
print("-" * 40)

def list_collections(collection, indent=0):
    prefix = "  " * indent
    obj_count = len(collection.objects)
    print(f"{prefix}• {collection.name} ({obj_count} objets)")
    for child in collection.children:
        list_collections(child, indent + 1)

# Collection racine
list_collections(bpy.context.scene.collection)

# Lister tous les objets
print("\n📦 OBJETS (MESHES):")
print("-" * 40)

meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
for obj in sorted(meshes, key=lambda x: x.name):
    parent = obj.parent.name if obj.parent else "—"
    collections = ", ".join([c.name for c in obj.users_collection])
    print(f"• {obj.name}")
    print(f"    Parent: {parent} | Collections: {collections}")

print(f"\nTotal: {len(meshes)} meshes")

# Autres types d'objets
print("\n🔧 AUTRES OBJETS:")
print("-" * 40)
other_types = {}
for obj in bpy.data.objects:
    if obj.type != 'MESH':
        other_types[obj.type] = other_types.get(obj.type, 0) + 1

for obj_type, count in sorted(other_types.items()):
    print(f"• {obj_type}: {count}")

# Export GLB complet
print("\n" + "="*60)
print("EXPORT GLB")
print("="*60)

output_path = os.path.join(assets_dir, "engine_full.glb")

# Sélectionner tous les objets mesh
bpy.ops.object.select_all(action='DESELECT')
for obj in meshes:
    obj.select_set(True)

# Export
bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format='GLB',
    use_selection=False,  # Exporter toute la scène
    export_apply=True,    # Appliquer les modificateurs
    export_texcoords=True,
    export_normals=True,
    export_materials='EXPORT'
)

print(f"\n✅ Exporté: {output_path}")
print("="*60)
