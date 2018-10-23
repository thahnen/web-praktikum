#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#   Stellt HTML-Seiten zur Verfügung
#
import os
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup

if os.name != "posix":
    raise Exception("Programm läuft nicht unter Unix!")
template_path = os.path.dirname(os.path.abspath(__file__))+"/../template/"

class View(object):
    # Eigentlich so unnötig wie die Hoden vom Papst
    def __init__(self):
        pass

    @staticmethod
    def render_page(pagename, data):
        page_template_path = template_path + pagename
        if (not os.path.exists(page_template_path)) or os.path.isdir(page_template_path):
            raise Exception("Mako-Template '%s' does not exist or is a directory" % page_template_path)

        template = TemplateLookup(directories = template_path).get_template(pagename)
        return template.render(data_o = data)
