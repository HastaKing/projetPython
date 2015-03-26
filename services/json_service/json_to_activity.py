import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/model")
from activity import *
import sqlite3


"""
	dataBase creation (if it exists, clear it)
"""
conn = sqlite3.connect('dataBase.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS activity")
c.execute('''CREATE TABLE activity
				(ActCode integer,
				ActLib text,
				EquipementId integer)''')
conn.commit()


"""
	Load JSON file
"""
activity = open('data/data_activity.json')
data_activity = json.load(activity)


"""
	Insert data into the dataBase
"""
for elem in data_activity["data"]:
	MyActivity = Activity(elem["EquipementId"])
	MyActivity.setActCode(elem["ActCode"])
	MyActivity.setActLib(elem["ActLib"])

	values = [(	MyActivity.getActCode(),
				MyActivity.getActLib(),
				MyActivity.getEquipementId() )]
	c.executemany('INSERT INTO activity VALUES (?,?,?)', values)
conn.commit()


"""
	Print the result
"""
"""
for row in c.execute('SELECT * FROM activity ORDER BY EquipementId'):
    print(row)

conn.close()
"""