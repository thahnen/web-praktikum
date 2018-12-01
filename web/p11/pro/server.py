#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Diese Datei ist für Aufgabe 1.1 um es etwas einfacher zu gestalten & zu trennen!


#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#
#   Hinzufügen über Link, dann POST-Formular
#   Bearbeiten über Link, dann POST-Formular
#   Löschen über POST-Formular
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
        return self.application.get_static_page("404")


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id_ODER_neu = None):
        # Erreichbar unter:
        #   /kundendaten
        #   /kundendaten/<kunden_id>
        #   /kundendaten/neu
        return self.application.get_static_page("404")


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id_ODER_neu = None):
        # Erreichbar unter:
        #   /mitarbeiterdaten
        #   /mitarbeiterdaten/<mitarbeiter_id>
        #   /mitarbeiterdaten/neu
        return self.application.get_static_page("404")


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
    def POST_Projektdaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
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
    def POST_Kundendaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
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
    def POST_Mitarbeiterdaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            return
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
