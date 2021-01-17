import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAssets = MyEditorUtility().get_selected_assets()

for asset in selectedAssets:
    #unreal.log("there is something selected")
    unreal.log(asset.get_full_name())
    unreal.log(asset.get_fname())
    unreal.log(asset.get_name())
    unreal.log(asset.get_path_name())
    unreal.log(asset.get_class())
    unreal.log_warning("*************************************************")