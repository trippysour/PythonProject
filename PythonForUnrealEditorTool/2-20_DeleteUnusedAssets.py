import unreal

workingPath = "/Game/" #언리얼 백그라운드에서는 Contents 폴더를 뜻함

@unreal.uclass()
class MyEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

AssetLib = MyEditorAssetLibrary()

allAssets = AssetLib.list_assets(workingPath, True, False)
#workingpath 하위의 모든 어셋을 불러옴

processingAssetPath = ""
allAssetsCount = len(allAssets)

if (allAssetsCount > 0):
    with unreal.ScopedSlowTask(allAssetsCount, processingAssetPath) as ST:
        ST.make_dialog(True)
        for asset in allAssets:
            processingAssetPath = asset
            deps = AssetLib.find_package_referencers_for_asset(asset, False) #디펜던시가 0이면 레퍼런스가 없음을 뜻함
            if (len(deps) <= 0):
                unreal.log(">>>>>> Deleteing >>>>> %s" % asset)
                AssetLib.delete_asset(asset)
            if ST.should_cancel():
                break
            ST.enter_progress_frame (1, processingAssetPath)