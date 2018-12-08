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
        # /projektdaten | /projektdaten/<projekt_id> | /projektdaten/neu
        return self.application.get_dynamic_page("projektdaten", projekt_id_ODER_neu)


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id_ODER_neu = None):
        # /kundendaten | /kundendaten/<kunden_id> | /kundendaten/neu
        return self.application.get_dynamic_page("kundendaten", kunden_id_ODER_neu)


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id_ODER_neu = None):
        # /mitarbeiterdaten | /mitarbeiterdaten/<mitarbeiter_id> | /mitarbeiterdaten/neu
        return self.application.get_dynamic_page("mitarbeiterdaten", mitarbeiter_id_ODER_neu)


    # POST-Aktion zum Hinzufügen der Projektdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Projektdaten_Add(self, nummer=None, bezeichnung=None, beschreibung=None,
                                    bearbeitungszeitraum=None, budget=None,
                                    kunden_id=None, **kwargs):
        # Es muss ausserdem überprüft werden, ob es die Kunden-ID und Mitarbeiter-IDs auch gibt!!!
        # In **kwargs sind die Mitarbeiter-IDs und Zuordnung der Arbeit

        if cherrypy.request.method == "POST":
            # Hier wie in 1.2 mit der API auswerten
            return "Projekt hinzugefügt"
        return self.application.get_static_page("404")


    # POST-Aktion zum Bearbeiten der Projektdaten
    # fehlen noch die ganzen Parameter!
    @cherrypy.expose
    def POST_Projektdaten_Update(self, unique_id=None, nummer=None, bezeichnung=None,
                                    beschreibung=None, bearbeitungszeitraum=None,
                                    budget=None, kunden_id=None, **kwargs):
        # Es muss ausserdem überprüft werden, ob es die Kunden-ID und Mitarbeiter-IDs auch gibt!!!
        # In **kwargs sind die Mitarbeiter-IDs und Zuordnung der Arbeit

        if cherrypy.request.method == "POST":
            # Hier wie in 1.2 mit der API auswerten
            return "Projekt geupdatet"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG + löschbar
    # POST-Aktion zum Löschen der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion = ""#self.application.delete_values("Projektdaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
                return "Projektdaten-Löschung hat funktioniert"
            # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
            return "Projektdaten-Löschung hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Hinzufügen der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Add(self, nummer=None, bezeichnung=None, ansprechpartner=None, ort=None):
        if cherrypy.request.method == "POST" and nummer != None and bezeichnung != None and ansprechpartner != None and ort != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : 404,
                "nummer" : int(nummer),
                "bezeichnung" : bezeichnung,
                "ansprechpartner" : ansprechpartner,
                "ort" : ort
            }
            addition = self.application.add_values("Kundendaten", data)
            if addition == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
                return "Kundendaten-Hinzufügen hat funktioniert"
            # Seite zurückgeben die eigentlich nur history.back() macht
            return "Kundendaten-Hinzufügen hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Bearbeiten der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Update(self, unique_id=None, nummer=None, bezeichnung=None, ansprechpartner=None, ort=None):
        if cherrypy.request.method == "POST" and unique_id != None and nummer != None and bezeichnung != None and ansprechpartner != None and ort != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : int(unique_id),
                "nummer" : int(nummer),
                "bezeichnung" : bezeichnung,
                "ansprechpartner" : ansprechpartner,
                "ort" : ort
            }
            addition = self.application.update_values("Kundendaten", data)
            if addition == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
                return "Kundendaten-Updaten hat funktioniert"
            # Seite zurückgeben die eigentlich nur history.back() macht
            return "Kundendaten-Updaten hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Löschen der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion = self.application.delete_values("Kundendaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /kundendaten - Seite zurückgeht
                return "Kundendaten-Löschung hat funktioniert"
            # Seite zurückgeben die eigentlich nur zur /kundendaten - Seite zurückgeht
            return "Kundendaten-Löschung hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Hinzufügen der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Add(self, name=None, vorname=None, funktion=None):
        if cherrypy.request.method == "POST" and name != None and vorname != None and funktion != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : 404,
                "name" : name,
                "vorname" : vorname,
                "funktion" : funktion
            }
            addition = self.application.add_values("Mitarbeiterdaten", data)
            if addition == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
                return "Mitarbeiterdaten-Hinzufügen hat funktioniert"
            # Seite zurückgeben die eigentlich nur history.back() macht
            return "Mitarbeiterdaten-Hinzufügen hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Bearbeiten der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Update(self, unique_id=None, name=None, vorname=None, funktion=None):
        if cherrypy.request.method == "POST" and unique_id != None and name != None and vorname != None and funktion != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : int(unique_id),
                "name" : name,
                "vorname" : vorname,
                "funktion" : funktion
            }
            addition = self.application.update_values("Mitarbeiterdaten", data)
            if addition == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
                return "Mitarbeiterdaten-Updaten hat funktioniert"
            # Seite zurückgeben die eigentlich nur history.back() macht
            return "Mitarbeiterdaten-Updaten hat nicht funktioniert"
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Löschen der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion = self.application.delete_values("Mitarbeiterdaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
                return "Projektdaten-Löschung hat funktioniert"
            # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
            return "Mitarbeiterdaten-Löschung hat nicht funktioniert"
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
