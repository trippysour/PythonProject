import unreal

blueprintName = "MyEpicBPActorClass"
blueprintPath = "/Game/AutoCreated"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.PlayerController)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
#unreal.AssetToolsHelpers 는 get_asset_tools 한 기능 밖에 없고 사용 할 때 마다 불러줘야 해서 변수로 지정
myFancyNewAssetFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

unreal.EditorAssetLibrary.save_loaded_asset(myFancyNewAssetFile)