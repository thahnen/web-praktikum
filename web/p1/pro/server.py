#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Webserver mit Config und Routing:
#   ================================
#
#   1. Routing:
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#   - "/projektdaten[?projekt_id=<xxx>]":
#       => Seite mit allen Projektdaten (und neues hinzufügen)
#       => Bei Angabe einer Projekt-ID nur dieses anzeigen (ua. zum bearbeiten)
#   - "/kundendaten[?kunden_id=<yyy>]":
#       => Seite mit allen Kundendaten (und neues hinzufügen)
#       => Bei Angabe einer Kunden-ID nur diesen anzeigen (ua. zum bearbeiten)
#       => WENN geändert müssen auch Projektdaten geändert werden?!
#   - "/mitarbeiterdaten[?mitarbeiter_id=<zzz>]":
#       => Seite mit allen Mitarbeiterdaten (und neues hinzufügen)
#       => Bei Angabe einer Mitarbeiter-ID nur diesen anzeigen (ua. zum bearbeiten)
#       => WENN geändert müssen auch Projektdaten geändert werden?!
#   - "/auswertung":
#       => Eine Projektübersicht?

# TODO: ggf. User-Agent etc auswerten? Irgendwas mit den Daten machen (._.)


import os
import os.path
import cherrypy
import app


class WebServer(object):
    def __init__(self):
        self.server_path = os.path.dirname(os.path.abspath(__file__))
        self.application = app.Application(self.server_path)


    # Index-Seite des Webservers (Liste aller Unterseiten oder so)
    @cherrypy.expose
    def index(self):
        return self.application.get_static_page("index")


    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        return "Die Seite mit den Auswertungen"


    # Seite mit allen Projektdaten
    @cherrypy.expose
    def projektdaten(self, projekt_id = None):
        # Beinhaltet sowohl:  /projektdaten/<projekt_id>
        #           als auch: /projektdaten?projekt_id=<projekt_id>
        if not projekt_id:
            return self.application.get_dynamic_page("projektdaten")
        return self.application.get_dynamic_page_with_params("projektdaten", projekt_id)


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id = None):
        # Beinhaltet sowohl:  /kundendaten/<kunden_id>
        #           als auch: /kundendaten?kunden_id=<kunden_id>
        if not kunden_id:
            return self.application.get_dynamic_page("kundendaten")
        return self.application.get_dynamic_page_with_params("kundendaten", kunden_id)


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id = None):
        # Beinhaltet sowohl:  /mitarbeiterdaten/<mitarbeiter_id>
        #           als auch: /mitarbeiterdaten?mitarbeiter_id=<mitarbeiter_id>
        if not mitarbeiter_id:
            return self.application.get_dynamic_page("mitarbeiterdaten")
        return self.application.get_dynamic_page_with_params("mitarbeiterdaten", mitarbeiter_id)


    # Seite um Werte zu updaten mit Hilfe XMLHttpRequest statt POST aus Formular!
    # curl -H "Content-Type: application/json" --request POST -d '{"test" : 1234}' 127.0.0.1:8080/update
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def update(self):
        # Erhaltene Daten nach der Form:
        # {
        #   "link" : "<Kundendaten/Mitarbeiterdaten/Projektdaten>",
        #   "method" : "<edit/new>",
        #   "data" {
        #       [...] Eingegebene Daten nach dem jeweiligen Template [...]
        #   }
        # }

        try:
            # War ein POST :)
            input_json = cherrypy.request.json
        except Exception as e:
            # War ein GET :(
            return self.application.get_static_page("404")
        return self.application.update_values(input_json)


config = {
    "/" : {
        "tools.staticdir.root" : os.path.dirname(os.path.abspath(__file__))
    },
    "/css" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/css/"
    },
    "/js" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/js/"
    }
}


if __name__ == '__main__':
    cherrypy.quickstart(WebServer(), "/", config=config)
