#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Gibt alle(!) sich auf dem Server befindenden Templates zurück:
#   =============================================================
#
#   1. GET /templates/
#   => Rückgabe einer Liste aller Templates
#


import os
import json
import codecs
import cherrypy


@cherrypy.expose
class Templates(object):
    def __init__(self, application):
        self.application = application
        self.template_path = self.application.server_path + "/templates/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "templates" : {
        #       "<Name>" : "<Inhalt>"
        #   }
        # }

        data = {
            'templates' : {}
        }

        files = [n for n in os.listdir(self.template_path) if os.path.isfile(os.path.join(self.template_path, n))]
        for file in files:
            if not file.endswith(".tpl"):
                del files[files.index(file)]

        for filename in files:
            file = codecs.open(self.template_path + filename, 'rU', 'utf-8')
            inhalt = file.read()
            file.close()
            data["templates"][filename] = inhalt

        return json.dumps(data)
