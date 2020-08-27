import json
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import os
from jsonpath_ng import parse
from collections import defaultdict

#parents = '..\\Assets\\Resources\\Outgame\\Data\\Sound' # Windows
parents = '../Assets/Resources/Outgame/Data/Sound'  # MacOS
os.chdir(parents)  # json 폴더 지정


def jsontodict(sound):
    results = defaultdict(dict)
    i = 0

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.json'):  # 특정 확장자만 열기
                fpath = os.path.join(root, file)  # join 으로 합쳐야지 str이 아닌 dir로 인식
                with open(fpath, encoding='cp949') as json_file:  # 인코딩 지정하지 않으면 에러 발
                    json_data = json.load(json_file)
                    json_str = json.dumps(json_data)

                    for key in parse('$..ContentsKey').find(json.loads(json_str)):
                        data = key.context.value['m_saveDataList']
                        for match in parse('$..soundName').find(data):
                            if sound == '':  # 빈 칸이면 모두
                                results[i]['file'] = file
                                results[i]['ContentsKey'] = key.context.value['ContentsKey']
                                results[i].update(match.context.value)
                                i += 1
                            elif sound in match.value:  # 특정 단어 포함하는지
                                results[i]['file'] = file
                                results[i]['ContentsKey'] = key.context.value['ContentsKey']
                                results[i].update(match.context.value)
                                i += 1

    return results


'''
엑셀로 쓰는 함수, 첫번째 행은 key들을 넣어주고 두번째 행부터는 value들
'''
def saveasxlsx(name, path):

    wb = Workbook()
    ws = wb.active
    ws.title = 'Sound'

    def toxls():

        rowindex = 1
        colindex = 1

        sounds = jsontodict()[0]

        for key in sounds[0]:
            ws.cell(row=rowindex, column=colindex).value = key
            ws.cell(row=rowindex, column=colindex).font = Font(bold=True, color='ffffff')
            ws.cell(row=rowindex, column=colindex).fill = PatternFill("solid", fgColor="404040")
            colindex += 1

        ws.freeze_panes = 'A2'
        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 30
        ws.column_dimensions['C'].width = 30
        ws.column_dimensions['D'].width = 30
        ws.column_dimensions['E'].width = 30
        ws.column_dimensions['F'].width = 30
        ws.column_dimensions['G'].width = 30
        ws.column_dimensions['H'].width = 30


        ws.auto_filter.ref = "A1:H1"

        colindex = 1
        rowindex = 2

        # for dict in allsoundtoxlsx():
        #     for data in dict:
        #         ws.cell(row=rowindex, column=colindex).value = dict[data]
        #         colindex += 1
        #     rowindex += 1
        #     colindex = 1

        for i in range(len(sounds)):
            for value in sounds[i].values():
                ws.cell(row=rowindex, column=colindex).value = value
                colindex += 1
            rowindex += 1



    toxls()
    #wb.save('C:\\Users\\trippysour\\Desktop\\EventSound.xlsx')
    wb.save('path'+'name')
    wb.close()

    return

'''
GUI 코드
# '''
from PySide2.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QHBoxLayout, QTableWidget, QLineEdit, QPushButton, QApplication, QLabel, QTableWidgetItem

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("SearchSound")
        self.setMinimumSize(875, 500)

        self.vb = QVBoxLayout()
        self.setLayout(self.vb)
        self.hbTop = QHBoxLayout()
        self.hbMid = QVBoxLayout()
        self.hbMid3 = QHBoxLayout()
        self.hbBot = QHBoxLayout()
        self.vb.addLayout(self.hbTop)
        self.vb.addLayout(self.hbMid)
        self.vb.addLayout(self.hbBot)

        self.ln = QLineEdit("Wwise Event 명")
        self.btn_name = QPushButton("Search By Name")
        self.btn_all = QPushButton("Search All")

        self.lb_result = QLabel("결과 :")
        self.tb_result = QTableWidget()
        self.tb_result.setAutoScroll(True)
        self.tb_result.showGrid()


        self.btn_save = QPushButton("Save As Xlsx")
        self.message = QMessageBox()

        self.hbTop.addWidget(self.ln)
        self.hbTop.addWidget(self.btn_name)
        self.hbTop.addWidget(self.btn_all)
        self.hbMid.addWidget(self.lb_result)
        self.hbMid.addWidget(self.tb_result)
        self.hbBot.addWidget(self.btn_save)

        self.btn_name.clicked.connect(self.search)
        self.btn_all.clicked.connect(self.search_all)

    def search_all(self):
        dict = jsontodict('')
        self.showresult(dict)
        self.lb_result.setText("결과 : 총 " + str(len(dict)) + " 개의 사운드를 찾았습니다.")
        return

    def search(self):
        dict = jsontodict(self.ln.text())
        self.showresult(dict)
        self.lb_result.setText("결과 : 총 " + str(len(dict)) + " 개의 사운드를 찾았습니다.")
        return


    def showresult(self, dict):
        self.tb_result.setRowCount(len(dict))

        header = []

        for key in dict[0].keys(): # 헤더 지정
            header.append(key)

        self.tb_result.setColumnCount(len(header))
        self.tb_result.setHorizontalHeaderLabels(header)
        self.lb_result.setText("결과 : 총 " + str(len(dict)) + " 개의 사운드를 찾았습니다.")

        for i in dict:
            for k in range(len(header)):
                item = QTableWidgetItem(str(dict[i][header[k]]))
                self.tb_result.setItem(i, k, item)

app = QApplication([])
GUI = Form()

GUI.show()
app.exec_()
