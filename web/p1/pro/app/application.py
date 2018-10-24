#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Stellt API-Funktionen bereit:
#   ============================
#

class Application(object):
    def __init__(self, server_path):
        self.server_path = server_path

    def get_static_page(self, pagename):
        return "Bruder muss los"

    def get_dynamic_page(self, pagename):
        return "Bruder muss los"

    def get_dynamic_page_with_params(self, pagename, parameter):
        return "Bruder muss los"

    def update_values(self, pagename, values):
        return "Bruder muss los"
