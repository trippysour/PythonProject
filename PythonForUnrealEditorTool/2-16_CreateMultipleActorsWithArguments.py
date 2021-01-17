import unreal
import sys

actorsCount = int(float(sys.argv[1])) #언리얼에서 받는 string 인 slider의 값을 float로 받고 다시 int로 하여 사용
# rotationStep = int(float(sys.argv[2]))
# positionOffset = float(sys.argv[3])
slowTaskDisplayText = "Spawning actors in the level...."

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAssets = MyEditorUtility().get_selected_assets()

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range (actorsCount):
        if ST.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAssets[0], unreal.Vector(1.0+x*100, 1.0+x*100, 30.0), unreal.Rotator(0.0, 0.0, 10.0*x))
        unreal.log("Just added an actor to the level!")
        ST.enter_progress_frame(1)