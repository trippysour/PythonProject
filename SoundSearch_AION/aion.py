import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import xml.etree.ElementTree as ET
from collections import defaultdict
from PySide2.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QHBoxLayout, QTableWidget, QLineEdit, QPushButton, QApplication, QLabel, QTableWidgetItem, QFileDialog, QAbstractItemView
from PySide2.QtGui import QColor


#parents = '..\\Assets\\Resources\\Outgame\\Data\\Sound' # 실제 path
parents = os.getcwd()  # 개발전용
os.chdir(parents)  # json 폴더 지정


def sound_in_anim(dirname):
    header = ['file', 'seq_name', 'sound_name', 'InRadius', 'OutRadius', 'vol']

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.xml'):  # 특정 확장자만 열기
                xml = ET.parse(file)
                root = xml.getroot()

                for seq in root.iter('animation'):
                    seq_name = seq.get('name')
                    for sounds in seq.findall('sound'):
                        if sounds.get('file') != None:
                            sound_name = sounds.get('file')
                            InRadius = sounds.get('TOOL_InRadius')
                            OutRadius =  sounds.get('TOOL_OutRadius')
                            vol = sounds.get('vol')
                            print(file, seq_name, sound_name, vol, InRadius, OutRadius)
                        else:
                            for sound in sounds.findall('probsound'):
                                sound_name = sound.get('file')
                                InRadius = sound.get('TOOL_InRadius')
                                OutRadius = sound.get('TOOL_OutRadius')
                                vol = sound.get('vol')
                                print(file, seq_name, sound_name, vol, InRadius, OutRadius)
    return

sound_in_anim(parents)
#
#
# def find_amb_in_particles(dirname):
#     filenames =  os.listdir(dirname)
#
#     def findsound(xmlfile):
#         xml = ET.parse(xmlfile)
#         root = xml.getroot()
#
#         isTrue = False
#         particle_name = ''
#         sound_name = ''
#         sound_volume = ''
#
#         for particles in root.iter('Particles'):
#             for sounds in particles:
#                 if sounds.get('Sound') != None and sounds.get('Sound') != '':
#                     if sounds.get('Sound').startswith('Sounds\\ambient\\'):
#                         isTrue = True
#                         particle_name = particles.get('Name')
#                         sound_name = sounds.get('Sound')
#                         sound_volume = sounds.get('SoundVolume')
#         return [isTrue, xmlfile, particle_name, sound_name, sound_volume]
#
#     f = open('E://particle2.csv', 'w', encoding='utf-8', newline='')
#     wr = csv.writer(f)
#     #wr.writerow(['xmlfile', 'particle_name', 'sound_name', 'sound_volume'])
#
#     for filename in filenames:
#         lst = findsound(filename)
#         for i in lst:
#             if lst[0] == True:# and not(lst[1].startswith('env') or lst[1].startswith('sys')):
#                 wr.writerow([lst[1], lst[2], lst[3], lst[4]])
#         f.close
#
#     print('Done!!')
#     return
#
# find_amb_in_particles(parents)
