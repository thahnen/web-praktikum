#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Fast alles über Annahmen (assert's), um Fehlerbehandlung kümmert sich die App!


#   Zur Erstellung/ Generierung von (Web-)Seiten:
#   ============================================
#
#   1. Statische Seite zurückgeben
#   => einfach aus Datei einlesen
#
#   2. Alle JS-Templates anfordern
#   => einlesen aller(!) Dateien
#   => Dictionary mit Dateiname und Dateiinhalt abspeichern


import os
from mako.template import Template
from mako.lookup import TemplateLookup


class View(object):
    def __init__(self, template_path):
        self.template_path = template_path


    # render_static_page(...) throws Exception
    def render_static_page(self, pagename):
        return open(pagename)


    # return_templates(...) throws Exception
    def return_templates(self):
        files = [n for n in os.listdir(self.template_path) if os.path.isfile(os.path.join(self.template_path, n))]
        for file in files:
            if not file.endswith(".tpl"):
                del files[files.index(file)]

        return {name : open(self.template_path + name).read() for name in files}
