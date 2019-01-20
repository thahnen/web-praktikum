#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Auswertung aller Fehler nach Projekt/Komponente/Status:
#   ======================================================
#
#   1. GET /katlist/
#   => Rückgabe einer Liste aller Fehler nach Projekt/Komponente/Status sortiert

import cherrypy


@cherrypy.expose
class KatList(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 500
        #
        # {
        #   "1...n" : "Fehler"-Objekt
        # }

        code, data = self.application.get_values("fehler.json", None)
        if code != 200:
            cherrypy.response.status = code
            return

        try:
            # Fehler nach:
            # 1) Projekt-Id (eine Zahl)
            # 2) Komponenten (eine Liste)
            # 3) Status (erkannt oder behoben)
            # sortieren
            return dict(sorted(
                data, key=lambda elem: (elem["erkannt"]["projekt"], elem["erkannt"]["komponenten"], elem["status"])
            ))
        except Exception as e:
            cherrypy.response.status = 500
