import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/model")
from installation import *
import sqlite3


"""
	dataBase creation (if it exists, clear it)
"""
conn = sqlite3.connect('dataBase.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS installation")
c.execute('''CREATE TABLE installation
				( 	ComLib text,
					InsCodePostal text,
					InsLibelleVoie text,
					InsNumeroInstall text,
					InsPartLibelle text,
					Latitude text,
					Longitude text)''')
conn.commit()


"""
	Load JSON file
"""
installation = open('data/data_installation.json')
data_installation = json.load(installation)


"""
	Insert data into the dataBase
"""
for elem in data_installation["data"]:
	monInstallation = Installation(elem["ComLib"])
	monInstallation.setInsCodePostal(elem["InsCodePostal"])
	monInstallation.setInsLibelleVoie(elem["InsLibelleVoie"])
	monInstallation.setInsNumeroInstall(elem["InsNumeroInstall"])
	monInstallation.setInsPartLibelle(elem["InsPartLibelle"])
	monInstallation.setLatitude(elem["Latitude"])
	monInstallation.setLongitude(elem["Longitude"])
	
	values = [(	
				monInstallation.getComLib(),
				monInstallation.getInsCodePostal(),
				monInstallation.getInsLibelleVoie(),
				monInstallation.getInsNumeroInstall(),
				monInstallation.getInsPartLibelle(),
				monInstallation.getLatitude(),
				monInstallation.getLongitude() )]
	c.executemany('INSERT INTO installation VALUES (?,?,?,?,?,?,?)', values)
conn.commit()


"""
	Print the result
"""
"""
for row in c.execute('SELECT * FROM installation ORDER BY ComLib'):
	print(row)

conn.close()
"""