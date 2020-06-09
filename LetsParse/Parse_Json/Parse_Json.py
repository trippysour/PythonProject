import json

with open('./EventSound.json') as json_file:
    json_data = json.load(json_file)
    json_str = json.dumps(json_data)
    json_dict = json.loads(json_str)

notifies = []

for i in range(len(json_dict['datas'])):
     for k in json_dict['datas'][i].keys():
         for n in json_dict['datas'][i][k][0].keys():
            for r in range(len(json_dict['datas'][i][k][0][n])):
                dict = json_dict['datas'][i][k][0][n][r]
                dict['theme'] = k
                notifies.append(dict)

print(notifies)

for dicts in notifies:
    print(dicts['theme'])
    print(dicts['animName'])
    print(dicts['soundName'])
    print(dicts['targetObjName'])
    print(dicts['sequenceTime'])
