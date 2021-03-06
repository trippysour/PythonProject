import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

EdUtil = MyEditorUtility()

selectedAssets = EdUtil.get_selected_assets()

for selectedAsset in selectedAssets:
    selectedAsset.set_editor_property("BlueprintDisplayName", "Some BP")
    selectedAsset.set_editor_property("BlueprintDescription", "This is a blueprint generated by Python or something")
    selectedAsset.set_editor_property("BlueprintCategory", "Collectable")

    selectedActors = EdUtil.get_selection_set()

for actor in selectedActors:
    actor.set_editor_property("canRotate", True)
    actor.set_editor_property("bHidden", 1)
    actor.set_editor_property("SpriteScale", 3.5)