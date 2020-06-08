import json
from json2xml import json2xml
from json2xml.utils import readfromjson
from xml.etree.ElementTree import parse, ElementTree


data = readfromjson('./EventSound.json')
xml = json2xml.Json2xml(data).to_xml()

tree = ElementTree(xml)
root = tree.getroot()

print(root)
