#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Fast alles über Annahmen (assert's), um Fehlerbehandlung kümmert sich die App!


#   Zur Verarbeitung der Daten im JSON-Format:
#   =========================================
#
#   1. Validierung der JSON-Daten
#       => Testen, ob Datei existiert
#       Das kommt noch:
#       => Testen, ob "Template" und "Elements" vorhanden in eingelesen Dateien
#       => Testen, ob "Template" dem JSON-Template entspricht
#       => Testen, ob Elemente in "Elements" dem "Template" entspricht
#
#   2. Einlesen einer JSON-Datei
#       => Rückgabe der validierten JSON-Dateien
#
#   3. Update von JSON-Daten
#       => Übergebenes JSON mit Datei vergleichen
#       => Element in Datei updaten
#
#   4. Hinzufügen von JSON-Daten
#       => Bestehende JSON-Datei auf letztes Element überprüfen sowie "unique_id"
#       => Neues Element dahinter einfügen
#
#   5. Löschen von JSON-Daten
#       => Bestehende JSON-Datei auf übergebenes Element vergleichen
#       => ggf. Projektdaten auf Vorkommen überprüfen und falls nicht vorhanden löschen
#       => Element suchen und entfernen
#
#   6. Neue "unique_id" anfragen
#       => Wird eingelesen aus der JSON-Datei "unique_id.json"
#       => Dann Zähler inkrementiert und abgespeichert!

# TODO: Muss noch für P2 angepasst werden!


import os
import json


class Database(object):
    def __init__(self, data_path):
        self.data_path = data_path


    # validate_integrity() throws Exception
    def validate_integrity(self, file_path):
        assert (os.path.exists(file_path) and not os.path.isdir(file_path))
        data = json.load(open(file_path))

        # Validierung der JSON-Daten um für alle Fälle sicher zu sein
        # kommt noch (irgendwann) :)

        return data


    # read_json_into_dict() throws Exception
    def read_json_into_dict(self, filename):
        file_path = self.data_path + filename
        return self.validate_integrity(file_path)


    # get_new_unique_id(...) returns int
    def get_new_unique_id(self):
        file_path = self.data_path + "unique_id.json"
        json_data = self.validate_integrity(file_path)

        json_data["unique_id"] += 1
        new = int(json_data["unique_id"])

        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out, indent=4)

        return new


    # add_json_into_file(...) throws Exception
    def add_json_into_file(self, filename, add_dict):
        # Dictionary add_dict hat folgenden Aufbau:
        #
        # {
        #   "unique_id" : XYZ,
        #   "..." : ...;
        # }

        file_path = self.data_path + filename
        json_data = self.validate_integrity(file_path)

        # "Generierte" neue unique_id bekommen
        new_unique_id = self.get_new_unique_id()
        add_dict["unique_id"] = new_unique_id

        index = 0
        for elem in json_data["Elements"]:
            if int(elem) > int(index):
                index = int(elem)
        index += 1

        json_data["Elements"][str(index)] = add_dict

        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out, indent=4)

        return new_unique_id


    # update_json_into_file(...) throws Exception
    def update_json_into_file(self, filename, update_dict):
        # Dictionary json_dict hat folgenden Aufbau:
        #
        # {
        #   "unique_id" : XYZ,
        #   "..." : ...;
        # }
        #

        file_path = self.data_path + filename
        json_data = self.validate_integrity(file_path)

        found = False
        for elem in json_data["Elements"]:
            if int(json_data["Elements"][elem]["unique_id"]) == int(update_dict["unique_id"]):
                found = True
                json_data["Elements"][elem] = update_dict
                break

        if not found: raise

        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out, indent=4)


    # remove_json_from_file(...) throws Exception
    def remove_json_from_file(self, filename, unique_id):
        file_path = self.data_path + filename
        json_data = self.validate_integrity(file_path)

        found = False
        #old = None
        for elem in json_data["Elements"]:
            if int(json_data["Elements"][elem]["unique_id"]) == int(unique_id):
                found = True
                #old = json_data["Elements"][elem]
                del json_data["Elements"][elem]
                break

        if not found: raise

        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out, indent=4)
