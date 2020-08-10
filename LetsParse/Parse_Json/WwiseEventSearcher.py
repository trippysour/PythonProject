import json
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import os
from jsonpath_ng import parse

parents = '..\\Assets\\Resources\\Outgame\\Data\\Sound' # Windows
#parents = '../Assets/Resources/Outgame/Data/Sound'  # MacOS
os.chdir(parents)  # json 폴더 지정



def searchReference(sound):
    results = []  # json 이름, Contents Key, 노티파이정보'
    dict = {}
    index = 0

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.json'):  # 특정 확장자만 열기
                fpath = os.path.join(root, file)  # join 으로 합쳐야지 str이 아닌 dir로 인식
                with open(fpath, encoding='cp949') as json_file: # 인코딩 지정하지 않으면 에러 발
                    json_data = json.load(json_file)
                    json_str = json.dumps(json_data)
                    json_dict = json.loads(json_str)

                searchsoundName = parse('$..soundName') # 하위 모든 경로 중 'soundname' 탐색
                searchContentsKey = parse('$..ContentsKey') # 위에 필터로는 컨텐츠키를 알 수 없어서 키를 찾는 필터 넣기

                for key in searchContentsKey.find(json_dict):
                    data = key.context.value['m_saveDataList']
                    for match in searchsoundName.find(data): # data 안에서 soundname 필터링
                        if match.value == sound:
                            dict['file'] = file
                            # print(file)
                            # print(key.context.value['ContentsKey'])
                            dict['ContentsKey'] = key.context.value['ContentsKey']
                            # print(match.context.value)
                            dict['Notify'] = match.context.value
                            print(dict)
                            index += 1

    return results


print(searchReference('CloudDeco_3D_Loop'))
def allsoundtoxlsx():
    results = []  # json 이름, Contents Key, 노티파이정보'

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.json'):  # 특정 확장자만 열기
                fpath = os.path.join(root, file)  # join 으로 합쳐야지 str이 아닌 dir로 인식
                with open(fpath, encoding='cp949') as json_file:  # 인코딩 지정하지 않으면 에러 발
                    json_data = json.load(json_file)
                    json_str = json.dumps(json_data)
                    json_dict = json.loads(json_str)

                ContentsKeys = parse('$..ContentsKey')

                for match in ContentsKeys.find(json_dict):
                    print(file)
                    print(match.context.value['ContentsKey'])

                    for soundnodes in match.context.value['m_saveDataList']:
                        for data in soundnodes['EventSoundDataList']:
                            print(data)
    return

#allsoundtoxlsx() #절대경로여야할듯

#
#
# '''
# 엑셀로 쓰는 함수, 첫번째 행은 key들을 넣어주고 두번째 행부터는 value들
# '''
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
#     for key in ParseJson()[0]:
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
#
#     ws.auto_filter.ref = "A1:G1"
#
#     colindex = 1
#     rowindex = 2
#
#     for dict in ParseJson():
#         for data in dict:
#             ws.cell(row=rowindex, column=colindex).value = dict[data]
#             colindex += 1
#         rowindex += 1
#         colindex = 1
#
#
# toxls()
# wb.save('C:\\Users\\trippysour\\Desktop\\EventSound.xlsx')
# wb.close()
#

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

