import unreal

actorsCount = 50 #이런 단위는 변수로 만들어 두는 것이 나중에 바꾸는 것이 편함
slowTaskDisplayText = "Spawning actors in the level...."

@unreal.uclass() #에디터 유틸리티를 불러오는 이유는 밑에 selectedAssets을 사용하기 위해서 필요함
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAssets = MyEditorUtility().get_selected_assets() #unreal.GlobalEditorUtilityBase의 get_selected_assets를 사용하기 위해 위에 오브젝트 생성

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range (actorsCount):
        if ST.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAssets[0], unreal.Vector(1.0+x*100, 1.0+x*100, 30.0), unreal.Rotator(0.0, 0.0, 10.0*x))
        # 레벨에 사용하기 위한 unreal.EditorLevelLibrary의 spawn_actor_from_object 사용
        ST.enter_progress_frame(1)