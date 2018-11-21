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
#
#   - "/api/":
#       => Ein Interface um Daten anzufordern und zu verändern


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
        return self.application.get_dynamic_page("projektdaten", projekt_id_ODER_neu)


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id_ODER_neu = None):
        # Erreichbar unter:
        #   /kundendaten
        #   /kundendaten/<kunden_id>
        #   /kundendaten/neu
        return self.application.get_dynamic_page("kundendaten", kunden_id_ODER_neu)


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id_ODER_neu = None):
        # Erreichbar unter:
        #   /mitarbeiterdaten
        #   /mitarbeiterdaten/<mitarbeiter_id>
        #   /mitarbeiterdaten/neu
        return self.application.get_dynamic_page("mitarbeiterdaten", mitarbeiter_id_ODER_neu)


    # Seite mit allen nötigen Informationen (?)
    @cherrypy.expose
    def auswertung(self):
        # hier kommt noch die Auswertung hin, bis auf weiteres nur 500.html zum testen!
        return self.application.get_static_page("500")


    # API für alle Funktionen
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def api(self, function=None):
        # Erhaltene Daten (input_json) nach der Form:
        # {
        #   "link" : "<Kundendaten/Mitarbeiterdaten/Projektdaten>",
        #   "token" : "Access Token"
        #   -> je nachdem welche Funktion anders:
        #   "data" : ...
        # }
        #
        # Mögliche Seiten:
        #   /api/get        (zum bekommen von Daten, zum anzeigen auf Webseiten)
        #   /api/new        (zum Hinzufügen von neuen Daten)
        #   /api/update     (zum Updaten von bereits bestehenden Daten)
        #   /api/delete     (zum Löschen von bereits bestehenden Daten)

        # EINZIGER Try-Except Block im Server, sollte eigentlich NUR in der Application sein
        try:
            # War ein POST :)
            input_json = cherrypy.request.json

            # Alle Annahmen, dass übergebenes JSON richtig formattiert ist
            assert (
                (function != None) and
                ("link" in input_json and "token" in input_json and "data" in input_json) and
                input_json["link"] in ["Projektdaten", "Kundendaten", "Mitarbeiterdaten"] and
                input_json["token"] == "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad"
            )

            page = input_json["link"]

            if function == "get":
                return self.application.get_values(page)
            elif function == "new":
                return self.application.add_values(page, input_json["data"])
            elif function == "update":
                return self.application.update_values(page, input_json["data"])
            elif function == "delete":
                return self.application.delete_values(page, input_json["data"])
            else:
                print("Wrong API-Call")
                return '{"code" : 500}'
        except Exception as e:
            # War ein GET :(
            return self.application.get_static_page("404")


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
