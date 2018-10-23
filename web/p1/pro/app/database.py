#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#   Stellt Verarbeitung/ Speicherung von Daten zur Verfügung
#

# TODO: Es fehlt noch Überprüfung der JSON-Daten auf Richtigkeit usw.

import os
import os.path
import json

if os.name != "posix":
    raise Exception("Programm läuft nicht unter Unix!")
data_path = os.path.dirname(os.path.abspath(__file__))+"/../data/"

class Database(object):
    # Eigentlich so unnötig wie die Hoden vom Papst
    def __init__(self):
        pass

    @staticmethod
    def read_json_into_dict(filename):
        file_path = data_path + filename
        if (not os.path.exists(file_path)) or os.path.isdir(file_path):
            raise Exception("JSON-File '%s' does not exist or is a directory" % file_path)
        return json.load(open(file_path))

    @staticmethod
    def write_json_into_file(self, filename, json_dict):
        file_path = data_path + filename
        if (not os.path.exists(file_path)) or os.path.isdir(file_path):
            ## ggf erstellen?
            raise Exception("JSON-File '%s' does not exist or is a directory" % file_path)
        # Bis jetzt noch nichts machen
        pass
