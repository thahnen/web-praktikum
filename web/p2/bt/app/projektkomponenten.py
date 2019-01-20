#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ver-/Bearbeitung aller (Projekt-)Komponenten:
#   ============================================
#
#   1. GET /projektkomponenten/<projekt_id>
#   => Rückgabe aller Projektkomponenten zum Projekt mit entsprechender Projekt-Id
#
#   2. GET /komponente/
#   => Rückgabe aller Projektkomponenten
#
#   3. GET /komponente/<komponente_id>
#   => Rückgabe einer einzelnen Projektkomponente mit entsprechender Komponenten-Id
#
#   4. POST /komponente/ + JSON-Daten
#   => Neue Projektkomponente speichern, gibt neue Komponenten-Id zurück
#
#   5. PUT /komponente/<komponente_id> + JSON-Daten
#   => Projektkomponente mit entsprechender Komponenten-Id verändern
#
#   6. DELETE /komponente/<komponente_id>
#   => Projektkomponente mit entsprechender Komponenten-Id löschen

# TODO: DELETE Verarbeitung

import cherrypy


@cherrypy.expose
class Projektkomponenten(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, projekt_id):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 400 | 500
        #
        # {
        #   "1...n" : "Komponenten"-Objekt
        # }

        if projekt_id != None:
            try:
                projekt_id = int(projekt_id)
            except Exception as e:
                cherrypy.response.status = 400
                return

        code, data = self.application.get_values("komponenten.json", None)
        if code != 200:
            cherrypy.response.status = code
            return

        # Alle Komponenten überprüfen, ob sie zum Projekt gehören
        for elem in data:
            if int(elem["projekt"]) != projekt_id:
                del elem

        if len(data) == 0:
            cherrypy.response.status = 204
            return

        return data


@cherrypy.expose
class Komponente(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, komponente_id=None):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "Komponenten"-Objekt) oder "Komponenten"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("komponenten.json", komponente_id)
        cherrypy.response.status = code
        if code == 200:
            return data


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, projekt_id):
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
        except Exception as e:
            cherrypy.response.status = 400
            return


    @cherrypy.tools.json_in()
    def PUT(self, komponente_id):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 400 | 404 | 500
        #
        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code = self.application.update_values("komponenten.json", komponente_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, komponente_id):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        code = self.application.delete_values("komponenten.json", komponente_id)
        cherrypy.response.status = code

        if code == 200:
            # Hier alle anderen Dateien bereinigen!
            # -> Projekt (entfernen) -> Fehler (loeschen) -> QS-Mitarbeiter / SW-Entwickler (entfernen)
            pass
