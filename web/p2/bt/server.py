#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, hier wird sich angemeldet
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
    def index(self):
        # Auswertung Cookie falls vorhanden!
        cookie = cherrypy.request.cookie
        if "hash" in cookie:
            # Hier dann den Cookie überprüfen
            print(f"Cookie 'hash' set to: {cookie['hash'].value}")

            self.application.eval_login()
        else:
            print(f"Cookie 'hash' not set")

        return self.application.get_static_page("index")

    # Nur POST-Verarbeitung der Benutzereingaben
    @cherrypy.expose
    def eval_login(self, username=None, password=None):
        if cherrypy.request.method == "POST" and username != None and password != None:
            # 1. Testen, ob Username in QS-Mitarbeiter oder SW-Entwickler (ja -> weiter)
            # 2. Testen, ob Hash mit abgespeichertem übereinstimmt (ja -> weiter)
            # 3. Cookie setzen (Hash aus Username + Hast), Weiterleitung auf /bt zurückgeben
            return f"{username}: {password}"

            qs_mitarbeiter_data = self.application.get_values("qs-mitarbeiter")
            if qs_mitarbeiter_data["code"] == 500:
                # Irgendein Fehler ist aufgetreten
                pass

        return self.application.get_static_page("404")

    # Bug-Tracker-Anwendungs-Seite des Webservers
    @cherrypy.expose
    def bt(self):
        # Testen, ob man als QS-Mitarbeiter angemeldet ist oder SW-Entwickler
        # je nachdem andere Seite zurückgeben!
        return self.application.get_static_page("bt")


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

    cherrypy.tree.mount(
        WebServer(logic), "/", config=config
    )

    cherrypy.tree.mount(
        app.Projekt(logic), "/projekt", config=config_rest
    )

    cherrypy.tree.mount(
        app.Projektkomponenten(logic), "/projektkomponenten", config=config_rest
    )

    cherrypy.tree.mount(
        app.Komponente(logic), "/komponente", config=config_rest
    )

    cherrypy.tree.mount(
        app.QSMitarbeiter(logic), "/qsmitarbeiter", config=config_rest
    )

    cherrypy.tree.mount(
        app.SWEntwickler(logic), "/swentwickler", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatFehler(logic), "/katfehler", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatUrsache(logic), "/katursache", config=config_rest
    )

    cherrypy.tree.mount(
        app.Fehler(logic), "/fehler", config=config_rest
    )

    cherrypy.tree.mount(
        app.ProList(logic), "/prolist", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatList(logic), "/katlist", config=config_rest
    )

    cherrypy.tree.mount(
        app.Templates(logic), "/templates", config=config_rest
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
