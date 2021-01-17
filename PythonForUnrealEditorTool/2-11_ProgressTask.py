import unreal

totalFrames = 500000 #enter_progress_frame을 쓰기 위해 frame 지정이 필요함
textDisplay = "i love python, and i guess i'll be using this for a while!"

with unreal.ScopedSlowTask(totalFrames, textDisplay) as ST:
    ST.make_dialog(True)
    for i in range (totalFrames):
        if ST.should_cancel():
            break
        unreal.log("one step!!!!")
        ST.enter_progress_frame(1)