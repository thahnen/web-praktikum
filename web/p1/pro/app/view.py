#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Zur Erstellung/ Generierung von (Web-)Seiten:
#   ============================================
#
#   1. Erstellung mit Template und zugehörigen Daten
#   => trifft zu auf die Kundendaten/ Prohektdaten/ Mitarbeiterdaten
#   => trifft auf einzelne Einträge zu (jeweils in URL mitgegeben!)
#
#   2. Generierung von nötigem CSS/ JS Code je Seite
#   => Vermeidung von zu vielen Dateien bzw. unnötigem Laden von Daten!

import os
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup

if os.name != "posix":
    raise Exception("Programm läuft nicht unter Unix!")
template_path = os.path.dirname(os.path.abspath(__file__))+"/../template/"

class View(object):
    # ggf template_path in view_path umändern?
    def __init__(self, template_path):
        pass

    @staticmethod
    def render_static_page(pagename):
        pass

    @staticmethod
    def render_dynamic_page(pagename, data):
        page_template_path = template_path + pagename
        if (not os.path.exists(page_template_path)) or os.path.isdir(page_template_path):
            raise Exception("Mako-Template '%s' does not exist or is a directory" % page_template_path)

        template = TemplateLookup(directories = template_path).get_template(pagename)
        return template.render(data_o = data)
