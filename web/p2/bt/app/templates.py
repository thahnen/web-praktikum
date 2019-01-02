#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Gibt alle(!) sich auf dem Server befindenden Templates zurück:
#   =============================================================
#
#   1. GET /templates/
#   => Rückgabe einer Liste aller Templates
#


import cherrypy


@cherrypy.expose
class Templates(object):
    def __init__(self, application):
        self.application = application
        self.template_path = self.application.server_path + "/templates/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "templates" : {
        #       "<Name>" : "<Inhalt>"
        #   }
        # }

        pass
