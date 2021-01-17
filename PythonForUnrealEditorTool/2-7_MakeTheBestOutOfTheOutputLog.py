import unreal

info = dir(unreal)
sampletext = 's'

for i in info:
    unreal.log("unreal." + str(i))
    unreal.log(sampletext)

