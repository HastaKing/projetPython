import cherrypy
import json
import sqlite3
from mako.template import Template


class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        maPage = ""
        mytemplate1 = Template(filename='services/web_service/template/header.html')
        mytemplate2 = Template(filename='services/web_service/template/index.html')
        mytemplate3 = Template(filename='services/web_service/template/footer.html')
        maPage += (mytemplate1.render())
        maPage += (mytemplate2.render())
        maPage += (mytemplate3.render())
        return maPage

    @cherrypy.expose
    def show_equipment(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_equipment?recherche=""&id=""
        """
        maPage = ""
        mytemplate1 = Template(filename='services/web_service/template/header.html')
        mytemplate2 = Template(filename='services/web_service/template/equipment.html')
        mytemplate3 = Template(filename='services/web_service/template/footer.html')
        maPage += (mytemplate1.render())
        maPage += (mytemplate2.render())
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table class=\"table-striped\"><th>Nom</th><th>ID Equipement</th><th>ID Installation</th><tr>"
            for row in c.execute("SELECT * FROM equipement WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"
        maPage += (mytemplate3.render())

        return maPage

    @cherrypy.expose
    def show_installation(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_installation?recherche=""&id=""
        """
        maPage = ""
        mytemplate1 = Template(filename='services/web_service/template/header.html')
        mytemplate2 = Template(filename='services/web_service/template/installation.html')
        mytemplate3 = Template(filename='services/web_service/template/footer.html')
        maPage += (mytemplate1.render())
        maPage += (mytemplate2.render())
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table><th>Ville</th><th>Code Postal</th><th>Adresse</th><th>ID Installation</th><th>Nom Installation</th><th>Latitude</th><th>Longitude</th><tr>"
            for row in c.execute("SELECT * FROM installation WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"
        maPage += (mytemplate3.render())

        return maPage

    @cherrypy.expose
    def show_activity(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_activity?recherche=""&id=""
        """
        maPage = ""
        mytemplate1 = Template(filename='services/web_service/template/header.html')
        mytemplate2 = Template(filename='services/web_service/template/activity.html')
        mytemplate3 = Template(filename='services/web_service/template/footer.html')
        maPage += (mytemplate1.render())
        maPage += (mytemplate2.render())
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table><th>ID Activite</th><th>Nom Activite</th><th>ID Equipement</th><tr>"
            for row in c.execute("SELECT * FROM activite WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"
        maPage += (mytemplate3.render())

        return maPage


cherrypy.quickstart(WebManager())