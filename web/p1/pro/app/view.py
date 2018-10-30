#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Zur Erstellung/ Generierung von (Web-)Seiten:
#   ============================================
#
#   1. Erstellung mit Template und zugehörigen Daten
#   => trifft zu auf die Kundendaten/ Prohektdaten/ Mitarbeiterdaten
#   => trifft auf einzelne Einträge zu (jeweils in URL mitgegeben!)
#
#   TODO: 
#   2. Generierung von nötigem CSS/ JS Code je Seite
#   => Vermeidung von zu vielen Dateien bzw. unnötigem Laden von Daten!


import os.path
from mako.template import Template
from mako.lookup import TemplateLookup


class View(object):
    def __init__(self, template_path):
        self.template_path = template_path


    # Gibt statische Seite zurück (nichts besonderes)
    def render_static_page(self, pagename):
        return open(pagename)


    # Gibt dynamische Seite anhand eines Templates zurück
    def render_dynamic_page(self, pagename, data):
        page_template_path = self.template_path + pagename + ".tpl"
        if (not os.path.exists(page_template_path)) or os.path.isdir(page_template_path):
            raise Exception("Mako-Template '%s' does not exist or is a directory" % page_template_path)

        template = TemplateLookup(directories = self.template_path).get_template(pagename + ".tpl")
        return template.render(data_o = data)
