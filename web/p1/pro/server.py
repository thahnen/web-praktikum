#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#       => Verlinkungen auf unterschiedliche Seiten für Aufgabe 1 und 2 !!!
#
#   AUFGABE 1:
#   Hinzufügen über Link, dann POST-Formular
#   Bearbeiten über Link, dann POST-Formular
#   Löschen über POST-Formular
#
#   - "/projektdaten_1":
#   - "/projektdaten_1/<projekt_id>":
#   - "/projektdaten_1/neu":
#       => siehe AUFGABE 2
#
#   - "/kundendaten_1":
#   - "/kundendaten_1/<kunden_id>":
#   - "/kundendaten_1/neu":
#       => siehe AUFGABE 2
#
#   - "/mitarbeiterdaten_1":
#   - "/mitarbeiterdaten_1/<mitarbeiter_id>":
#   - "/mitarbeiterdaten_1/neu":
#       => siehe AUFGABE 2
#
#   - "/POST_Projektdaten_Add":
#   - "/POST_Projektdaten_Update":
#   - "/POST_Projektdaten_Delete":
#       => Jeweilige POST-Aktion für die Projektdaten
#
#   - "/POST_Kundendaten_Add":
#   - "/POST_Kundendaten_Update":
#   - "/POST_Kundendaten_Delete":
#       => Jeweilige POST-Aktion für die Kundendaten
#
#   - "/POST_Mitarbeiterdaten_Add":
#   - "/POST_Mitarbeiterdaten_Update":
#   - "/POST_Mitarbeiterdaten_Delete":
#       => Jeweilige POST-Aktion für die Mitarbeiterdaten
#
#
#   AUFGABE 2:
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
#   - "/kundendaten/<projekt_id>":
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


    #############################################################################
    #                                                                           #
    #                               AUFGABE 1                                   #
    #                                                                           #
    #############################################################################

    # Seite mit allen Projektdaten
    @cherrypy.expose
    def projektdaten_1(self, projekt_id_ODER_neu = None):
        # Erreichbar unter:
        #   /projektdaten_1
        #   /projektdaten_1/<projekt_id>
        #   /projektdaten_1/neu
        return "404"


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten_1(self, kunden_id_ODER_neu = None):
        # Erreichbar unter:
        #   /kundendaten_1
        #   /kundendaten_1/<kunden_id>
        #   /kundendaten_1/neu
        return "404"


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten_1(self, mitarbeiter_id_ODER_neu = None):
        # Erreichbar unter:
        #   /mitarbeiterdaten_1
        #   /mitarbeiterdaten_1/<mitarbeiter_id>
        #   /mitarbeiterdaten_1/neu
        return "404"


    # POST-Aktion zum Hinzufügen der Projektdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Projektdaten_Add(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Bearbeiten der Projektdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Projektdaten_Update(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Löschen der Projektdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Projektdaten_Delete(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Hinzufügen der Kundendaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Kundendaten_Add(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Bearbeiten der Kundendaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Kundendaten_Update(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Löschen der Kundendaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Kundendaten_Delete(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Hinzufügen der Mitarbeiterdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Add(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Bearbeiten der Mitarbeiterdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Update(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    # POST-Aktion zum Löschen der Mitarbeiterdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Delete(self):
        if cherrypy.request.method == "POST":
            return
        return self.application.get_static_page("404")


    #############################################################################
    #                                                                           #
    #                               AUFGABE 2                                   #
    #                                                                           #
    #############################################################################

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
            return self.application.update_values(input_json)
        except Exception as e:
            # War ein GET oder Input war fehlerhaft!
            return self.application.get_static_page("404")


    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        return "Die Seite mit den Auswertungen"


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
