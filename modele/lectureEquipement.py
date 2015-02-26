import json

equipement = open('../data_equipement.json')
data_equipement = json.load(equipement)

print(json.dumps(data_equipement, sort_keys=True, indent=4, separators=(',', ': ')))