import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/modele")
from Activite import *
import sqlite3

conn = sqlite3.connect('activite.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS activite")
c.execute('''CREATE TABLE activite
				(ActCode integer,
				ActLib text,
				EquipementId integer)''')

conn.commit()

activite = open('data/data_activite.json')
data_activite = json.load(activite)

for elem in data_activite["data"]:
	monActivite = Activite(elem["EquipementId"])
	monActivite.setActCode(elem["ActCode"])
	monActivite.setActLib(elem["ActLib"])

	values = [(	monActivite.getEquipementId(),
				monActivite.getActCode(),
				monActivite.getActLib() )]
	c.executemany('INSERT INTO activite VALUES (?,?,?,?,?,?,?,?,?,?)', values)
	print (monActivite)

#print(json.dumps(jr, sort_keys=True, indent=4, separators=(',', ': ')))

conn.commit()

for row in c.execute('SELECT * FROM activite ORDER BY EquipementId'):
    print(row)

conn.close()