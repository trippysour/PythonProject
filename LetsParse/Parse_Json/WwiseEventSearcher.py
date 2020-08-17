import json
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import os
from jsonpath_ng import parse
from collections import defaultdict

#parents = '..\\Assets\\Resources\\Outgame\\Data\\Sound' # Windows
parents = '../Assets/Resources/Outgame/Data/Sound'  # MacOS
os.chdir(parents)  # json 폴더 지정



def jsontodict():
    alldicts = defaultdict(dict)
    index = 0

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.json'):  # 특정 확장자만 열기
                fpath = os.path.join(root, file)  # join 으로 합쳐야지 str이 아닌 dir로 인식
                with open(fpath, encoding='cp949') as json_file: # 인코딩 지정하지 않으면 에러 발
                    json_data = json.load(json_file)
                    json_str = json.dumps(json_data)

                    alldicts[index]['data'] = json.loads(json_str)
                    alldicts[index]['data']['file'] = file
                    index += 1
    return alldicts

json_dicts = jsontodict()

print(json_dicts)

def findsound(sound):

    results = defaultdict(dict)
    index = 0

    searchsoundName = parse('$..soundName') # 하위 모든 경로 중 'soundname' 탐색
    searchContentsKey = parse('$..ContentsKey')
    file = parse('$..file')

    for key in searchContentsKey.find(json_dicts):
        data = key.context.value['m_saveDataList']
        for match in searchsoundName.find(data):  # data 안에서 soundname 필터링
            if sound == '':
                results[index]['ContentsKey'] = key.context.value['ContentsKey']
                results[index].update(match.context.value)
                index += 1
            elif match.value == sound:
                results[index]['ContentsKey'] = key.context.value['ContentsKey']
                results[index].update(match.context.value)
                index += 1

    return results


print(len(findsound('')))
print(findsound('Choco_Idle_VOX'))

'''
엑셀로 쓰는 함수, 첫번째 행은 key들을 넣어주고 두번째 행부터는 value들
'''
#
# wb = Workbook()
# ws = wb.active
# ws.title = 'EventSound'
#
# def toxls():
#
#     rowindex = 1
#     colindex = 1
#
#     sounds = allsoundtoxlsx()
#
#     for key in sounds[0]:
#         ws.cell(row=rowindex, column=colindex).value = key
#         ws.cell(row=rowindex, column=colindex).font = Font(bold=True, color='ffffff')
#         ws.cell(row=rowindex, column=colindex).fill = PatternFill("solid", fgColor="404040")
#         colindex += 1
#
#     ws.freeze_panes = 'A2'
#     ws.column_dimensions['A'].width = 30
#     ws.column_dimensions['B'].width = 30
#     ws.column_dimensions['C'].width = 30
#     ws.column_dimensions['D'].width = 30
#     ws.column_dimensions['E'].width = 30
#     ws.column_dimensions['F'].width = 30
#     ws.column_dimensions['G'].width = 30
#     ws.column_dimensions['H'].width = 30
#
#
#     ws.auto_filter.ref = "A1:H1"
#
#     colindex = 1
#     rowindex = 2
#
#     # for dict in allsoundtoxlsx():
#     #     for data in dict:
#     #         ws.cell(row=rowindex, column=colindex).value = dict[data]
#     #         colindex += 1
#     #     rowindex += 1
#     #     colindex = 1
#
#     for i in range(len(sounds)):
#         for value in sounds[i].values():
#             ws.cell(row=rowindex, column=colindex).value = value
#             colindex += 1
#         rowindex += 1
#
#
#
# toxls()
# #wb.save('C:\\Users\\trippysour\\Desktop\\EventSound.xlsx')
# wb.save('EventSound.xlsx')
# wb.close()
#
#print(searchReference('Camera_Shutter')[0]['file'])

#
# '''
# GUI 코드
# # '''
# from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, QApplication
#
# class Form(QWidget):
#     def __init__(self):
#         super(Form, self).__init__()
#         self.setWindowTitle("JSON To XLSX")
#         self.setMinimumSize(350, 200)
#         self.setMaximumSize(350, 200)
#
# #결과 팝업창, json 열기 버튼, exel 시트 만들기버튼
#
# app = QApplication([])
# GUI = Form()
#
# GUI.show()
# app.exec_()
