#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# REVIEW: Fast alles über Annahmen (assert's), um Fehlerbehandlung kümmert sich die App!


#   Zur Verarbeitung der Daten im JSON-Format:
#   =========================================
#
#   1. Validierung der JSON-Daten
#       => Testen, ob Datei existiert
#       => Testen, ob "Template" und "Elements" vorhanden
#       Das kommt noch:
#       => Testen, ob "Template" dem JSON-Template entspricht
#       => Testen, ob Elemente in "Elements" dem "Template" entspricht
#
#   2. Einlesen einer JSON-Datei
#       => Rückgabe der validierten JSON-Dateien
#
#   3. Update von JSON-Daten
#       => Übergebenes JSON mit Datei vergleichen
#       => Element in Datei updaten
#       => Überprüfen, ob andere JSON-Dateien mitgeändert werden müssen
#
#   4. Hinzufügen von JSON-Daten
#       => Bestehende JSON-Datei auf letztes Element überprüfen sowie "unique_id"
#       => Neues Element dahinter einfügen
#
#   5. Löschen von JSON-Daten
#       => Bestehende JSON-Datei auf übergebenes Element vergleichen
#       => Element suchen und entfernen
#


import os
import json


class Database(object):
    def __init__(self, data_path):
        self.data_path = data_path


    # validate_integrity() throws Exception
    def validate_integrity(self, file_path):
        # Annahme, dass JSON-Datei existiert
        assert (os.path.exists(file_path) and not os.path.isdir(file_path))
        data = json.load(open(file_path))

        # Kurze Validierung, genauere folgt irgendwann ^^
        assert ("Template" in data and "Elements" in data)

        return data


    # read_json_into_dict() throws Exception
    def read_json_into_dict(self, filename):
        file_path = self.data_path + filename

        return self.validate_integrity(file_path)


    # update_json_into_file(...) throws Exception
    def update_json_into_file(self, filename, update_dict):
        # Dictionary json_dict sieht wie folgt aus:
        #
        # {
        #   "unique_id" : XYZ,
        #   "..." : ...;
        # }
        #

        file_path = filename[0].lower() + filename[1::]
        file_path = self.data_path + file_path + ".json"

        json_data = self.validate_integrity(file_path)
        print(json_data) #DEBUG
        print("") #DEBUG

        # Iteriere durch alle Elemente
        for elem in json_data["Elements"]:
            # Überprüfe, ob das übergebene Element mit einem bisherigen übereinstimmt
            if json_data["Elements"][elem]["unique_id"] == update_dict["unique_id"]:
                # Wenn ja, dann ersetz das alte einfach durch das neue!
                # Es wird noch nicht auf die Integrität der anderen JSON-Dateien geachtet!
                json_data["Elements"][elem] = update_dict
                break

        print(json_data) #DEBUG
        print("") #DEBUG
        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out)


    # add_json_into_file(...) throws Exception
    def add_json_into_file(self, filename, add_dict):
        # Dictionary add_dict sieht wie folgt aus:
        #
        # {
        #   "unique_id" : XYZ,
        #   "..." : ...;
        # }
        #

        file_path = filename[0].lower() + filename[1::]
        file_path = self.data_path + file_path + ".json"

        json_data = self.validate_integrity(file_path)
        print(json_data) #DEBUG
        print("") #DEBUG

        index = 0

        for elem in json_data["Elements"]:
            if int(json_data["Elements"][elem]["unique_id"]) == int(add_dict["unique_id"]):
                # diese Unique-ID gibt es bereits!
                raise Exception
            # letzten Index suchen
            if int(elem) > int(index):
                index = int(elem)
        # Noch einen höher setzen, da auf letzten gesetzt!
        index += 1

        json_data["Elements"][str(index)] = add_dict

        print(json_data) #DEBUG
        print("") #DEBUG
        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out)


    # remove_json_from_file(...) throws Exception
    def remove_json_from_file(self, filename, unique_id):
        # Integer unique_id entspricht der zu löschenden unique_id!

        file_path = filename[0].lower() + filename[1::]
        file_path = self.data_path + file_path + ".json"

        json_data = self.validate_integrity(file_path)
        print(json_data) #DEBUG
        print("") #DEBUG

        for elem in json_data["Elements"]:
            if int(json_data["Elements"][elem]["unique_id"]) == unique_id:
                # Wenn ja, dann bestehendes löschen!
                # Es wird noch nicht auf die Integrität der anderen JSON-Dateien geachtet!
                del json_data["Elements"][elem]
                break

        print(json_data) #DEBUG
        print("") #DEBUG
        with open(file_path, "w") as json_out:
            json.dump(json_data, json_out)
