#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien


import json
import app.database
import app.view


class Application(object):
    def __init__(self, server_path :str):
        self.server_path :str = server_path
        self.content_path :str = self.server_path + "/content/"
        self.database = app.Database(server_path + "/data/")
        self.view = app.View(server_path + "/template/")


    # Handhabt statische Seiten
    def get_static_page(self, pagename :str) -> str:
        try:
            return self.view.render_static_page(self.content_path + pagename + ".html")
        except Exception:
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt alle dynamischen Seiten (mit oder ohne Parametern)
    def get_dynamic_page(self, pagename :str, parameter=None) -> str:
        try:
            data = self.database.read_json_into_dict(pagename + ".json")

            if parameter == None:
                return self.view.render_dynamic_page(pagename, data)
            elif parameter == "neu":
                return self.view.render_dynamic_page(pagename + "-new", data)

            found :bool = False
            for elem in data["Elements"]:
                if int(data["Elements"][elem]["unique_id"]) == int(parameter):
                    # Alles andere Löschen, damit nur noch das eine übrig bleibt!
                    data["Data"] = data["Elements"][elem]
                    del data["Elements"]
                    found = True
                    break

            if found:
                return self.view.render_dynamic_page(pagename + "-edit", data)
            return self.get_static_page("404")
        except Exception:
            return self.get_static_page("500")


    # Handhabt sortierte Auswertung
    def get_sorted_evaluation(self) -> str:
        # Alle Projekte laden (Template braucht keiner) und Indizes konvertieren (String -> Int)
        projects = self.database.read_json_into_dict("Projektdaten.json")["Elements"]
        projects = {int(k):v for k,v in projects.items()}
        # Projekte nach (Bezeichnung) sortieren (kv[1] um Value aus Key-Value-Paar zu erhalten)
        projects = dict(sorted(projects.items(), key=lambda kv: kv[1]["bezeichnung"]))

        # Alle Kunden laden (Template braucht keiner) und Indizes konvertieren (String -> Int)
        kunden = self.database.read_json_into_dict("Kundendaten.json")["Elements"]
        kunden = {int(k):v for k,v in kunden.items()}

        # Alle Mitarbeiter laden (Template braucht keiner) und Indizes konvertieren (String -> Int)
        arbeiter = self.database.read_json_into_dict("Mitarbeiterdaten.json")["Elements"]
        arbeiter = {int(k):v for k,v in arbeiter.items()}

        # Bei allen Projekten:
        # 1) kunden_id durch Dictionary mit Kunden-Information ersetzen
        #   "kunden_id" : <kunden_id>
        #
        #   "kunden_id" : {
        #       "unique_id" : <unique_id>,
        #       "nummer" : <nummer>,                        -> nicht unbedingt benötigt
        #       "bezeichnung" : <bezeichnung>,
        #       "ansprechpartner" : <ansprechpartner>,
        #       "ort" : <ort>                               -> nicht unbedingt benötigt
        #   }
        #
        # 2) mitarbeiter_ids durch Liste mit Dictionaries mit Mitarbeiter-Informationen ersetzen
        #   "mitarbeiter_ids" : [ 1..n <mitarbeiter_id> ]
        #
        #   "mitarbeiter_ids" : [
        #       1..n {
        #               "unique_id" : <unique_id>,
        #               "name" : <name>,
        #               "vorname" : <vorname>,
        #               "funktion" : <funktion>             -> nicht unbedingt benötigt
        #           }
        #   ]
        #
        # 3) zuordnung_arbeit mit gesamter Wochenstundenanzahl erweitern
        #   "zuordnung_arbeit" : { ... }
        #
        #   "zuordnung_arbeit" : {
        #       "gesamt_anzahl" : <gesamt_anzahl>,
        #       "gesamt_woche_n" : [...],
        #       ...
        #   }

        for pro in projects:
            # Kunde ersetzen
            kunden_id :int = projects[pro]["kunden_id"]
            for kun in kunden:
                if int(kunden[kun]["unique_id"]) == int(kunden_id):
                    projects[pro]["kunden_id"] = kunden[kun]
                    break

            # Mitarbeiter ersetzen + sortieren
            mitarbeiter_ids = projects[pro]["mitarbeiter_ids"]
            for m_id in mitarbeiter_ids:
                for arb in arbeiter:
                    if int(arbeiter[arb]["unique_id"]) == int(m_id):
                        projects[pro]["mitarbeiter_ids"][projects[pro]["mitarbeiter_ids"].index(m_id)] = arbeiter[arb]
                        break
            projects[pro]["mitarbeiter_ids"] = sorted(
                projects[pro]["mitarbeiter_ids"],
                key=lambda elem: (elem["name"], elem["vorname"])
            )

            # Zuordnung erweitern
            zuordnung_arbeit = projects[pro]["zuordnung_arbeit"]
            gesamt_woche_n = [0] * projects[pro]["bearbeitungszeitraum"]
            gesamt_anzahl :int = 0
            for zuo in zuordnung_arbeit:
                for stunden in zuordnung_arbeit[zuo]:
                    gesamt_anzahl += int(stunden)
            for zuo in zuordnung_arbeit:
                for i in range(len(zuordnung_arbeit[zuo])):
                    gesamt_woche_n[i] += zuordnung_arbeit[zuo][i]
            projects[pro]["zuordnung_arbeit"]["gesamt_woche_n"] = gesamt_woche_n
            projects[pro]["zuordnung_arbeit"]["gesamt_anzahl"] = gesamt_anzahl

        try:
            return self.view.render_dynamic_page("auswertung", projects)
        except Exception:
            return self.get_static_page("500")


    # Handhabt Rückgabe der Daten
    def get_values(self, page :str) -> str:
        try:
            filename :str = page[0].lower() + page[1::] + ".json"
            data = self.database.read_json_into_dict(filename)
            del data["Template"]
            return '{"code" : 200, "data" : ' + json.dumps(data) + '}'
        except Exception:
            return '{"code" : 500}'


    # Handhabt Hinzufügen der Daten
    def add_values(self, page :str, values) -> str:
        try:
            self.database.add_json_into_file(page, values)
            return '{"code" : 200}'
        except Exception:
            return '{"code" : 500}'


    # Handhabt Updates der Daten
    def update_values(self, page :str, values) -> str:
        try:
            self.database.update_json_into_file(page, values)
            return '{"code" : 200}'
        except Exception:
            return '{"code" : 500}'


    # Handhabt Löschen der Daten
    def delete_values(self, page :str, values) -> str:
        try:
            self.database.remove_json_from_file(page, values)
            return '{"code" : 200}'
        except Exception:
            return '{"code" : 500}'
