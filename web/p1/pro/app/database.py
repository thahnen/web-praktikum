#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Zur Verarbeitung der Daten im JSON-Format:
#   =========================================
#
#   1. Einlesen einer JSON-Datei
#   => Validierung: Überprüfen, ob Elemente dem Template entsprechen
#   => wenn nicht: Fehler oder JSON auffüllen
#
#   2. Schreiben von JSON-Daten in Datei
#   => Validierung: Überprüfen, ob Elemente dem Template entsprechen
#   => wenn nicht: Fehler oder JSON auffüllen
#
#   Fehlende Funktion(en):
#   - boolean test_on_integrity(JSON data):
#       => überprüft, ob "Template" und "Elements" vorhanden
#       => überprüft, ob alle Elemente dem Template entsprechen (wenn "Elements" nicht leer)


import os
import os.path
import json


if os.name != "posix":
    raise Exception("Programm läuft nicht unter Unix!")
data_path = os.path.dirname(os.path.abspath(__file__))+"/../data/"

class Database(object):
    # Eigentlich so unnötig wie die Hoden vom Papst
    def __init__(self, data_path):
        self.data_path = data_path

    @staticmethod
    def read_json_into_dict(filename):
        # Test if filename contains ".json"
        file_path = data_path + filename
        assert (os.path.exists(file_path) and not os.path.isdir(file_path))
        return json.load(open(file_path))

    @staticmethod
    def write_json_into_file(filename, json_dict):
        # Test if filename contains ".json"
        file_path = data_path + filename
        if (not os.path.exists(file_path)) or os.path.isdir(file_path):
            ## ggf erstellen?
            raise Exception("JSON-File '%s' does not exist or is a directory" % file_path)
        # Bis jetzt noch nichts machen
        pass
