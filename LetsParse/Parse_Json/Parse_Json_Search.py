import json
from jsonpath_ng import parse


with open('EventSound.json') as j:
    d = json.load(j)
    json_str = json.dumps(d)
    json_dict = json.loads(json_str)

    jsonpath_expr = parse('$..soundName')

    for match in jsonpath_expr.find(json_dict):
        print(match.value)
        print(match.full_path)
