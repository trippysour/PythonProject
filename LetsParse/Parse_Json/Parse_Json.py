import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('./EventSound.json') as json_file:
    json_data = json.load(json_file)

    json_str = json.dumps(json_data, indent=4)
    json_dict = json.loads(json_str)
    print(json_str)
    #pp.pprint(json_dict)
    print(type(json_dict['datas'])) # list
    print(json_dict['datas'][0]) # {'Bt': [{'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}]}
    print(type(json_dict['datas'][0])) # dict
    print(json_dict['datas'][0]['Bt']) # [{'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}]
    print(type(json_dict['datas'][0]['Bt'])) #list
    print(json_dict['datas'][0]['Bt'][0]) # {'home_bt_moving_walk': [{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]}
    print(type(json_dict['datas'][0]['Bt'][0])) #dict
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk']) #[{'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}, {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '50.1'}]
    print(type(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'])) # list
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]) # {'animName': 'home_bt_moving_walk', 'soundName': 'BT_Footstep', 'targetObjName': '', 'sequenceTime': '0.1'}
    print(type(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]))  # dict
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['animName'])
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['soundName'])
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['targetObjName'])
    print(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0]['sequenceTime'])

    for i in range(len(json_dict['datas'])):
         for k in json_dict['datas'][i].keys(): # k = theme name
             print(k)

    for i in range(len(json_dict['datas'][0]['Bt'][0])):
         for k in json_dict['datas'][0]['Bt'][i].keys(): # k = theme name
             print(k)

    for i in range(len(json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][0])):
         for k in json_dict['datas'][0]['Bt'][0]['home_bt_moving_walk'][i].keys(): # k = theme name
             print(k)

    #https://khanrc.tistory.com/entry/PyCon-%EC%9C%84%EB%8C%80%ED%95%9C-dict-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
