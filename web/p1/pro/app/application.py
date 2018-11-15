#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien
#


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


    # Handhabt dynamische Seiten (zusammenfassen mit get_dynamic_page_with_params(...))
    def get_dynamic_page(self, pagename):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
            return self.view.render_dynamic_page(pagename, data)
        except Exception as e:
            return self.get_static_page("500")


    # Handhabt dynamische Seiten MIT Parametern (zusammenfassen mit get_dynamic_page(...))
    def get_dynamic_page_with_params(self, pagename, parameter):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
        except Exception as e:
            return self.get_static_page("500")

        if parameter == "neu":
            try:
                return self.view.render_dynamic_page(pagename + "-new", data["Template"])
            except Exception as e:
                return self.get_static_page("500")

        found = False

        for elem in data["Elements"]:
            try:
                if int(data["Elements"][elem]["unique_id"]) == int(parameter):
                    # Alles andere Löschen, damit nur noch das eine übrig bleibt!
                    data["Data"] = data["Elements"][elem]
                    del data["Elements"]
                    found = True
                    break
            except Exception as e:
                return self.get_static_page("500")

        try:
            if found:
                return self.view.render_dynamic_page(pagename + "-edit", data)
            return self.get_static_page("404")
        except Exception as e:
            return self.get_static_page("500")


    def update_values(self, values):
        #
        #   1) Link ( values["link"] ) auswerten und auf Richtigkeit prüfen
        #   2) Methode ( values["methode"] ) auswerten und auf Richtigkeit prüfen:
        #   => 2.1) "edit" (aka Werte werden geupdatet):
        #           - Daten jeweils updaten && Alles klar zurückgeben: { "code" : 200 }
        #   => 2.2) "new" (aka neue Werte kommen hinzu):
        #          - Daten neu hinzufügen && Alles klar zurückgeben: { "code" : 200 }
        #   => 2.3) "delete" (aka Werte werden gelöscht):
        #          - Daten jeweils löschen && Alles klar zurückgeben : {"code" : 200}
        #

        # Annahme "values" richtig aufgebaut existiert!
        try:
            assert ("link" in values and "method" in values and "data" in values)
        except Exception as e:
            return '{ "code" : 500 }'

        page = values["link"]

        # 1) Link überprüfen
        try:
            assert (page in ["Kundendaten", "Mitarbeiterdaten", "Projektdaten"])
        except Exception as e:
            return '{ "code" : 404 }'

        # 2) Methode überprüfen
        try:
            if values["method"] == "edit":
                # 2.1) Update
                self.database.update_json_into_file(page, values["data"])
            elif values["method"] == "new":
                # 2.2) Neu hinzufügen
                self.database.add_json_into_file(page, values["data"])
            elif values["method"] == "delete":
                # 2.3) Löschen
                self.database.remove_json_from_file(page, values["data"])
            else:
                raise
        except Exception as e:
            return '{ "code" : 500 }'

        # Alles klärchen :)
        return '{ "code" : 200 }'
