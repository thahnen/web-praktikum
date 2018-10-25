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
    def __init__(self):
        self.application = app.Application(server_path)

    # Index-Seite (Landing-Page) des Webservers
    # => Listet alle Unterseiten auf?
    @cherrypy.expose
    def index(self):
        # return application.get_static_page("index")
        return open(server_path + "/content/index.html")

    # Seite mit allen Projektdaten
    @cherrypy.expose
    def projektdaten(self, projekt_id = 0):
        # return application.get_dynamic_page("projektdaten")
        return app.View.render_dynamic_page(
            "projektdaten.tpl", app.Database.read_json_into_dict("projektdaten.json")
        )

    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id = 0):
        # return application.get_dynamic_page("kundendaten")
        return app.View.render_dynamic_page(
            "kundendaten.tpl", app.Database.read_json_into_dict("kundendaten.json")
        )

    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id = 0):
        # return application.get_dynamic_page("mitarbeiterdaten")
        return app.View.render_dynamic_page(
            "mitarbeiterdaten.tpl", app.Database.read_json_into_dict("mitarbeiterdaten.json")
        )

    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        return "Die Seite mit den Auswertungen"

    # Seite um Werte zu updaten mit Hilfe XMLHTTPREQUEST statt POST aus Formular!
    @cherrypy.expose
    #@cherrypy.tools.json_out() # ohne es klappt aber Rückgabe als json nicht!
    @cherrypy.tools.json_in()
    def update(self):
        # Überprüfen ob GET oder POST von "/update" aufgerufen wurde!
        try:
            input_json = cherrypy.request.json
        except Exception as e:
            # Fehlerpage zurückgeben, die generiert wird
            return "<h1>404</h1><h2>Nicht gefunden</h2><h3>...du Otto</h3>"
        # return application.update_values(input_json)
        # funktioniert leider nicht, sonst wäre normale Rückgabe möglich!
        #cherrypy.response.headers["Content-Type"] = "application/json"
        return '{"json": "true"}'

# Auslagern in eigene Datei der Übersicht halber
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
