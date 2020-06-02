import json
import pandas as pd

# with open('E:\\01_Work\\Python\\LetsParse\\Parse_Json\\EventSound.json') as json_file:
#     json_data = json.load(json_file)
#
#     json_str = json.dumps(json_data, indent=4)
#     json_dict = json.loads(json_str)
#
#     print(json_dict)
#     print(json_dict['datas'])
#     print(len(json_dict['datas']))
#
#     for i in range(len(json_dict['datas'])):
#          for k in json_dict['datas'][i].keys(): # k = theme name
#              print(k)

df = pd.read_json("./EventSound.json")

https://youtu.be/SrQlQrfcFwY
