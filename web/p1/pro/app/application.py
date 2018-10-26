#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Stellt API-Funktionen bereit:
#   ============================
#
#   Nur um diese Datei irgendwie nützlich zu machen -.-
#
#   Server ruft den Kram der Application auf.
#   Kümmert sich um Validät der Parameter und so


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
        return self.view(self.view.render_dynamic_page(
            pagename, self.database.read_json_into_dict("")
        ))

    def get_dynamic_page_with_params(self, pagename, parameter):
        # So wenn anstatt Dateiname die URL abgefragt wird
        # => entnimmt Websitenname und Parameter aus Webseiten-Pfad
        #data_file, params = pagename.split("/")[-1:][0].split("?")

        # Parameter sollte unique ID entsprechen, wenn nicht Fehler und so
        try:
            data = self.database.read_json_into_dict(pagename)
        except app.database.DatabaseException as de:
            errorcode = de.args[0]["code"]
            # Gucken welcher Code es war und dementsprechend Seite zurückgeben!
        except Exception as e:
            raise
        elements = [x for x in data["Elements"]]

        for element in elements:
            try:
                # Testen, ob:
                # {
                #   "Template" : { ... },
                #   "Elements" : {
                #       "1" : { "unique_id" := parameter ist! ... },
                #       "2" : { "unique_id" := parameter ist! ... },
                #       ...
                #       "n" : { "unique_id" := parameter ist! ... }
                #   }
                # }
                if int(data["Elements"][element]["unique_id"]) == int(parameter):
                    # mal gucken was passiert wenns geht :o
                    break
                # mal gucken was passiert wenn nicht :o
            except Exception as e:
                raise

        return "Bruder muss los"

    def update_values(self, pagename, values):
        # Update auch der anderen Seiten und so!
        return "Bruder muss los"
