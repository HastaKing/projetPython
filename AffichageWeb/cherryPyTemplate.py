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
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <br></br>
                    <a href='show_activite'>Table d'activités</a></br>
                    <a href='show_equipement'>Table d'equipements<a/></br>
                    <a href='show_installation'>Table d'installations<a/>
                    """
        return maPage

    @cherrypy.expose
    def show_equipement(self):
        """
        Exposes the service at localhost:8080/show_equipement/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'équipements sportif</h2>
                    <form name='monForm' action='show_equipement_id'>
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        return maPage

    @cherrypy.expose
    def show_activite(self):
        """
        Exposes the service at localhost:8080/show_equipement/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'équipements sportif</h2>
                    <form name='monForm' action='show_activite_id'>
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        return maPage

    @cherrypy.expose
    def show_installation(self):
        """
        Exposes the service at localhost:8080/show_equipement/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'équipements sportif</h2>
                    <form name='monForm' action='show_installation_id'>
                        <input type="text" name='id'>
                        <input type="submit" id='submit'>
                        <a href='index'>Retour</a>
                    </form>
                    """
        return maPage

    @cherrypy.expose
    def show_equipement_id(self, id):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'équipements sportif</h2>
                    <form name='monForm' action='show_equipement_id'>
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1' style='text-align'><th>Nom</th><th>ID Equipement</th><th>ID Installation</th><tr>"
            for row in c.execute("SELECT * FROM equipement WHERE EquipementId LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage

    @cherrypy.expose
    def show_installation_id(self, id):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'installations sportives</h2>
                    <form name='monForm' action='show_installation_id'>
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1' style='text-align'><th>Nom</th><th>ID Equipement</th><th>ID Installation</th><tr>"
            for row in c.execute("SELECT * FROM equipement WHERE InsNumeroInstall LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage

    @cherrypy.expose
    def show_activite_id(self, id):
        """
        Exposes the service at localhost:8080/show_activite_id/[id]/
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'activitées sportives</h2>
                    <form name='monForm' action='show_activite_id'>
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1' style='text-align'><th>ID Activite</th><th>Nom Activite</th><th>ID Equipement</th><tr>"
            for row in c.execute("SELECT * FROM activite WHERE ActCode LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage


cherrypy.quickstart(WebManager())