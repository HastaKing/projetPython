import cherrypy
import json
import sqlite3
 
 
data = json.loads(open("data/data_activite.json").read())
 
 
class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		conn = sqlite3.connect("dataBase.db")
		c = conn.cursor()
		return "There are {0} items".format(len(c.execute('SELECT * FROM activite ORDER BY ActLib')))
	 
	@cherrypy.expose
	def show_all(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn = sqlite3.connect("dataBase.db")
		c = conn.cursor()
		res="<table border='1' style='text-align'><th>Nom</th><th>ID Activite</th><th>ID Equipement</th><tr>"
		for row in c.execute('SELECT * FROM activite ORDER BY ActLib'):
			for elem in row:
				res = res + "<td>" + str(elem) + "</td>"
			res = res + "</tr>"
		res = res + "</table>"
		return res
	 
	@cherrypy.expose
	def show(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			item = data[int(id)]
		except (IndexError, IOError):
			return "Invalid ID"
		 
		return json.dumps(item)
 
 
cherrypy.quickstart(WebManager()) 