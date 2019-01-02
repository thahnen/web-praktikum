#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller Qualitätssicherungs-Mitarbeiter:
#   ======================================================
#
#   1. GET /qsmitarbeiter/
#   => Rückgabe aller QS-Mitarbeiter
#
#   2. GET /qsmitarbeiter/<qsmitarbeiter_id>
#   => Rückgabe eines einzelnen QS-Mitarbeiters mit entsprechender QS-Mitarbeiter-Id
#
#   3. POST /qsmitarbeiter/ + JSON-Daten
#   => Neuen QS-Mitarbeiter speichern, gibt neue QS-Mitarbeiter-Id zurück
#
#   4. PUT /qsmitarbeiter/<qsmitarbeiter_id> + JSON-Daten
#   => QS-Mitarbeiter mit entsprechender QS-Mitarbeiter-Id verändern
#
#   5. DELETE /qsmitarbeiter/<qsmitarbeiter_id>
#   => QS-Mitarbeiter mit entsprechender QS-Mitarbeiter-Id löschen
#


import cherrypy


@cherrypy.expose
class QSMitarbeiter(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, qsmitarbeiter_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "qsmitarbeiter" : "QS-Mitarbeiter"-Objekt | List["QS-Mitarbeiter"-Objekt]
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "qsmitarbeiter_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, qsmitarbeiter_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, qsmitarbeiter_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass
