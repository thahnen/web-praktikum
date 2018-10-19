#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import cherrypy
from cherrypy.lib.static import serve_file
import app

# Dateipfad mit allen HTML/CSS/JS-Dateien
content_dir = os.path.dirname(os.path.abspath(__file__))+"/content/"

class WebServer(object):

    @cherrypy.expose
    def index(self):
        # irgendwie funktionieren die dort benutzen Dateien aber nicht!
        # irgendwie mit Konfigurationen arbeiten oder so -.-
        return serve_file(os.path.join(content_dir, "index.html"))

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

if __name__ == '__main__':
    cherrypy.quickstart(WebServer())
