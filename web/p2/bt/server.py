#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, hier wird sich angemeldet
#
#   - "/eval_login" (Pseudo-Seite)
#       => Hier werden alle Anmeldedaten überprüft!
#
#   - "/eval_logout" (Pseudo-Seite)
#       => Hier wird jeder Nutzer ausgeloggt!
#
#   - "/bt":
#       => Bug-Tracker-Seite
#

import os
import cherrypy
import app


class WebServer(object):
    def __init__(self, application):
        self.application = application


    # Index-Seite des Webservers, um sich zu authentifizieren
    @cherrypy.expose
    def index(self) -> str:
        # Auswertung Cookie falls vorhanden!
        cookie = cherrypy.request.cookie
        if "type" in cookie and "username" in cookie and "password" in cookie:
            code, _, _ = self.application.eval_login(cookie["username"].value, cookie["password"].value, True)
            if code == 200:
                return self.application.get_static_page("forward")

        self.application.setCookies(False)
        return self.application.get_static_page("index")


    # Nur POST-Verarbeitung der Benutzereingaben
    @cherrypy.expose
    def eval_login(self, username :str = None, password :str = None) -> str:
        if cherrypy.request.method == "POST" and username != None and password != None:
            code, user_type, password_hash = self.application.eval_login(username, password)
            if code == 200:
                self.application.setCookies(True, user_type, username, password_hash)
                return self.application.get_static_page("forward")

            self.application.setCookies(False)
            return self.application.get_static_page("backward")
        return self.application.get_static_page("404")


    # Nur POST-Verarbeitung der Benutzereingaben
    @cherrypy.expose
    def eval_logout(self) -> str:
        if cherrypy.request.method == "POST":
            self.application.setCookies(False)
            return self.application.get_static_page("backward")
        return self.application.get_static_page("404")


    # Bug-Tracker-Anwendungs-Seite des Webservers
    @cherrypy.expose
    def bt(self) -> str:
        # Auswertung Cookie (muss vorhanden sein)!
        cookie = cherrypy.request.cookie
        if "type" in cookie and "username" in cookie and "password" in cookie:
            code, user_type, _ = self.application.eval_login(cookie["username"].value, cookie["password"].value, True)
            if code == 200:
                # Noch testen, ob es ein QS-Mitarbeiter oder SW-Entwickler ist!
                if user_type == "QSM":
                    return self.application.get_static_page("bt-qsm")
                return self.application.get_static_page("bt-swe")

        self.application.setCookies(False)
        return self.application.get_static_page("backward")


config = {
    "/" : {
        "tools.staticdir.root" : os.path.dirname(os.path.abspath(__file__))
    },
    "/css" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/css/"
    },
    "/js" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/js/"
    }
}

config_rest = {
    "/" : {
        "request.dispatch" : cherrypy.dispatch.MethodDispatcher()
    }
}


if __name__ == '__main__':
    server_path = os.path.dirname(os.path.abspath(__file__))
    logic = app.Application(server_path)

    cherrypy.tree.mount(WebServer(logic), "/", config=config)
    cherrypy.tree.mount(app.Projekt(logic), "/projekt", config=config_rest)
    cherrypy.tree.mount(app.Projektkomponenten(logic), "/projektkomponenten", config=config_rest)
    cherrypy.tree.mount(app.Komponente(logic), "/komponente", config=config_rest)
    cherrypy.tree.mount(app.QSMitarbeiter(logic), "/qsmitarbeiter", config=config_rest)
    cherrypy.tree.mount(app.SWEntwickler(logic), "/swentwickler", config=config_rest)
    cherrypy.tree.mount(app.KatFehler(logic), "/katfehler", config=config_rest)
    cherrypy.tree.mount(app.KatUrsache(logic), "/katursache", config=config_rest)
    cherrypy.tree.mount(app.Fehler(logic), "/fehler", config=config_rest)
    cherrypy.tree.mount(app.ProList(logic), "/prolist", config=config_rest)
    cherrypy.tree.mount(app.KatList(logic), "/katlist", config=config_rest)
    cherrypy.tree.mount(app.Templates(logic), "/templates", config=config_rest)

    cherrypy.engine.start()
    cherrypy.engine.block()
