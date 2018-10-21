#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import cherrypy
import app

# Dateipfad zum Hauptordner
server_path = os.path.dirname(os.path.abspath(__file__))

class WebServer(object):

    @cherrypy.expose
    def index(self):
        # irgendwie funktionieren die dort benutzen Dateien aber nicht!
        # irgendwie mit Konfigurationen arbeiten oder so -.-
        return open(server_path + "/content/index.html")

    @cherrypy.expose
    def projektdaten(self):
        return "Die Seite der Projektdaten"

    @cherrypy.expose
    def kundendaten(self):
        return "Die Seite der Kundendaten"

    @cherrypy.expose
    def mitarbeiterdaten(self):
        return "Die Seite der Mitarbeiterdaten"

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
