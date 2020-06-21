import json
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'EventSound'

with open('./EventSound.json') as json_file:
    json_data = json.load(json_file)
    json_str = json.dumps(json_data)
    json_dict = json.loads(json_str)

all = [] # WAAPI와도 통신 하기 위해서 따로 빼놓기

for i in range(len(json_dict['datas'])):
    for k in json_dict['datas'][i].keys():  # k = theme, 캐릭터 이름
        dict = {}
        dict['Theme Or Character'] = k
        for n in json_dict['datas'][i][k][0].keys():  # n = 애니메인션 이름
            for r in range(len(json_dict['datas'][i][k][0][n])):
                dict.update(json_dict['datas'][i][k][0][n][r])  # dict = 노티파이 딕셔너
                all.append(dict)

'''
엑셀로 쓰는 함수, 첫번째 행은 key들을 넣어주고 두번째 행부터는 value들
all로 다른 함수도 돌리기 위해서 따로 함수로 
'''

def toxls(all):

    rowindex = 1
    colindex = 1

    for key in all[0]:
        ws.cell(row=rowindex, column=colindex).value = key
        colindex += 1

    colindex = 1
    rowindex = 2

    for dict in all:
        for data in dict:
            ws.cell(row=rowindex, column=colindex).value = dict[data]
            colindex += 1
        rowindex += 1
        colindex = 1


toxls(all)
wb.save('./EventSound.xlsx')
wb.close()
print('done')
