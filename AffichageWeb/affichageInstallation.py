import cherrypy
import json
import sqlite3
 
 
data = json.loads(open("data/data_installation.json").read())
 
 
class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		return "There are {0} items".format(len(data))
	 
	@cherrypy.expose
	def show_all(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn = sqlite3.connect("installation.db")
		c = conn.cursor()
		res="<table border='1'><th>Ville</th><th>Code Postal</th><th>Adresse</th><th>ID Installation</th><th>Nom Installation</th><th>Latitude</th><th>Longitude</th><tr>"
		for row in c.execute('SELECT * FROM installation ORDER BY InsCodePostal'):
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