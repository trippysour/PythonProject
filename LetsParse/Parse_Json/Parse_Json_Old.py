import json
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import os

parents = '..\\Assets\\Resources\\Outgame\\Data\\Sound'
os.chdir(parents) # json 폴더 지정

'''
Json --> Dictionary
'''
def ParseJson():
    all = []
    alldict = []

    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.lower().endswith('.json'):  # 특정 확장자만 열기
                fpath = os.path.join(root, file)  # join 으로 합쳐야지 str이 아닌 dir로 인식
                with open(fpath, encoding='cp949') as json_file:
                    json_data = json.load(json_file)
                    json_str = json.dumps(json_data)
                    json_dict = json.loads(json_str)
                    all.append(json_dict)

    for i in range(len(all)):
        if 'm_saveDataList' in all[i]:
            dicttemp1 = {}
            for n in range(len(all[i]['m_saveDataList'])):
                dicttemp1['Json'] = all[i]["ContentsKey"]
                for k in range(len(all[i]['m_saveDataList'][n]['EventSoundDataList'])):
                    dicttemp2 = all[i]['m_saveDataList'][n]['EventSoundDataList'][k]
                    alldict.append({**dicttemp1, **dicttemp2})
        elif 'ObjectDataList' in all[i]:
            dicttemp1 = {}
            for o in range(len(all[i]['ObjectDataList'])):
                dicttemp1['Json'] = all[i]["ThemeKey"]
                for m in range(len(all[i]['ObjectDataList'][o]['m_saveDataList'])):
                    for h in range(len(all[i]['ObjectDataList'][o]['m_saveDataList'][m]['EventSoundDataList'])):
                        dicttemp2 = all[i]['ObjectDataList'][o]['m_saveDataList'][m]['EventSoundDataList'][h]
                        alldict.append({**dicttemp1, **dicttemp2})
    return alldict
