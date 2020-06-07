import json
from json2xls.json2xls import Json2Xls
import pprint
from json2xml import json2xml
from json2xml.utils import readfromjson

pp = pprint.PrettyPrinter(indent=4)

data = readfromjson('./EventSound.json')
#print(json2xml.Json2xml(data).to_xml())

with open('./EventSound.json') as json_file:
    json_data = json.load(json_file)
    json_str = json.dumps(json_data, indent=4)
    json_dict = json.loads(json_str)
    obj = Json2Xls('test.xls', json_str)
    obj.make()

    edges = []
    leaves = []
    nodes = []


    def paths(data):
        for key, value in data.items():
            yield key
            if 'children' in value:
                for child in value['children']:
                    for path in paths(child):
                        yield f'{key}/{path}'


    print(list(paths(json_dict['datas'][0])))

    for i in range(len(json_dict['datas'])):
        print(list(paths(json_dict['datas'][i])))


    # # print(json_str)
    # pp.pprint(json_dict)
    # print(type(json_dict['datas'])) # list
    # print(json_dict['datas'][0]) # {'Bt': [{'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}]}
    # print(type(json_dict['datas'][0])) # dict
    # print(json_dict['datas'][0]['Bt']) # [{'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}]
    # print(type(json_dict['datas'][0]['Bt'])) #list
    # print(json_dict['datas'][0]['Bt'][0]) # {'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}
    # print(type(json_dict['datas'][0]['Bt'][0])) #dict
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk']) #[{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]
    # print(type(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'])) # list
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]) # {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}
    # print(type(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]))  # dict
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['animName'])
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['soundName'])
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['targetObjName'])
    # print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['sequenceTime'])
    #
    # for i in range(len(json_dict['datas'])):
    #      for k in json_dict['datas'][i].keys(): # k = theme name
    #          print(k)
    #
    # for i in range(len(json_dict['datas'][0]['Bt'][0])):
    #      for k in json_dict['datas'][0]['Bt'][i].keys(): # k = theme name
    #          print(k)
