#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import cherrypy
import app

# Dateipfad zum Hauptordner
if os.name != "posix":
    raise Exception("Nicht unter Unix ausgeführt!")
server_path = os.path.dirname(os.path.abspath(__file__))

class WebServer(object):
    # Index-Seite (Landing-Page) des Webservers
    # => Listet alle Unterseiten auf?
    @cherrypy.expose
    def index(self):
        return open(server_path + "/content/index.html")

    # Seite mit allen Projektdaten
    # => bei Angabe der eindeutigen Projekt-ID wird dieses aufgelistet!
    @cherrypy.expose
    def projektdaten(self, projekt_id = 0):
        return "Die Seite der Projektdaten"

    # Seite mit allen Kundendaten
    # => bei Angabe der eindeutigen Kunden-ID wird nur dieser aufgelistet!
    @cherrypy.expose
    def kundendaten(self, kunden_id = 0):
        return app.View.render_page(
            "kundendaten.tpl", app.Database.read_json_into_dict("kundendaten.json")
        )

    # Seite mit allen Mitarbeiterdaten
    # => bei Angabe der eindeutigen Mitarbeiter-ID wird nur dieser aufgelistet!
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id = 0):
        return "Die Seite der Mitarbeiterdaten"

    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        return "Die Seite mit den Auswertungen"

config = {
    "/" : {
        "tools.staticdir.root" : server_path
    },
    "/css" : {
        "tools.staticdir.on" : True,
        # Eine Index-Datei für das Verzeichnis
        # "tools.staticdir.index" : "index.html",
        "tools.staticdir.dir" : "./content/css/"
    },
    "/js" : {
        "tools.staticdir.on" : True,
        # Eine Index-Datei für das Verzeichnis
        # "tools.staticdir.index" : "index.html",
        "tools.staticdir.dir" : "./content/js/"
    }
}

if __name__ == '__main__':
    cherrypy.quickstart(WebServer(), "/", config=config)
