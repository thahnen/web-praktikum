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

# TODO: DELETE Verarbeitung

import cherrypy


@cherrypy.expose
class QSMitarbeiter(object):
    def __init__(self, application):
        self.application = application
        self.data_path :str = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, qsmitarbeiter_id :int = None):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "QS-Mitarbeiter"-Objekt) oder "QS-Mitarbeiter"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("qs-mitarbeiter.json", qsmitarbeiter_id)
        cherrypy.response.status = code
        if code == 200:
            return data


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   "unique_id" : int
        # }

        try:
            input_json = cherrypy.request.json
        except Exception:
            cherrypy.response.status = 400
            return

        code, data = self.application.add_values("qs-mitarbeiter.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return { "unique_id" : data }


    @cherrypy.tools.json_in()
    def PUT(self, qsmitarbeiter_id :int):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 400 | 404 | 500
        #

        try:
            input_json = cherrypy.request.json
        except Exception:
            cherrypy.response.status = 400
            return

        code :int = self.application.update_values("qs-mitarbeiter.json", qsmitarbeiter_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, qsmitarbeiter_id :int):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        code :int = self.application.delete_values("qs-mitarbeiter.json", qsmitarbeiter_id)
        cherrypy.response.status = code

        if code == 200:
            # Hier alle anderen Dateien bereinigen!
            # -> Fehler mit andere Id versehen (irgendwas generelles 99999?)
            # -> Loeschen eigentlich nicht vorhergesehen, da Login-Daten noetig!
            pass
