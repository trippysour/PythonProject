import unreal

totalRequiredBlueprints = 70
newAssetName = "BP_pythonMade_%d" #%d 로 배치 넘버링
createdAssetsPath = "/Game/TestStuff" #path가 존재 하지 않으면 폴더까지 생성함
slowTaskDisplayText = "Createing new assets....."

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Pawn)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()

with unreal.ScopedSlowTask(totalRequiredBlueprints, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range(totalRequiredBlueprints): #실제로 생성하는 단계
        if ST.should_cancel():
            break
        newAsset = assetTools.create_asset(newAssetName%(x), createdAssetsPath, None, factory) #%d = for 도는 x 인덱스
        unreal.EditorAssetLibrary.save_loaded_asset(newAsset)
        unreal.log("Just created an asset BP_PythonMade_%d via PYTHON API" %(x))
        ST.enter_progress_frame(1)