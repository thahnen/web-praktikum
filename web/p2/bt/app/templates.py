#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Gibt alle(!) sich auf dem Server befindenden Templates zurück:
#   =============================================================
#
#   1. GET /templates/
#   => Rückgabe einer Liste aller Templates

import cherrypy


@cherrypy.expose
class Templates(object):
    def __init__(self, application):
        self.application = application
        self.template_path = self.application.server_path + "/templates/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene Daten mit folgenden Aufbau (weil das lt. Beims so muss),
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 500
        #
        # {
        #   "templates" : {
        #       "<Name>" : "<Inhalt>"
        #   }
        # }

        try:
            templates = self.application.view.return_templates()
            if not bool(templates):
                cherrypy.response.status = 204
                return
            return { "templates" : templates }
        except Exception as e:
            cherrypy.response.status = 500
            return
