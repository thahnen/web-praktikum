#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien

# TODO: MUSS Noch für P2 angepasst werden!

import json
import app.database
import app.view


class Application(object):
    def __init__(self, server_path):
        self.server_path = server_path
        self.content_path = self.server_path + "/content/"
        self.database = app.Database(server_path + "/data/")
        self.view = app.View(server_path + "/templates/")


    # Handhabt statische Seiten
    def get_static_page(self, pagename):
        try:
            return self.view.render_static_page(self.content_path + pagename + ".html")
        except Exception as e:
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt den Login-Vorgang
    def eval_login(self, username, password):
        try:
            qsmitarbeiter = self.database.read_json_into_dict("qsmitarbeiter.json")
            swentwickler = self.database.read_json_into_dict("swentwickler.json")
        except Exception as e:
            raise

        # Rückgabe sollte Array mit (klar ist nicht sicher aber simpel)
        # => Angaben richtig - True | False
        # => Type des Benutzers - QSM | SWE
        # => Halber Hash aus der JSON-Datei!
        return []


    # HIER MUSS ALLES ÜBERARBEITET WERDEN!


    # Handhabt Rückgabe der Daten
    # Gibt Fehler-Codes zurück: 200 | 204 | 400 | 404 | 500
    def get_values(self, json_file, unique_id):
        try:
            data = self.database.read_json_into_dict(json_file)
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            data = data["Elements"]
        except Exception as e:
            return [500, None]

        if unique_id != None:
            # War die Eingabe überhaupt richtig?
            try:
                unique_id = int(unique_id)
            except Exception as e:
                return [400, None]

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(data) == 0:
            return [204, None]

        if unique_id == None:
            # Alle Fehlerkategorien zurückgeben
            return [200, data]

        # Spezielle Fehlerkategorie (falls vorhanden) zurückgeben
        for elem in data:
            print(elem)
            if int(elem["unique_id"]) == int(unique_id):
                return [200, elem]

        # ansonsten 404 nicht gefunden zurückgeben
        return [404, None]


    # Handhabt Hinzufügen der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    def add_values(self, json_file, add_dict):
        try:
            new_unique_id = self.database.add_json_into_file(json_file, add_dict)
            return [200, new_unique_id]
        except Exception as e:
            print("Error on API add!")
            return [500, None]


    # Handhabt Updates der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    # noch gucken, wie man hier die unique_id unterbringen kann!
    def update_values(self, json_file, unique_id, update_dict):
        if unique_id != None:
            # War die Eingabe überhaupt richtig?
            try:
                unique_id = int(unique_id)
            except Exception as e:
                return 400

        try:
            self.database.update_json_into_file(json_file, update_dict)
            return 200
        except Exception as e:
            print("Error on API update!")
            return 500


    # Handhabt Löschen der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    def delete_values(self, json_file, unique_id):
        if unique_id != None:
            # War die Eingabe überhaupt richtig?
            try:
                unique_id = int(unique_id)
            except Exception as e:
                return 400

        try:
            self.database.remove_json_from_file(json_file, unique_id)
            return 200
        except Exception as e:
            print("Error on API delete! Item maybe used!")
            return 500
