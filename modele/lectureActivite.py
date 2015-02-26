import json
from Activite import Activite
import sqlite3

conn = sqlite3.connect('activite.db')

c = conn.cursor()

activite = open('../data_activite.json')
data_activite = json.load(activite)

for elem in data_activite["data"]:
	monActivite = Activite(elem["EquipementId"])
	monActivite.setActCode(elem["ActCode"])
	monActivite.setActLib(elem["ActLib"])
	monActivite.setActNivLib(elem["ActNivLib"])
	monActivite.setComInsee(elem["ComInsee"])
	monActivite.setComLib(elem["ComLib"])
	monActivite.setEquActivitePraticable(elem["EquActivitePraticable"])
	monActivite.setEquActivitePratique(elem["EquActivitePratique"])
	monActivite.setEquActiviteSalleSpe(elem["EquActiviteSalleSpe"])
	monActivite.setEquNbEquIdentique(elem["EquNbEquIdentique"])
	values = [(	elem["EquipementId"],
				elem["ActCode"],
				elem["ActLib"],
				elem["ActNivLib"],
				elem["ComInsee"],
				elem["ComLib"],
				elem["EquActivitePraticable"],
				elem["EquActivitePratique"],
				elem["EquActiviteSalleSpe"],
				elem["EquNbEquIdentique"])]
	c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', values)
	print (monActivite)

#print(json.dumps(jr, sort_keys=True, indent=4, separators=(',', ': ')))

conn.commit()

for row in c.execute('SELECT * FROM activite ORDER BY nom'):
    print(row)

conn.close()