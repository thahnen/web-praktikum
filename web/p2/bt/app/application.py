#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien

import json
import hashlib
import cherrypy
import app.database
import app.view


class Application(object):
    def __init__(self, server_path :str):
        self.server_path :str = server_path
        self.content_path :str = self.server_path + "/content/"
        self.database = app.Database(server_path + "/data/")
        self.view = app.View(server_path + "/templates/")


    # Handhabt statische Seiten
    def get_static_page(self, pagename :str) -> str:
        try:
            return self.view.render_static_page(self.content_path + pagename + ".html")
        except Exception:
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt den Login-Vorgang
    def eval_login(self, username :str, password :str, cookie :bool = False):
        try:
            code1, qs_mitarbeiter_data = self.get_values("qs-mitarbeiter.json", None)
            code2, sw_entwickler_data = self.get_values("sw-entwickler.json", None)

            if code1 in [200, 204]:
                if code1 == 204: qs_mitarbeiter_data = {}
            else: raise Exception

            if code2 in [200, 204]:
                if code2 == 204: sw_entwickler_data = {}
            else: raise Exception
        except Exception:
            # Irgendein Fehler ist aufgetreten
            return [500, None, None]

        password_hash :str = None
        if not cookie:
            password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        else:
            password_hash = password

        found :bool = None
        for elem in qs_mitarbeiter_data:
            if qs_mitarbeiter_data[elem]["username"] == username and qs_mitarbeiter_data[elem]["password"] == password_hash:
                found = "QSM"

        if found == "QSM": return [200, found, password_hash]

        for elem in sw_entwickler_data:
            if sw_entwickler_data[elem]["username"] == username and sw_entwickler_data[elem]["password"] == password_hash:
                found = "SWE"

        if found == "SWE": return [200, found, password_hash]

        return [404, None, None]


    # Setzt Cookie bzw. loescht ihn
    def setCookies(self, set :bool = True, user_type :str = None, username :str = None, password_hash :str = None):
        if set:
            cherrypy.response.cookie["type"] = user_type
            cherrypy.response.cookie["username"] = username
            cherrypy.response.cookie["password"] = password_hash
        else:
            cherrypy.response.cookie["type"] = ""
            cherrypy.response.cookie["type"]["expires"] = 0
            cherrypy.response.cookie["type"]["max-age"] = 0
            cherrypy.response.cookie["username"] = ""
            cherrypy.response.cookie["username"]["expires"] = 0
            cherrypy.response.cookie["username"]["max-age"] = 0
            cherrypy.response.cookie["password"] = ""
            cherrypy.response.cookie["password"]["expires"] = 0
            cherrypy.response.cookie["password"]["max-age"] = 0


    # Handhabt Rückgabe der Daten
    def get_values(self, json_file :str, unique_id :int):
        try:
            data = self.database.read_json_into_dict(json_file)
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            data = data["Elements"]
        except Exception:
            return [500, None]

        if unique_id != None:
            try:
                unique_id = int(unique_id)
            except Exception:
                return [400, None]

        if unique_id == None and len(data) == 0:
            return [204, None]
        elif unique_id == None and len(data) != 0:
            return [200, data]
        elif unique_id != None and len(data) == 0:
            return [404, None]

        # Spezielle Fehlerkategorie (falls vorhanden) zurückgeben
        for elem in data:
            if int(data[elem]["unique_id"]) == unique_id:
                return [200, data[elem]]

        return [404, None]


    # Handhabt Hinzufügen der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    def add_values(self, json_file :str, add_dict):
        try:
            new_unique_id :int = self.database.add_json_into_file(json_file, add_dict)
            return [200, new_unique_id]
        except Exception:
            return [500, None]


    # Handhabt Updates der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    def update_values(self, json_file :str, unique_id :int, update_dict) -> int:
        if unique_id != None:
            try:
                unique_id = int(unique_id)
            except Exception:
                return 400

        try:
            self.database.update_json_into_file(json_file, update_dict)
            return 200
        except Exception:
            return 500


    # Handhabt Löschen der Daten
    # überarbeiten, dass mehr Fehlercodes möglich sind! Genau: 404...
    def delete_values(self, json_file :str, unique_id :int) -> int:
        if unique_id != None:
            try:
                unique_id = int(unique_id)
            except Exception:
                return 400

        try:
            self.database.remove_json_from_file(json_file, unique_id)
            return 200
        except Exception:
            return 500
