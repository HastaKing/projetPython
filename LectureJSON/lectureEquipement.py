import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/modele")
from Equipement import *
import sqlite3

conn = sqlite3.connect('equipement.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS equipement")
c.execute('''CREATE TABLE equipement
				(
				EquNom text,
				EquipementId integer,
				InsNumeroInstall integer)''')

conn.commit()

equipement = open('data/data_equipement.json')
data_equipement = json.load(equipement)

#print(json.dumps(data_equipement, sort_keys=True, indent=4, separators=(',', ': ')))

for elem in data_equipement["data"]:
	monEquipement = Equipement(int(elem["EquipementId"]))
	monEquipement.setEquNom(elem["EquNom"])
	monEquipement.setInsNumeroInstall(int(elem["InsNumeroInstall"]))

	values = [(	monEquipement.getEquNom(),
				monEquipement.getEquipementId(),
				monEquipement.getInsNumeroInstall() )]
	c.executemany('INSERT INTO equipement VALUES (?,?,?)', values)
	#print (monEquipement)

#print(json.dumps(jr, sort_keys=True, indent=4, separators=(',', ': ')))

conn.commit()

for row in c.execute('SELECT * FROM equipement ORDER BY EquipementId'):
    print(row)

conn.close()