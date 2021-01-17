import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MyAnimationLibrary(unreal.AnimationLibrary):
    pass

EdUtil = MyEditorUtility()
AnimLib = MyAnimationLibrary()

selectedAssets = EdUtil.get_selected_assets()

for asset in selectedAssets:
    asset.modify(True)
    AnimLib.remove_all_animation_notify_tracks(asset)