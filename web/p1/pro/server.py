#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Webserver mit Config und Routing:
#   ================================
#
#   1. Config ausgelagert in eigene Datei
#   TODO: auslagern!
#   => für statische Ordner und Dateien!
#   => noch genauere Konfigurationen vornehmen!
#
#   2. Routing:
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#   - "/projektdaten[?projekt_id=<xxx>]":
#       => Seite mit allen Projektdaten
#       => Bei Angabe einer Projekt-ID nur dieses anzeigen (ua. zum bearbeiten)
#   - "/kundendaten[?kunden_id=<yyy>]":
#       => Seite mit allen Kundendaten
#       => Bei Angabe einer Kunden-ID nur diesen anzeigen (ua. zum bearbeiten)
#       => WENN geändert müssen auch Projektdaten geändert werden?!
#   - "/mitarbeiterdaten[?mitarbeiter_id=<zzz>]":
#       => Seite mit allen Mitarbeiterdaten
#       => Bei Angabe einer Mitarbeiter-ID nur diesen anzeigen (ua. zum bearbeiten)
#       => WENN geändert müssen auch Projektdaten geändert werden?!
#   - "/auswertung":
#       => Eine Projektübersicht?

# TODO: ggf. User-Agent etc auswerten? Irgendwas mit den Daten machen (._.)

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
