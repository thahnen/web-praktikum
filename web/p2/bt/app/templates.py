#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Gibt alle(!) sich auf dem Server befindenden Templates zurück:
#   =============================================================
#
#   1. GET /templates/
#   => Rückgabe einer Liste aller Templates
#

# REVIEW: Ist eigentlich soweit fertig, es fehlen vlt. nur die Auswertung bezüglich Code?


import cherrypy


@cherrypy.expose
class Templates(object):
    def __init__(self, application):
        self.application = application
        self.template_path = self.application.server_path + "/templates/"


    # GGF achten ob keine vorhanden, dann 204 zurückgeben?
    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau (weil das lt. Beims so muss),
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 500
        #
        # {
        #   "templates" : {
        #       "<Name>" : "<Inhalt>"
        #   }
        # }

        try:
            data = {
                "templates" : self.application.view.return_templates()
            }

            return data
        except Exception as e:
            cherrypy.response.status = 500
            return
