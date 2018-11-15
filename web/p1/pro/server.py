#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Diese Datei ist für Aufgabe 1.2 um es etwas einfacher zu gestalten & zu trennen!


#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#
#   Hinzufügen über Button, dann XMLHttpRequest
#   Bearbeiten über JavaScript-Auswahl, dann Button, dann XMLHttpRequest
#   Löschen über JavaScript-Auswahl, dann Button, dann XMLHttpRequest
#
#   - "/projektdaten":
#       => Seite mit allen Projektdaten
#   - "/projektdaten/<projekt_id>":
#       => Seite mit Angaben des Projekts der angegebenen Projekt-ID zum bearbeiten
#   - "/projektdaten/neu":
#       => Seite zum hinzufügen eines neuen Projekts
#
#   - "/kundendaten":
#       => Seite mit allen Kundendaten
#   - "/kundendaten/<kunden_id>":
#       => Seite mit Angaben des Kundens der angegebenen Kunden-ID zum bearbeiten
#   - "/kundendaten/neu":
#       => Seite zum hinzufügen eines neuen Kunden
#
#   - "/mitarbeiterdaten":
#       => Seite mit allen Mitarbeiterdaten
#   - "/mitarbeiterdaten/<mitarbeiter_id>":
#       => Seite mit Angaben des Mitarbeiters der angegebenen Mitarbeiter-ID zum bearbeiten
#   - "/mitarbeiterdaten/neu":
#       => Seite zum hinzufügen eines neuen Mitarbeiters
#
#   - "/auswertung":
#       => Eine Projektübersicht mit allen Informationen


import os
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


    # Seite mit allen Projektdaten
    @cherrypy.expose
    def projektdaten(self, projekt_id_ODER_neu = None):
        # Erreichbar unter:
        #   /projektdaten
        #   /projektdaten/<projekt_id>
        #   /projektdaten/neu
        if not projekt_id_ODER_neu:
            return self.application.get_dynamic_page("projektdaten")
        return self.application.get_dynamic_page_with_params("projektdaten", projekt_id_ODER_neu)


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id_ODER_neu = None):
        # Erreichbar unter:
        #   /kundendaten
        #   /kundendaten/<kunden_id>
        #   /kundendaten/neu
        if not kunden_id_ODER_neu:
            return self.application.get_dynamic_page("kundendaten")
        return self.application.get_dynamic_page_with_params("kundendaten", kunden_id_ODER_neu)


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id_ODER_neu = None):
        # Erreichbar unter:
        #   /mitarbeiterdaten
        #   /mitarbeiterdaten/<mitarbeiter_id>
        #   /mitarbeiterdaten/neu
        if not mitarbeiter_id_ODER_neu:
            return self.application.get_dynamic_page("mitarbeiterdaten")
        return self.application.get_dynamic_page_with_params("mitarbeiterdaten", mitarbeiter_id_ODER_neu)


    # Seite um Werte zu updaten bzw. neu hinzuzufügen
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def update(self):
        # Erhaltene Daten (input_json) nach der Form:
        # {
        #   "link" : "<Kundendaten/Mitarbeiterdaten/Projektdaten>",
        #   "method" : "<edit/new/delete>",
        #   1. wenn "delete":
        #   "data" : unique_id
        #   2. sonst:
        #   "data" : {
        #       [...] Eingegebene Daten nach dem jeweiligen Template [...]
        #   }
        # }

        try:
            # War ein POST :)
            input_json = cherrypy.request.json
            # Gibt auch Infos zurück, wenn Input fehlerhaft!
            return self.application.update_values(input_json)
        except Exception as e:
            # War ein GET :(
            return self.application.get_static_page("404")


    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        # hier kommt noch die Auswertung hin, bis auf weiteres nur 500.html zum testen!
        return self.application.get_static_page("500")


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
