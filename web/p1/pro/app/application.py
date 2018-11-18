#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien


import app.database
import app.view


class Application(object):
    def __init__(self, server_path):
        self.server_path = server_path
        self.content_path = self.server_path + "/content/"
        self.database = app.Database(server_path+"/data/")
        self.view = app.View(server_path+"/template/")


    # Handhabt statische Seiten
    def get_static_page(self, pagename):
        try:
            return self.view.render_static_page(self.content_path + pagename + ".html")
        except Exception as e:
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt alle dynamischen Seiten (mit oder ohne Parametern)
    def get_dynamic_page(self, pagename, parameter=None):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")

            if parameter == None:
                return self.view.render_dynamic_page(pagename, data)
            elif parameter == "neu":
                return self.view.render_dynamic_page(pagename + "-new", data)

            found = False
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
        except Exception as e:
            return self.get_static_page("500")


    # Handhabt Updates der Daten
    def update_values(self, values):
        try:
            assert ("link" in values and "method" in values and "data" in values)

            page = values["link"]

            assert (page in ["Kundendaten", "Mitarbeiterdaten", "Projektdaten"])

            if values["method"] == "edit":
                self.database.update_json_into_file(page, values["data"])
            elif values["method"] == "new":
                self.database.add_json_into_file(page, values["data"])
            elif values["method"] == "delete":
                self.database.remove_json_from_file(page, values["data"])
            else:
                raise
        except Exception as e:
            return '{ "code" : 500 }'

        return '{"code":200}'

    # Gibt bestimmte
    def get_json_data(self, values):
        # filename = values["link"]
        # filename = filename[0].lower() + filename[1::]
        # return self.database.read_json_into_dict(filename)
        pass
