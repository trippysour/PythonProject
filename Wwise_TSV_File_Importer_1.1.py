import os
from waapi import WaapiClient, CannotConnectToWaapiException
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, QApplication
# from pandas import Series, DataFrame
import json


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Wwise TSV File Importer")

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
        self.lbl2 = QLabel("텍스트 파일명을 입력해주세요")
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
        self.message1.setWindowTitle("Wwise TSV File Importer")
        self.message1.setText("텍스트 파일을 찾을 수 없습니다, 경로나 파일 명을 확인 해주세요.")

        self.btn2.clicked.connect(self.Import)

    def Import(self):
        createworkunits('Dialogue')
        texts = FindText(self.ln.text(), self.ln2.text())
        if texts[1] == 0:
            self.message1.exec()
        else:
            createworkunits('Dialogue')
            ImportToWwise(texts[0], self.check.isChecked(), self.combo2.currentText(), self.combo1.currentText())


app = QApplication([])
GUI = Form()

try:
    client = WaapiClient()

    def FindText(rootpath, filename):
        txt_all = []
        filename = filename if filename != '' else 'trackevents.txt'

        for root, dirs, files in os.walk(rootpath):
            for file in files:
                if file == filename and os.path.getsize(root + '/' + file) > 0:
                    txt_all.append(root + '/' + file)

        return (txt_all, len(txt_all))


    def createworkunits(name):
        actorargs = {
            "parent": "\Actor-Mixer Hierarchy",
            "type": "WorkUnit",
            "name": name
        }

        eventargs = {
            "parent": "\Events",
            "type": "WorkUnit",
            "name": name
        }
        print(type(actorargs))
        client.call("ak.wwise.core.object.create", actorargs)
        client.call("ak.wwise.core.object.create", eventargs)
        return


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

        json_str = json.dumps(result)
        json_dict = json.loads(json_str)

        for name in json_dict.values():
            for i in range(len(name)):
                if name[i].get('name') != 'Mixed' and name[i].get('name') != 'SFX' and name[i].get(
                        'name') != 'SoundSeed Grain' and name[i].get('name') != 'External':
                    lst.append(name[i].get('name'))
        return lst

    for lang in getlanguageinfo(client):
        GUI.combo1.addItem(lang)

    GUI.show()
    app.exec_()

except CannotConnectToWaapiException:
    GUI.message0 = QMessageBox()
    GUI.message0.setWindowTitle("Wwise TSV File Importer")
    GUI.message0.setText("WAAPI에 연결하지 못했습니다. : Wwise가 켜져있고 WAAPI가 Enabled 되어 있는지 체크 해주세요.")
    GUI.message0.exec()


# client.call("ak.wwise.ui.bringToForeground")


#pyinstaller --onefile --noconsole E:\01_Work\Python\Wwise_TSV_File_Importer\Wwise_TSV_File_Importer.py
