import unreal

totalRequiredInstances = 15 #생성할 갯수를 변수로 지정

newAssetName = ""
sourceAssetPath = ""
createdAssetsPath = ""

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MyMaterialEditingLibrary(unreal.MaterialEditingLibrary):
    pass

editorUtil = MyEditorUtility()
materialEditingLib = MyMaterialEditingLibrary()

selectedAssets = editorUtil.get_selected_assets()

factor = unreal.MaterialInstanceConstantFactoryNew() # 무언갈 만들땐 항상 factory를 써서 생성

assetTools = unreal.AssetToolsHelpers.get_asset_tools()

for selectedAsset in selectedAssets:
    newAssetName = selectedAsset.get_name() + "_%s_%d" # 'inst' + numbering
    sourceAssetPath = selectedAsset.get_path_name()

    createdAssetsPath = sourceAssetPath.replace(selectedAsset.get_name(), "-") #replace("찾을값", "바꿀값), path_namae에서 어셋 네임을 -로 바꿈
    createdAssetsPath = createdAssetsPath.replace("-.-", "") #그러고 나면 -.- 라는 폴더 하위에 어셋이 생기는데 이걸 공백으로 바꿔주면 같은 폴더에 생김

    for x in range (totalRequiredInstances):
        newAsset = assetTools.create_asset(newAssetName %("inst", x+1), createdAssetsPath, None, factor) # asset_names(str), package_path(str), asset_class, factory(factory)
        materialEditingLib.set_material_instance_parent(newAsset, selectedAsset) #선택한 어셋을 기반으로 네이밍을 해서 만들고 여기서 그 선택한 어셋을 부모로 지정