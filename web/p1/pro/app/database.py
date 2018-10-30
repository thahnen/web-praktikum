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


class Database(object):
    def __init__(self, data_path):
        self.data_path = data_path


    def read_json_into_dict(self, filename):
        file_path = self.data_path + filename
        # anstatt assert try-except um json.load?
        assert (
            os.path.exists(file_path) and not os.path.isdir(file_path)
        )

        data = json.load(open(file_path))
        # Validate if JSON-File is correct -> auslagern in eigene Funktion?
        try:
            # das ist hässlich und wird noch ersetzt
            # anstatt des try-Blocks ein if?
            dummy__elems = [x for x in data["Elements"]]
        except TypeError as te:
            # data["Elements"] kein Dictionary (irgendwas anderes)
            # auf data["Template"] überprüfen, wenn nicht vorhanden:
            #   => JSON-Datei durch Template ersetzen und 404 oä.
            # wenn doch vorhanden:
            #   => data["Elements"] = {} setzen und 404 oä.
            if "Template" in data:
                data["Elements"] = {}
            else:
                # Datei durch JSON-Template ersetzen (aus Datei oder Hardcode?)
                #data = json.load(open("Pfad zum jeweiligen Template"))
                pass

            with open(file_path, "w") as datei:
                json.dump(data)
            # Fehler aber kein passender Fehlercode?
            raise
        except KeyError as ke:
            # data["Elements"] gibt es nicht!
            # auf data["Template"] überprüfen, wenn nicht vorhanden:
            #   => JSON-Datei durch Template ersetzen und 404 oä.
            # wenn doch vorhanden:
            #   => data["Elements"] = {} setzen und 404 oä.
            if "Template" in data:
                data["Elements"] = {}
            else:
                # Datei durch JSON-Template ersetzen (aus Datei oder Hardcode?)
                #data = json.load(open("Pfad zum jeweiligen Template"))
                pass

            with open(file_path, "w") as datei:
                json.dump(data)
            # Fehler aber kein passender Fehlercode?
            raise
        except Exception as e:
            # Irgendwas anderes ist passiert
            raise

        # Return data if everything is fine
        return data


    def write_json_into_file(self, filename, json_dict, update=False):
        file_path = self.data_path + filename
        # anstatt assert try-except um json.load?
        assert (
            os.path.exists(file_path) and not os.path.isdir(file_path)
        )

        data = json.load(open(file_path))
        elements = [x for x in data["Elements"]]
        # Test for Update or new Element
        if update:
            # Update den Rest gleich mit (nur bei projektdaten.json)
            update_all = True if filename == "kundendaten.json" else False

            return

        # New Element!
        pass
