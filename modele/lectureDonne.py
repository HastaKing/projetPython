import json
 
file = open('../data_installation.json')
jr = json.load(file)

data = json.dumps(jr)

#json.JSONEncoder().decode(data)

#print(data)

print(jr["data"][0]["ActCode"])
#for i in range(1, 2):
#	print(jr["data"][i])

#	i += 1


#print(json.dumps(jr, sort_keys=True, indent=4, separators=(',', ': ')))
