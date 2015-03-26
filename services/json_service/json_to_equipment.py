import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/model")
from equipment import *
import sqlite3


"""
	dataBase creation (if it exists, clear it)
"""
conn = sqlite3.connect('dataBase.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS equipment")
c.execute('''CREATE TABLE equipment
				(
				EquNom text,
				EquipementId integer,
				InsNumeroInstall integer)''')
conn.commit()


"""
	Load JSON file
"""
equipment = open('data/data_equipment.json')
data_equipment = json.load(equipment)


"""
	Insert data into the dataBase
"""
for elem in data_equipment["data"]:
	MyEquipment = Equipment(int(elem["EquipementId"]))
	MyEquipment.setEquNom(elem["EquNom"])
	MyEquipment.setInsNumeroInstall(int(elem["InsNumeroInstall"]))

	values = [(	MyEquipment.getEquNom(),
				MyEquipment.getEquipementId(),
				MyEquipment.getInsNumeroInstall() )]
	c.executemany('INSERT INTO equipment VALUES (?,?,?)', values)
conn.commit()


"""
	Print the result
"""
"""
for row in c.execute('SELECT * FROM equipment ORDER BY EquipementId'):
    print(row)

conn.close()
"""