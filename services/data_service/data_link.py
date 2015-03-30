import sqlite3

conn = sqlite3.connect('dataBase.db')
c = conn.cursor()
c.execute("""	SELECT i.InsNumeroInstall, e.EquipementId, a.EquipementId
			    FROM installation i
			        JOIN equipment e ON i.InsNumeroInstall = e.InsNumeroInstall
			        JOIN activity a ON e.EquipementId = a.EquipementId""")
conn.commit()