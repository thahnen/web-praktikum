#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Fast alles über Annahmen (assert's), um Fehlerbehandlung kümmert sich die App!


#   Zur Erstellung/ Generierung von (Web-)Seiten:
#   ============================================
#
#   1. Statische Seite zurückgeben
#   => einfach aus Datei einlesen
#
#   2. Dynamische Seite zurückgeben
#   => anhand des Seitennamens und des dazugehörigen Templates
#   => Füllung des Templates aus mitgegebenen Daten


import os
from mako.template import Template
from mako.lookup import TemplateLookup


class View(object):
    def __init__(self, template_path):
        self.template_path = template_path


    # render_static_page(...) throws Exception
    def render_static_page(self, pagename):
        return open(pagename)


    # render_dynamic_page(...) throws Exception
    def render_dynamic_page(self, pagename, data):
        page_template_path = self.template_path + pagename + ".tpl"
        assert (os.path.exists(page_template_path) and not os.path.isdir(page_template_path))

        template = TemplateLookup(directories = self.template_path).get_template(pagename + ".tpl")
        return template.render(data_o = data)
