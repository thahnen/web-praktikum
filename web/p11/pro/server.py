#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Diese Datei ist für Aufgabe 1.1 um es einfacher zu gestalten & zu trennen!


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
import ast # um Liste als String in Liste zurückzuverwandeln
import cherrypy
import app


class WebServer(object):
    def __init__(self):
        self.server_path = os.path.dirname(os.path.abspath(__file__))
        self.application = app.Application(self.server_path)


    # Index-Seite des Webservers (führt zu allen wichtigen Seiten)
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


    # TODO: Noch alle Parameter auf Richtigkeit überprüfen?
    # POST-Aktion zum Hinzufügen der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Add(self, nummer=None, bezeichnung=None, beschreibung=None,
                                    bearbeitungszeitraum=None, budget=None,
                                    kunden_id=None, mitarbeiter_ids=None, **kwargs):

        if cherrypy.request.method == "POST" and nummer != None and \
                                            bezeichnung != None and beschreibung != None and \
                                            bearbeitungszeitraum != None and budget != None and \
                                            kunden_id != None and mitarbeiter_ids != None:
            # Hier wie in 1.2 mit der API auswerten
            try:
                mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
            except Exception as e:
                # Entweder falsch mit "," am Ende oder als Liste!
                # Annahme dass nur 0-9 + "," vorkommen, geht über Regex aber kb
                while mitarbeiter_ids[-1::] == ",":
                    mitarbeiter_ids = mitarbeiter_ids[:-1]
                    mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
                if mitarbeiter_ids[-1::] == "]":
                    mitarbeiter_ids = ast.literal_eval(mitarbeiter_ids)

            # Alles auf Richtigkeit überprüfen

            data = {
                "unique_id" : 404,
                "nummer" : int(nummer),
                "bezeichnung" : bezeichnung,
                "beschreibung" : beschreibung,
                "bearbeitungszeitraum" : int(bearbeitungszeitraum),
                "budget" : int(budget),
                "kunden_id" : int(kunden_id),
                "mitarbeiter_ids" : mitarbeiter_ids
            }

            # Überprüfen, ob "zuordnung_arbeit" in kwargs (dann wurde letzte Seite aufgerufen)
            if "unique_id" in kwargs and "zuordnung_arbeit" in kwargs:
                if '' in kwargs["zuordnung_arbeit"]:
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

                data["unique_id"] = int(kwargs["unique_id"])
                data["zuordnung_arbeit"] = kwargs["zuordnung_arbeit"]

                zuordnung_arbeit = {}
                be = int(bearbeitungszeitraum)

                for i in range(0, len(mitarbeiter_ids)):
                    zeiten = []
                    for j in range(0, be):
                        zeiten.append(int(data["zuordnung_arbeit"][(i*be)+j]))
                    zuordnung_arbeit.update({f"{mitarbeiter_ids[i]}" : zeiten})
                data.update({"zuordnung_arbeit" : zuordnung_arbeit})

                #return f"{data}"

                addition = self.application.add_values("Projektdaten", data)

                if addition == '{"code" : 200}':
                    # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
                # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            # Das Template muss noch hinzugefügt werden!
            return self.application.view.render_dynamic_page("zuordnung-arbeit-new", data)
        return self.application.get_static_page("404")


    # TODO: Noch alle Parameter auf Richtigkeit überprüfen?
    # POST-Aktion zum Bearbeiten der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Update(self, unique_id=None, nummer=None, bezeichnung=None,
                                    beschreibung=None, bearbeitungszeitraum=None,
                                    budget=None, kunden_id=None, mitarbeiter_ids=None, **kwargs):

        #return f"{unique_id}, {nummer}, {bezeichnung}, {beschreibung}, {bearbeitungszeitraum}, {budget}, {kunden_id}, {kwargs}"

        if cherrypy.request.method == "POST" and unique_id != None and nummer != None and \
                                            bezeichnung != None and beschreibung != None and \
                                            bearbeitungszeitraum != None and budget != None and \
                                            kunden_id != None and mitarbeiter_ids != None:
            # Hier wie in 1.2 mit der API auswerten
            try:
                mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
            except Exception as e:
                # Entweder falsch mit "," am Ende oder als Liste!
                # Annahme dass nur 0-9 + "," vorkommen, geht über Regex aber kb
                while mitarbeiter_ids[-1::] == ",":
                    mitarbeiter_ids = mitarbeiter_ids[:-1]
                    mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
                if mitarbeiter_ids[-1::] == "]":
                    mitarbeiter_ids = ast.literal_eval(mitarbeiter_ids)

            # Alles auf Richtigkeit überprüfen

            data = {
                "unique_id" : int(unique_id),
                "nummer" : int(nummer),
                "bezeichnung" : bezeichnung,
                "beschreibung" : beschreibung,
                "bearbeitungszeitraum" : int(bearbeitungszeitraum),
                "budget" : int(budget),
                "kunden_id" : int(kunden_id),
                "mitarbeiter_ids" : mitarbeiter_ids
            }

            try:
                zuordnung_arbeit = ast.literal_eval(kwargs["zuordnung_arbeit"])
            except Exception as e:
                data["zuordnung_arbeit"] = kwargs["zuordnung_arbeit"]

            if '' in kwargs["zuordnung_arbeit"]:
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            if "not_done" in kwargs:
                # Es muss noch Tabelle geupdatet werden!
                return self.application.view.render_dynamic_page("zuordnung-arbeit-edit", data)

            zuordnung_arbeit = {}
            be = int(bearbeitungszeitraum)

            for i in range(0, len(mitarbeiter_ids)):
                zeiten = []
                for j in range(0, be):
                    zeiten.append(int(data["zuordnung_arbeit"][(i*be)+j]))
                zuordnung_arbeit.update({f"{mitarbeiter_ids[i]}" : zeiten})
            data.update({"zuordnung_arbeit" : zuordnung_arbeit})

            addition = self.application.update_values("Projektdaten", data)

            if addition == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Löschen der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Delete(self, delete_unique_id=None):
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion = self.application.delete_values("Projektdaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur zur /projektdaten - Seite zurückgeht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Hinzufügen der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Add(self, nummer=None, bezeichnung=None, ansprechpartner=None, ort=None):
        if cherrypy.request.method == "POST" and nummer != None and \
                                            bezeichnung != None and \
                                            ansprechpartner != None and ort != None:
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur history.back() macht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Bearbeiten der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Update(self, unique_id=None, nummer=None, bezeichnung=None,
                                    ansprechpartner=None, ort=None):
        if cherrypy.request.method == "POST" and unique_id != None and nummer != None and \
                                            bezeichnung != None and \
                                            ansprechpartner != None and ort != None:
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur history.back() macht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur zur /kundendaten - Seite zurückgeht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Hinzufügen der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Add(self, name=None, vorname=None, funktion=None):
        if cherrypy.request.method == "POST" and name != None and \
                                            vorname != None and funktion != None:
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur history.back() macht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_static_page("404")


    # REVIEW: FERTIG
    # POST-Aktion zum Bearbeiten der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Update(self, unique_id=None, name=None, vorname=None, funktion=None):
        if cherrypy.request.method == "POST" and unique_id != None and name != None and \
                                            vorname != None and funktion != None:
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur history.back() macht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
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
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            # Seite zurückgeben die eigentlich nur zur /mitarbeiterdaten - Seite zurückgeht
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
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
