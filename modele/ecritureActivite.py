import sqlite3

conn = sqlite3.connect('activite.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS activite")
c.execute('''CREATE TABLE activite
				(ActCode text,
				ActLib text,
				ActNivLib text,
				ComInsee text,
				ComLib text,
				EquActivitePraticable text,
				EquActivitePratique text,
				EquActiviteSalleSpe text,
				EquNbEquIdentique text,
				EquipementId text)''')

conn.commit()
conn.close()