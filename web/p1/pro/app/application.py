#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen bereit:
#   ============================
#
#   Nur um diese Datei irgendwie nützlich zu machen -.-
#
#   Server ruft den Kram der Application auf.
#   Kümmert sich um Validität der Parameter und Daten
#   NICHT: Validität der JSON-Dateien


import app.database
import app.view

class Application(object):
    def __init__(self, server_path):
        self.server_path = server_path
        self.database = app.Database(server_path+"/data/")
        self.view = app.View(server_path+"/template/")

    def get_static_page(self, pagename):
        return open(self.view.render_static_page(pagename))

    def get_dynamic_page(self, pagename):
        try:
            data = self.database.read_json_into_dict(pagename)
        except app.database.DatabaseException as de:
            errorcode = de.args[0]["code"]
            # Gucken welcher Code es war und dementsprechend Seite zurückgeben!
        except Exception as e:
            raise

        # ggf auf "Pagename" testen?
        return self.view.render_dynamic_page(pagename, data)

    def get_dynamic_page_with_params(self, pagename, parameter):
        try:
            data = self.database.read_json_into_dict(pagename)
        except app.database.DatabaseException as de:
            errorcode = de.args[0]["code"]
            # Gucken welcher Code es war und dementsprechend Seite zurückgeben!
        except Exception as e:
            raise

        elements = [x for x in data["Elements"]]
        found = False

        for element in elements:
            try:
                #   "Elements" : {
                #       "1" : { "unique_id" := parameter testen! ... },
                #       ...
                #       "n" : { "unique_id" := parameter testen! ... }
                #   }
                if int(data["Elements"][element]["unique_id"]) == int(parameter):
                    # Alles andere Löschen, damit nur noch das eine übrig bleibt!
                    data["Data"] = data["Elements"][element]
                    del data["Elements"]
                    found = True
                    break
            except Exception as e:
                raise

        if found:
            # schön das Template zum bearbeiten zurückgeben!
            pass

        # 404 zurückgeben (so oder so ähnlich ^-^)
        return self.get_static_page("/content/404.html")

    def update_values(self, pagename, values):
        # Update auch der anderen Seiten und so!
        return "Bruder muss los"
