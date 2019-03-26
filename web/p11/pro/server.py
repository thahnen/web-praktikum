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
import ast
import cherrypy
import app


class WebServer(object):
    def __init__(self):
        self.server_path :str = os.path.dirname(os.path.abspath(__file__))
        self.application = app.Application(self.server_path)


    # Index-Seite des Webservers (führt zu allen wichtigen Seiten)
    @cherrypy.expose
    def index(self) -> str:
        return self.application.get_static_page("index")


    # Seite mit allen Projektdaten
    @cherrypy.expose
    def projektdaten(self, projekt_id_ODER_neu :str = None) -> str:
        # /projektdaten | /projektdaten/<projekt_id> | /projektdaten/neu
        return self.application.get_dynamic_page("projektdaten", projekt_id_ODER_neu)


    # Seite mit allen Kundendaten
    @cherrypy.expose
    def kundendaten(self, kunden_id_ODER_neu :str = None) -> str:
        # /kundendaten | /kundendaten/<kunden_id> | /kundendaten/neu
        return self.application.get_dynamic_page("kundendaten", kunden_id_ODER_neu)


    # Seite mit allen Mitarbeiterdaten
    @cherrypy.expose
    def mitarbeiterdaten(self, mitarbeiter_id_ODER_neu :str = None) -> str:
        # /mitarbeiterdaten | /mitarbeiterdaten/<mitarbeiter_id> | /mitarbeiterdaten/neu
        return self.application.get_dynamic_page("mitarbeiterdaten", mitarbeiter_id_ODER_neu)


    # POST-Aktion zum Hinzufügen der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Add(self, nummer :int = None, bezeichnung :str = None, beschreibung :str = None,
                                    bearbeitungszeitraum :str = None, budget :float = None,
                                    kunden_id :int = None, mitarbeiter_ids :str = None, **kwargs) -> str:

        if cherrypy.request.method == "POST" and nummer != None and \
                                            bezeichnung != None and beschreibung != None and \
                                            bearbeitungszeitraum != None and budget != None and \
                                            kunden_id != None and mitarbeiter_ids != None:
            # Hier wie in 1.2 mit der API auswerten

            # GGf "," am Ende!
            while mitarbeiter_ids[-1::] == ",":
                mitarbeiter_ids = mitarbeiter_ids[:-1]

            try:
                mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
            except Exception:
                # Annahme dass nur 0-9 + "," vorkommen, geht über Regex aber kb
                if mitarbeiter_ids[-1::] == "]":
                    mitarbeiter_ids = ast.literal_eval(mitarbeiter_ids)
                else:
                    mitarbeiter_ids = list(mitarbeiter_ids)

            # Alles auf Richtigkeit überprüfen
            for mid in mitarbeiter_ids:
                try:
                    # das hier anders loesen!
                    x = int(mid)
                except Exception:
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

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


            # Überprüfen, ob die kunden_id und alle mitarbeiter_ids überhaupt existieren!
            alle_kunden = self.application.database.read_json_into_dict("kundendaten.json")
            alle_mitarbeiter = self.application.database.read_json_into_dict("mitarbeiterdaten.json")

            gefunden_k :bool = False
            for elem in alle_kunden["Elements"]:
                if alle_kunden["Elements"][elem]["unique_id"] == data["kunden_id"]:
                    gefunden_k = True
                    break

            if not gefunden_k:
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            for mid in data["mitarbeiter_ids"]:
                gefunden_m = False
                for elem in alle_mitarbeiter["Elements"]:
                    if alle_mitarbeiter["Elements"][elem]["unique_id"] == mid:
                        gefunden_m = True
                        break
                if not gefunden_m:
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            # Überprüfen, ob "zuordnung_arbeit" in kwargs (dann wurde letzte Seite aufgerufen)
            if "unique_id" in kwargs and "zuordnung_arbeit" in kwargs:
                for zu in kwargs["zuordnung_arbeit"]:
                    try:
                        # das hier anders loesen!
                        x = int(zu)
                    except Exception:
                        return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

                data["unique_id"] = int(kwargs["unique_id"])
                data["zuordnung_arbeit"] = kwargs["zuordnung_arbeit"]

                zuordnung_arbeit = {}
                be :int = int(bearbeitungszeitraum)

                for i in range(0, len(mitarbeiter_ids)):
                    zeiten = []
                    for j in range(0, be):
                        zeiten.append(int(data["zuordnung_arbeit"][(i*be)+j]))
                    zuordnung_arbeit.update({f"{mitarbeiter_ids[i]}" : zeiten})
                data.update({"zuordnung_arbeit" : zuordnung_arbeit})

                addition :str = self.application.add_values("Projektdaten", data)
                if addition == '{"code" : 200}':
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            return self.application.view.render_dynamic_page("zuordnung-arbeit-new", data)
        return self.application.get_dynamic_page("projektdaten", None)


    # POST-Aktion zum Bearbeiten der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Update(self, unique_id :int = None, nummer :int = None, bezeichnung :str= None,
                                    beschreibung :str = None, bearbeitungszeitraum :str = None,
                                    budget :float = None, kunden_id :int = None, mitarbeiter_ids = None, **kwargs) -> str:

        if cherrypy.request.method == "POST" and unique_id != None and nummer != None and \
                                            bezeichnung != None and beschreibung != None and \
                                            bearbeitungszeitraum != None and budget != None and \
                                            kunden_id != None and mitarbeiter_ids != None:
            # Hier wie in 1.2 mit der API auswerten

            # GGf "," am Ende!
            while mitarbeiter_ids[-1::] == ",":
                mitarbeiter_ids = mitarbeiter_ids[:-1]

            try:
                mitarbeiter_ids = list(map(lambda x: int(x), mitarbeiter_ids.split(",")))
            except Exception:
                # Annahme dass nur 0-9 + "," vorkommen, geht über Regex aber kb
                if mitarbeiter_ids[-1::] == "]":
                    mitarbeiter_ids = ast.literal_eval(mitarbeiter_ids)
                else:
                    mitarbeiter_ids = list(mitarbeiter_ids)

            # Alles auf Richtigkeit überprüfen
            for mid in mitarbeiter_ids:
                try:
                    # das hier anders loesen!
                    x = int(mid)
                except Exception:
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

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

            # Überprüfen, ob die kunden_id und alle mitarbeiter_ids überhaupt existieren!
            alle_kunden = self.application.database.read_json_into_dict("kundendaten.json")
            alle_mitarbeiter = self.application.database.read_json_into_dict("mitarbeiterdaten.json")

            gefunden_k :bool = False
            for elem in alle_kunden["Elements"]:
                if alle_kunden["Elements"][elem]["unique_id"] == data["kunden_id"]:
                    gefunden_k = True
                    break

            if not gefunden_k:
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            for mid in data["mitarbeiter_ids"]:
                gefunden_m = False
                for elem in alle_mitarbeiter["Elements"]:
                    if alle_mitarbeiter["Elements"][elem]["unique_id"] == mid:
                        gefunden_m = True
                        break
                if not gefunden_m:
                    return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            if type(kwargs["zuordnung_arbeit"]) == str:
                zuordnung_arbeit = ast.literal_eval(kwargs["zuordnung_arbeit"])
                data["zuordnung_arbeit"] = zuordnung_arbeit
            elif type(kwargs["zuordnung_arbeit"]) == list:
                zuordnung_arbeit = kwargs["zuordnung_arbeit"]
                data["zuordnung_arbeit"] = zuordnung_arbeit
            else:
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})

            for zu in zuordnung_arbeit:
                try:
                    # das hier anders loesen!
                    x = int(zu)
                except Exception:
                    # Die alte Zuordnung ist als Element noch in der Liste
                    del zuordnung_arbeit[zuordnung_arbeit.index(zu)]
                    data["zuordnung_arbeit"] = zuordnung_arbeit

            if "not_done" in kwargs:
                # Es muss noch Tabelle geupdatet werden!
                return self.application.view.render_dynamic_page("zuordnung-arbeit-edit", data)

            zuordnung_arbeit = {}
            be :int = int(bearbeitungszeitraum)

            for i in range(0, len(mitarbeiter_ids)):
                zeiten = []
                for j in range(0, be):
                    zeiten.append(int(data["zuordnung_arbeit"][(i*be)+j]))
                zuordnung_arbeit.update({f"{mitarbeiter_ids[i]}" : zeiten})
            data.update({"zuordnung_arbeit" : zuordnung_arbeit})

            addition :str = self.application.update_values("Projektdaten", data)

            if addition == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("projektdaten", None)


    # POST-Aktion zum Löschen der Projektdaten
    @cherrypy.expose
    def POST_Projektdaten_Delete(self, delete_unique_id :int = None) -> str:
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion :str = self.application.delete_values("Projektdaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("projektdaten", None)


    # POST-Aktion zum Hinzufügen der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Add(self, nummer :int = None, bezeichnung :str = None, ansprechpartner :str = None, ort :str = None) -> str:
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

            addition :str = self.application.add_values("Kundendaten", data)
            if addition == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("kundendaten", None)


    # POST-Aktion zum Bearbeiten der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Update(self, unique_id :int = None, nummer :int = None, bezeichnung :str = None,
                                    ansprechpartner :str = None, ort :str = None) -> str:
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

            addition :str = self.application.update_values("Kundendaten", data)
            if addition == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("kundendaten", None)


    # POST-Aktion zum Löschen der Kundendaten
    @cherrypy.expose
    def POST_Kundendaten_Delete(self, delete_unique_id :int = None) -> str:
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion :str = self.application.delete_values("Kundendaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("kundendaten", None)


    # POST-Aktion zum Hinzufügen der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Add(self, name :str = None, vorname :str = None, funktion :str = None) -> str:
        if cherrypy.request.method == "POST" and name != None and \
                                            vorname != None and funktion != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : 404,
                "name" : name,
                "vorname" : vorname,
                "funktion" : funktion
            }

            addition :str = self.application.add_values("Mitarbeiterdaten", data)
            if addition == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("mitarbeiterdaten", None)


    # POST-Aktion zum Bearbeiten der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Update(self, unique_id :int = None, name :str = None, vorname :str = None, funktion :str = None) -> str:
        if cherrypy.request.method == "POST" and unique_id != None and name != None and \
                                            vorname != None and funktion != None:
            # Hier wie in 1.2 mit der API auswerten
            data = {
                "unique_id" : int(unique_id),
                "name" : name,
                "vorname" : vorname,
                "funktion" : funktion
            }

            addition :str = self.application.update_values("Mitarbeiterdaten", data)
            if addition == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("mitarbeiterdaten", None)


    # POST-Aktion zum Löschen der Mitarbeiterdaten
    @cherrypy.expose
    def POST_Mitarbeiterdaten_Delete(self, delete_unique_id :int = None) -> str:
        if cherrypy.request.method == "POST" and delete_unique_id != None:
            # Hier wie in 1.2 mit der API auswerten
            deletion :str = self.application.delete_values("Mitarbeiterdaten", int(delete_unique_id))
            if deletion == '{"code" : 200}':
                return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":True})
            return self.application.view.render_dynamic_page("funktion-erfolgreich", {"erfolgreich":False})
        return self.application.get_dynamic_page("mitarbeiterdaten", None)


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
