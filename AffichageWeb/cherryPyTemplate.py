import cherrypy
import json
import sqlite3

from mako.template import Template
from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=[""])


class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        view = Template(filename="template.html", lookup=lookup)

        return view.render(
		rows=[[item["name"], item["age"]] for item in data]
	)

    @cherrypy.expose
    def show_equipement(self):
        """
        Exposes the service at localhost:8080/show_equipement/
        """
        conn = sqlite3.connect("dataBase.db")
        c = conn.cursor()
        res="<table border='1' style='text-align'><th>Nom</th><th>ID Equipement</th><th>ID Installation</th><tr>"
        for row in c.execute('SELECT * FROM equipement ORDER BY EquNom'):
            for elem in row:
                res = res + "<td>" + str(elem) + "</td>"
            res = res + "</tr>"
        res = res + "</table>"
        return res

    @cherrypy.expose
    def show_activite(self):
        """
        Exposes the service at localhost:8080/show_equipement/
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
    def show_installation(self):
        """
        Exposes the service at localhost:8080/show_equipement/
        """
        conn = sqlite3.connect("dataBase.db")
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