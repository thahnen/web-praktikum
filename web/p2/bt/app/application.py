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
        self.view = app.View(server_path + "/template/")


    # Handhabt statische Seiten
    def get_static_page(self, pagename):
        try:
            return self.view.render_static_page(self.content_path + pagename + ".html")
        except Exception as e:
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt Rückgabe der Daten
    def get_values(self, page):
        try:
            filename = page[0].lower() + page[1::] + ".json"
            data = self.database.read_json_into_dict(filename)
            del data["Template"]
            return '{"code" : 200, "data" : ' + json.dumps(data) + '}'
        except Exception as e:
            print("Error on API get!")
            return '{"code" : 500}'


    # Handhabt Hinzufügen der Daten
    def add_values(self, page, values):
        try:
            self.database.add_json_into_file(page, values)
            return '{"code" : 200}'
        except Exception as e:
            print("Error on API add!")
            return '{"code" : 500}'


    # Handhabt Updates der Daten
    def update_values(self, page, values):
        try:
            self.database.update_json_into_file(page, values)
            return '{"code" : 200}'
        except Exception as e:
            print("Error on API update!")
            return '{"code" : 500}'


    # Handhabt Löschen der Daten
    def delete_values(self, page, values):
        try:
            self.database.remove_json_from_file(page, values)
            return '{"code" : 200}'
        except Exception as e:
            print("Error on API delete! Item maybe used!")
            return '{"code" : 500}'
