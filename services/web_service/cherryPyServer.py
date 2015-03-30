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
        mytemplate = Template(filename='services/web_service/template/header.html')
        myothertemplate = Template(filename='services/web_service/template/index.html')
        maPage += (mytemplate.render())
        maPage += (myothertemplate.render())
        return maPage

    @cherrypy.expose
    def show_equipement(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_equipement?recherche=""&id=""
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'équipements sportif</h2>
                    <form name='monForm' action='show_equipement'>
                        Rechercher par
                        <select name='recherche'>
                            <option value='EquNom'> Nom Equipement
                            <option value='EquipementId'> ID Equipement
                            <option value='InsNumeroInstall'> ID Installation
                        </select>
                        :
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1' style='text-align'><th>Nom</th><th>ID Equipement</th><th>ID Installation</th><tr>"
            for row in c.execute("SELECT * FROM equipement WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage

    @cherrypy.expose
    def show_installation(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_installation?recherche=""&id=""
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'installations sportives</h2>
                    <form name='monForm' action='show_installation'>
                        Rechercher par 
                        <select name='recherche'>
                            <option value='Comlib'> Ville 
                            <option value='InsCodePostal'> Code Postale
                            <option value='InsLibelleVoie'> Adresse
                            <option value='InsNumeroInstall'> ID Installation 
                            <option value='InsPartLibelle'> Nom Installation
                            <option value='Latitude'> Latitude
                            <option value='Longitude'> Longitude
                        </select>
                        :
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1'><th>Ville</th><th>Code Postal</th><th>Adresse</th><th>ID Installation</th><th>Nom Installation</th><th>Latitude</th><th>Longitude</th><tr>"
            for row in c.execute("SELECT * FROM installation WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage

    @cherrypy.expose
    def show_activite(self, id, recherche):
        """
        Exposes the service at localhost:8080/show_activite?recherche=""&id=""
        """
        maPage = """<h1>Recherche d'installations sportives</h1>
                    <h2>Recheche d'activitées sportives</h2>
                    <form name='monForm' action='show_activite'>
                        Rechercher par
                        <select name='recherche'>
                            <option value='ActCode'>ID Activité
                            <option value='ActLib'> Nom Activité
                            <option value='EquipementId'> ID Equipement
                        </select>
                        :
                        <input type="text" name='id'>
                        <input type="submit">
                        <a href='index'>Retour</a>
                    </form>
                    """
        try:
            conn = sqlite3.connect("dataBase.db")
            c = conn.cursor()
            maPage +="<table border='1' style='text-align'><th>ID Activite</th><th>Nom Activite</th><th>ID Equipement</th><tr>"
            for row in c.execute("SELECT * FROM activite WHERE "+recherche+" LIKE \'%"+id+"%\'"):
                for elem in row:
                    maPage += "<td>" + str(elem) + "</td>"
                maPage += "</tr>"
            maPage += "</table>"
        except (IndexError, IOError):
            return "Invalid ID"

        return maPage


cherrypy.quickstart(WebManager())