import os # 2번줄 위해서 import
os.chdir('F:\\AION\\AION\\AION_Data\\Data\\animationmarkers') # 작업 디렉토리 
import xml.etree.ElementTree as ET # xml 파씽 라이브러리
import csv

def find_amb_in_anim(dirname):
    filenames =  os.listdir(dirname)

    def findsound(xmlfile):
        xml = ET.parse(xmlfile)
        root = xml.getroot()

        isTrue = False
        sound_name = ''
        sound_volume = ''

        for seq in root.iter('animation'): 
            seq_name = seq.get('name')
            for sounds in seq:
                if sounds.get('file') != None and sounds.get('file') != '':
                    if sounds.get('file').startswith('Sounds\\ambient'):
                        isTrue = True
                        sound_name = sounds.get('file')
                        sound_volume = sounds.get('vol')
        return [isTrue, xmlfile, seq_name, sound_name, sound_volume]

    f = open('E://anim2.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)

    for filename in filenames:
        lst = findsound(filename)
        for i in lst:
            if lst[0] == True:
                wr.writerow([lst[1], lst[2], lst[3], lst[4]])
        f.close
        
    print('Done!!')
    return

find_amb_in_anim('F:\\AION\\AION\\AION_Data\\Data\\animationmarkers')



# def getlanguage(path):
#     xml = ET.parse(path)
#     root = xml.getroot()
#     language = []
#     for languages in root.iter('LanguageList'):
#         for child in languages:
#             name = child.get('Name')
#             if name != 'External' and name != 'Mixed' and name != 'SFX':
#                 language.append(name)
#     return (language)


'''
'''
import os # 2번줄 위해서 import
os.chdir('F:\\AION\\AION\\AION_Data\\Editor\\particles') # 작업 디렉토리
import xml.etree.ElementTree as ET # xml 파씽 라이브러리
import csv

def find_amb_in_particles(dirname):
    filenames =  os.listdir(dirname)

    def findsound(xmlfile):
        xml = ET.parse(xmlfile)
        root = xml.getroot()

        isTrue = False
        particle_name = ''
        sound_name = ''
        sound_volume = ''

        for particles in root.iter('Particles'): 
            for sounds in particles:
                if sounds.get('Sound') != None and sounds.get('Sound') != '':
                    if sounds.get('Sound').startswith('Sounds\\ambient\\'):
                        isTrue = True
                        particle_name = particles.get('Name')
                        sound_name = sounds.get('Sound')
                        sound_volume = sounds.get('SoundVolume')
        return [isTrue, xmlfile, particle_name, sound_name, sound_volume]
    
    f = open('E://particle2.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    #wr.writerow(['xmlfile', 'particle_name', 'sound_name', 'sound_volume'])

    for filename in filenames:
        lst = findsound(filename)
        for i in lst:
            if lst[0] == True:# and not(lst[1].startswith('env') or lst[1].startswith('sys')):
                wr.writerow([lst[1], lst[2], lst[3], lst[4]])
        f.close

    print('Done!!')
    return 

find_amb_in_particles('F:\\AION\\AION\\AION_Data\\Editor\\particles')
