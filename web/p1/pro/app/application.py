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


    # Handhabt dynamische Seiten (zusammenfassen mit get_dynamic_page_with_params(...))
    def get_dynamic_page(self, pagename):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
        except Exception as e:
            return self.get_static_page("500")

        return self.view.render_dynamic_page(pagename, data)


    # Handhabt dynamische Seiten MIT Parametern (zusammenfassen mit get_dynamic_page(...))
    def get_dynamic_page_with_params(self, pagename, parameter):
        try:
            data = self.database.read_json_into_dict(pagename + ".json")
        except Exception as e:
            return self.get_static_page("500")

        if parameter == "neu":
            return self.view.render_dynamic_page(pagename + "-new", data["Template"])

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

        if found:
            return self.view.render_dynamic_page(pagename + "-edit", data)
        return self.get_static_page("404")


    # update_values() throws Exception
    def update_values(self, values):
        #
        #   1) Link ( values["link"] ) auswerten und auf Richtigkeit prüfen
        #   => Link nicht "Kundendaten" / "Mitarbeiterdaten" / "Projektdaten":
        #          - Fehler zurückgeben: { "code" : 404 }
        #   2) Methode ( values["methode"] ) auswerten und auf Richtigkeit prüfen:
        #   => 2.1) "edit" (aka Werte werden geupdatet):
        #           - Daten jeweils updaten && Alles klar zurückgeben: { "code" : 200 }
        #   => 2.2) "new" (aka neue Werte kommen hinzu):
        #          - Daten neu hinzufügen && Alles klar zurückgeben: { "code" : 200 }
        #   => 2.3) "delete" (aka Werte werden gelöscht):
        #          - Daten jeweils löschen && Alles klar zurückgeben : {"code" : 200}
        #   => 2.4) Irgendwas anderes:
        #           - Fehler zurückgeben: { "code" : 500 }
        #

        # Annahme values["link"] und values["data"] existiert!
        assert(values.has_key("link") and  values.has_key("data"))

        page = values["link"]

        # 1) Link überprüfen
        if page not in ["Kundendaten", "Mitarbeiterdaten", "Projektdaten"]:
            return '{ "code" : 404 }'

        # 2) Methode überprüfen
        try:
            if values["method"] == "edit":
                # 2.1) Update
                self.database.write_json_into_file(page, values["data"], update=True)
            elif values["method"] == "new":
                # 2.2) Neu hinzufügen
                self.database.write_json_into_file(page, values["data"])
            elif values["method"] == "delete":
                # 2.3) Löschen
                # fehlt noch!
                raise
            else:
                raise Exception({"code" : 500})
        except Exception as e:
            # 2.3) Irgendwas anderes (falsches) bzw
            #       irgendwas beim Speichern ging schief!
            print(e.args[0]["code"])
            return '{ "code" : %s }' % e.args[0]["code"]

        # Alles klärchen :)
        return '{ "code" : 200 }'
