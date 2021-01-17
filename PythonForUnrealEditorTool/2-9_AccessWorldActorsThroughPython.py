import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    # unreal.log(actor.get_name())
    if actor.actor_has_tag('1'):
        unreal.log(actor.get_name())
    if not actor.actor_has_tag('3'):
        unreal.log(actor.get_name())