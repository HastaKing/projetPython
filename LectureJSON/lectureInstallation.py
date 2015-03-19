import json
import sys
sys.path.append("/hometu/etudiants/E134188G/Annee 2/Semestre 4/Complement Info/projetPython/modele")
from Installation import *
import sqlite3

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

installation = open('data/data_installation.json')
data_installation = json.load(installation)

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
	#print (monEquipement)

#print(json.dumps(jr, sort_keys=True, indent=4, separators=(',', ': ')))

conn.commit()

for row in c.execute('SELECT * FROM installation ORDER BY ComLib'):
	print(row)

conn.close()