#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen für den Server bereit:
#   ===========================================
#
#   Datei kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien
#
#   GGF keine Fehlercode-Seiten statisch sondern dynamisch generieren :3
#   => mit angegebenem Grund zum debuggen in Zukunft möglich
#   => nur ein traurige 404 und böse 500 Seite :D


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
            # Nur Fehler 500 zurückgeben; kann auch zur Exception führen xD
            return self.view.render_static_page(self.content_path + "500.html")


    # Handhabt dynamische Seiten
    def get_dynamic_page(self, pagename):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
        except Exception as e:
            return self.get_static_page("500")

        return self.view.render_dynamic_page(pagename, data)


    # Handhabt dynamische Seiten MIT Parametern
    def get_dynamic_page_with_params(self, pagename, parameter):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
        except Exception as e:
            return self.get_static_page("500")

        elements = [x for x in data["Elements"]]
        found = False

        for element in elements:
            try:
                if int(data["Elements"][element]["unique_id"]) == int(parameter):
                    # Alles andere Löschen, damit nur noch das eine übrig bleibt!
                    data["Data"] = data["Elements"][element]
                    del data["Elements"]
                    found = True
                    break
            except Exception as e:
                return self.get_static_page("500")

        if found:
            return self.view.render_dynamic_page(pagename + "edit", data)
        return self.get_static_page("404")


    # Funktion um JSON-Daten zu ändern
    def update_values(self, values):
        # Welche der Seiten gemeint ist muss aus übergebenem JSON ermittelt werden!
        # Update auch der anderen Seiten und so!
        return "Bruder muss los\n"
