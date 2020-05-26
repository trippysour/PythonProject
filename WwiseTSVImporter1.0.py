import os
from waapi import WaapiClient, CannotConnectToWaapiException
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, QApplication
from PySide2.QtGui import QIcon
import json

'''
GUI 코드
'''

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Wwise TSV Importer")
        self.setMinimumSize(350, 200)
        self.setMaximumSize(350, 200)

        self.vb = QVBoxLayout()
        self.setLayout(self.vb)
        self.hbTop = QVBoxLayout()
        self.hbMid = QVBoxLayout()
        self.hbMid1 = QHBoxLayout()
        self.hbMid2 = QHBoxLayout()
        self.hbMid3 = QHBoxLayout()
        self.hbBot = QHBoxLayout()
        self.vb.addLayout(self.hbTop)
        self.vb.addLayout(self.hbMid)
        self.vb.addLayout(self.hbMid1)
        self.vb.addLayout(self.hbMid2)
        self.vb.addLayout(self.hbMid3)
        self.vb.addLayout(self.hbBot)

        self.lbl = QLabel("텍스트 파일들이 존재하는 경로를 입력해주세요.")
        self.ln = QLineEdit("ex. C:\\")
        self.lbl2 = QLabel("텍스트 파일명을 입력해주세요.")
        self.ln2 = QLineEdit('trackevents.txt')
        self.btn2 = QPushButton("임포트")
        self.lbl3 = QLabel("importLanguage")
        self.combo1 = QComboBox()
        self.lbl4 = QLabel("importOperation")
        self.combo2 = QComboBox()
        self.combo2.addItem("useExisting")
        self.combo2.addItem("createNew")
        self.combo2.addItem("replaceExisting")
        self.lbl5 = QLabel("autoAddToSourceControl")
        self.check = QCheckBox()
        self.check.setChecked(1)

        self.hbTop.addWidget(self.lbl)
        self.hbTop.addWidget(self.ln)
        self.hbMid.addWidget(self.lbl2)
        self.hbMid.addWidget(self.ln2)
        self.hbMid1.addWidget(self.lbl5)
        self.hbMid1.addWidget(self.check)
        self.hbBot.addWidget(self.btn2)
        self.hbMid2.addWidget(self.lbl3)
        self.hbMid2.addWidget(self.combo1)
        self.hbMid3.addWidget(self.lbl4)
        self.hbMid3.addWidget(self.combo2)

        self.message1 = QMessageBox()
        self.message1.setWindowTitle("Wwise TSV Importer")
        self.message1.setIcon(QMessageBox.Warning)
        self.message1.setText("텍스트 파일을 찾을 수 없습니다, 경로나 파일 명을 확인 해주세요.")

        self.btn2.clicked.connect(self.Import)

    '''
    GUI 버튼과 팝업 오브젝트를 이용해서 다른 함수들과 연결
    '''

    def Import(self):
        texts = FindText(self.ln.text(), self.ln2.text())
        if texts[1] == 0:
            self.message1.exec()
        else:
            findworkunitandcreate('\Actor-Mixer Hierarchy', 'Dialogue')
            findworkunitandcreate('\Events', 'Dialogue')
            ImportToWwise(texts[0], self.check.isChecked(), self.combo2.currentText(), self.combo1.currentText())
            print('s')
            self.message2 = QMessageBox()
            self.message2.setWindowTitle("Wwise TSV Importer")
            self.message2.setIcon(QMessageBox.Information)
            self.message2.setText("총 " + str(texts[1]) + "개의 TSV 파일을 임포트 했습니다.")
            self.message2.exec()
        return


app = QApplication([])
app.setWindowIcon(QIcon("E:\\01_Work\\Python\\WwiseTSVImporter\\ncsound.ico")) # app 아이콘 지정
GUI = Form()

'''
WAAPI 연결 체크 성공하면 try로, 아니면 except로
'''

try:
    client = WaapiClient()
    
    '''
    GUI로 입력받는 path와 filename 으로 path 안에 1바이트 이상의 파일 찾아서 풀 경로를 txt_all 리스트로 그 갯수도 반환
    '''
    def FindText(rootpath, filename):
        txt_all = []
        filename = filename if filename != '' else 'trackevents.txt'

        for root, dirs, files in os.walk(rootpath):
            for file in files:
                if file == filename and os.path.getsize(root + '/' + file) > 0:
                    txt_all.append(root + '/' + file)

        return (txt_all, len(txt_all))


    '''
    워크유닛이 없으면 임포트 되지 않는 것을 WAAPI로 해당 워크유닛을 찾고 없으면 생성 하는 것으로 해결
    '''
    def findworkunitandcreate(path, name):
        arg = {
            "from": {
                "path": [
                    path
                ]
            },
            "transform": [
                {
                    "select": [
                        "children"
                    ]
                },
                {
                    "where": [
                        "type:isIn",
                        [
                            "WorkUnit"
                        ],
                    ],
                    "where": [
                        "name:matches", name
                    ]
                }
            ]
        }
        options = {
            "return": ['name']
        }
        result = client.call("ak.wwise.core.object.get", arg, options=options)

        json_str = json.dumps(result)

        if json_str == '{"return": []}':
            args = {
                "parent": path,
                "type": "WorkUnit",
                "name": name
            }
            client.call("ak.wwise.core.object.create", args)

    '''
    GUI 임포트 버튼과 연결될 함수, GUI로 부터 받은 인자 대로 WAAPI를 통해 임포트
    '''
    def ImportToWwise(txtlist, autosourcebool, importoperation, importlanguage):
        for i, v in enumerate(txtlist):
            args = {
                'autoAddToSourceControl': autosourcebool,
                'importFile': v,
                'importOperation': importoperation,
                'importLanguage': importlanguage
            }
            client.call("ak.wwise.core.audio.importTabDelimited", args)
        return
    '''
    임포트 아규먼트중 language 가 있는데 선택지를 현재 프로젝트에서 WAAPI로 불러와서 제공
    '''
    def getlanguageinfo(client):
        lst = []

        langargs = {
            "from": {
                "ofType": [
                    "Language"
                ]
            }
        }

        options = {
            "return": ['name']
        }

        result = client.call("ak.wwise.core.object.get", langargs, options=options)

        json_str = json.dumps(result) # result로 받은 결과를 str로
        json_dict = json.loads(json_str) # 그걸 다시 dict로

        for name in json_dict.values():
            for i in range(len(name)): # name 키값을 받는 value 중 Mixed, SoundSeed Grain, External 제거
                if name[i].get('name') != 'Mixed' and name[i].get('name') != 'SFX' and name[i].get(
                        'name') != 'SoundSeed Grain' and name[i].get('name') != 'External':
                    lst.append(name[i].get('name'))
        return lst

    for lang in getlanguageinfo(client):
        GUI.combo1.addItem(lang) # 필터링된 result를 GUI 콤보박스의 아이템으로 추가

    GUI.show()
    app.exec_()
    client.call("ak.wwise.ui.bringToForeground")

except CannotConnectToWaapiException: # WAAPI에 연결 되지 않으면 바로 팝업으로 알려주고 종료
    GUI.message0 = QMessageBox()
    GUI.message0.setWindowTitle("Wwise TSV Importer")
    GUI.message0.setIcon(QMessageBox.Warning)
    GUI.message0.setText("WAAPI에 연결하지 못했습니다. : Wwise가 켜져있고 WAAPI가 Enabled 되어 있는지 체크 해주세요.")
    GUI.message0.exec()



