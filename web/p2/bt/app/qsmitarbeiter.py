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
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "QS-Mitarbeiter"-Objekt) oder "QS-Mitarbeiter"-Objekt-Inhalt
        # }

        try:
            qsmitarbeiter = self.application.database.read_json_into_dict("qs-mitarbeiter.json")
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            qsmitarbeiter = qsmitarbeiter["Elements"]
            # Erstmal hier, vlt geht das irgendwie besser (400 anstatt 500)
            a = int(qsmitarbeiter_id) if qsmitarbeiter_id != None else None
        except Exception as e:
            cherrypy.response.status = 500
            return

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(qsmitarbeiter) == 0:
            cherrypy.response.status = 204
            return

        if qsmitarbeiter_id == None:
            # Alle QS-Mitarbeiter zurückgeben
            return qsmitarbeiter

        # Speziellen QS-Mitarbeiter (falls vorhanden) zurückgeben
        # ansonsten 404 nicht gefunden zurückgeben
        for elem in qsmitarbeiter:
            print(elem)
            if int(elem["unique_id"]) == int(qsmitarbeiter_id):
                return elem

        cherrypy.response.status = 404
        return


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   "qsmitarbeiter_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, qsmitarbeiter_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # ggf so? oder wie auswerten?
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, qsmitarbeiter_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # ggf so? oder wie auswerten?
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass
