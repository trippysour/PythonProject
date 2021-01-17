import unreal

#/Game/Mannequin/Animations/ThirdPersonJump_End.ThirdPersonJump_End
#/Game/Mannequin/Animations/anim_ThirdPersonJump_End.anim_ThirdPersonJump_End

prefixAnimationBlueprint    = "animBP"
prefixAnimationSequence     = "anim"
prefixAnimation             = "anim"
prefixBlendSpace            = "animBlnd"
prefixBlueprint             = "bp"
prefixCurveFloat            = "crvF"
prefixCurveLinearColor      = "crvL"
prefixLevel                 = "lvl"
prefixMaterial              = "mat"
prefixMaterialFunction      = "mat_func"
prefixMaterialInstance      = "mat_inst"
prefixParticleSystem        = "fx"
prefixPhysicsAsset          = "phsx"
prefixSkeletalMesh          = "sk"
prefixSkeleton              = "skln"
prefixSoundCue              = "cue"
prefixSoundWave             = "wv"
prefixStaticMesh            = "sm"
prefixTexture2D             = "tex"
prefixTextureCube           = "HDRI"

workingPath = "/Game/"

@unreal.uclass()
class MyEditorAssetLIbrary(unreal.EditorAssetLibrary):
    pass

def GetProperPrefix(className):
    _prefix = ""
    if className == "AnimBlueprint":
        _prefix = prefixAnimationBlueprint
    elif className == "AnimSequence":
        _prefix = prefixAnimationSequence
    elif className == "Animation":
        _prefix = prefixAnimation
    elif className == "BlendSpace1D":
        _prefix = prefixBlendSpace
    elif className == "Blueprint":
        _prefix = prefixBlueprint
    elif className == "CurveFloat":
        _prefix = prefixCurveFloat
    elif className == "CurveLinearColor":
        _prefix = prefixCurveLinearColor
    elif className == "Material":
        _prefix = prefixMaterial
    elif className == "MaterialFunction":
        _prefix = prefixMaterialFunction
    elif className == "MaterialInstance":
        _prefix = prefixMaterialInstance
    elif className == "ParticleSystem":
        _prefix = prefixParticleSystem
    elif className == "PhysicsAsset":
        _prefix = prefixPhysicsAsset
    elif className == "SkeletalMesh":
        _prefix = prefixSkeletalMesh
    elif className == "Skeleton":
        _prefix = prefixSkeleton
    elif className == "SoundCue":
        _prefix = prefixSoundCue
    elif className == "SoundWave":
        _prefix = prefixSoundWave
    elif className == "StaticMesh":
        _prefix = prefixStaticMesh
    elif className == "Texture2D":
        _prefix = prefixTexture2D
    elif className == "TextureCube":
        _prefix = prefixTextureCube
    else:
        _prefix = ""
    return  _prefix

editorAssetLib = MyEditorAssetLIbrary()

allAssets = editorAssetLib.list_assets(workingPath, True, False) #하위 모든 파일 선택
allAssetsCount = len(allAssets)

selectedAssetPath = workingPath

with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as ST:
    ST.make_dialog(True)

    for asset in allAssets:
        _assetData = editorAssetLib.find_asset_data(asset) #class와 path를 얻을 수 있음
        _assetName = _assetData.get_asset().get_name() #이름 얻기
        _assetPathName = _assetData.get_asset().get_path_name() #assetdata에서 path_name을 얻고
        _assetPathOnly = _assetPathName.replace((_assetName + "." + _assetName), "") #path_name은 asset_name.asset_name 형태로 나와서 공백으로 바꿈
        _assetClassName = _assetData.get_asset().get_class().get_name() #class 네임 얻기
        _assetPrefix = GetProperPrefix(_assetClassName) #위에 만들어놓은 함수인 GetProperPrefix에 위에서 얻은 class name을 넣해 return 받은 접두사

        if _assetPrefix in _assetName: #접두사가 이미 있으면 넘어가기
            continue
        elif _assetPrefix == "": #접두사 함수 케이스에 없으면 넘어가기
            continue
        else:
            _targetPathName = _assetPathOnly + ("%s%s%s%s%s%s%s" % (_assetPrefix, "_", _assetName, ".", _assetPrefix, "_", _assetName)) # 위에서 나온대로 접두사_어셋네임.접두사_어셋네임으로 만들기 위해 포맷팅

            editorAssetLib.rename_asset(_assetPathName, _targetPathName)
            unreal.log(">>>>>> Renaming [%s] to [%s]" %(_assetPathName, _targetPathName))

        if ST.should_cancel():
            break
        ST.enter_progress_frame(1, asset)

