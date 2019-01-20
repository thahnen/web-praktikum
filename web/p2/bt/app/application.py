#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien

import json
import hashlib
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
            code1, qs_mitarbeiter_data = self.get_values("qs-mitarbeiter")
            code2, sw_entwickler_data = self.get_values("sw-entwickler")

            if code1 != 200 or code2 != 200: raise

            qs_mitarbeiter_data = qs_mitarbeiter_data["Elements"]
            sw_entwickler_data = sw_entwickler_data["Elements"]
        except Exception as e:
            # Irgendein Fehler ist aufgetreten
            return [500, None, None]

        found = None
        password_hash = haslib.sha256(password.encode("utf-8")).hexdigest()
        for elem in qs_mitarbeiter_data:
            # Hier ggf Username nicht mehr nötig, kann durch unique_id ersetzt werden
            if elem["username"] == username and elem["password"] == password_hash:
                found = "QSM"

        if found == "QSM":
            return [200, found, password_hash]

        for elem in sw_entwickler_data:
            # Hier ggf Username nicht mehr nötig, kann durch unique_id ersetzt werden
            if elem["username"] == username and elem["password"] == password_hash:
                found = "SWE"

        if found == "SWE":
            return [200, found, password_hash]

        return [404, None, None]


    # Handhabt Rückgabe der Daten
    def get_values(self, json_file, unique_id):
        try:
            data = self.database.read_json_into_dict(json_file)
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            data = data["Elements"]
        except Exception as e:
            return [500, None]

        if unique_id != None:
            try:
                unique_id = int(unique_id)
            except Exception as e:
                return [400, None]

        if unique_id == None and len(data) == 0:
            return [204, None]
        elif unique_id == None and len(data) != 0:
            return [200, data]
        elif unique_id != None and len(data) == 0:
            return [404, None]

        # Spezielle Fehlerkategorie (falls vorhanden) zurückgeben
        for elem in data:
            print(elem)
            if int(elem["unique_id"]) == int(unique_id):
                return [200, elem]

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
