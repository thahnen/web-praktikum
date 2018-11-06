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


    # read_json_into_dict() throws Exception
    def read_json_into_dict(self, filename):
        file_path = self.data_path + filename

        assert (os.path.exists(file_path) and not os.path.isdir(file_path))

        data = json.load(open(file_path))
        # Validate if JSON-File is correct -> auslagern in eigene Funktion?
        try:
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
                data = json.load(open(file_path + ".tpl"))

            with open(file_path, "w") as datei:
                json.dump(data)
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
                data = json.load(open(file_path + ".tpl"))

            with open(file_path, "w") as datei:
                json.dump(data)
            raise
        except Exception as e:
            raise

        # Return data if everything is fine
        return data


    # write_json_into_file(...) throws Exception
    def write_json_into_file(self, filename, json_dict, update=False):
        #
        #   1) Erhaltene Daten mit Template aus JSON auf Richtigkeit prüfen
        #   2) Update oder neues Element hinzufügen?
        #   => 2.1) Update:
        #       2.1.1) Muss die "Projektdaten.json" auch geändert werden?
        #       => 2.1.1.1) ja:
        #           2[...]1) Alte Daten zwischenspeichern und Neue Daten updaten
        #           2[...]2) "Projektdaten.json" updaten
        #           2[...]3) Alles ok, es passiert nichts [Application erkennt das]
        #       => 2.1.1.2) nein:
        #           2[...]1) Neue Daten updaten
        #           2[...]2) Alles ok, es passiert nichts [Application erkennt das]
        #   => 2.2) Neu:
        #       2.2.1) Index für neuen Eintrag herausfinden
        #       2.2.2) Neue Daten eintragen mit neuem Index
        #       2.2.3) Alles ok, es passiert nichts [Application erkennt das]
        #

        file_path = filename[0].lower() + filename[1::]
        file_path = self.data_path + file_path + ".json"

        assert (os.path.exists(file_path) and not os.path.isdir(file_path))

        data = json.load(open(file_path))
        elements = [x for x in data["Elements"]]
        templates = [x for x in data["Template"]]
        json_data = [x for x in json_dict]
        print(elements)


        # 1) Auf Richtigkeit prüfen (alles Template-Items erfüllt und nicht doppelt!)
        # 1.1) Beide Dicts gleich lang (muss, sonst falsches JSON übergeben)
        if len(templates) != len(json_data):
            raise Exception({"code" : 100})
        else:
            # 1.2) Beide Keys der Dicts auch gleich (muss, sonst falsches JSON übergeben)
            for x in range(0, len(templates)):
                if templates[x] != json_data[x]:
                    raise Exception({"code" : 101})

        gefunden = False
        update_elem = None
        for elem in elements:
            if str(data["Elements"][elem]["unique_id"]) == json_dict["unique_id"]:
                update_elem = elem
                gefunden = True


        # 2) Update oder neues Element?
        if update:
            # 2.1) Update
            # Testen ob die unique_id auch einer bestehenden entspricht!
            if not gefunden: raise Exception({"code" : 102})

            # 2.1.1) Muss "Projektdaten.json" geändert werden?
            if (filename == "Kundendaten" or filename == "Mitarbeiterdaten"):
                # 2.1.1.1) Ja (kein direktes Update "Projektdaten")
                pass

            # 2.1.1.2) Nein (direktes Update "Projektdaten")
            data["Elements"][elem] = json_dict
            with open(file_path, "w") as json_file:
                json.dump(data, json_file)
            return

        # 2.2) Neu
        # Testen, ob unique_id einer bestehenden entspricht
        if gefunden: raise Exception({"code" : 103})
        # 2.2.1) Letzte Index-Nummer bekommen
        letzte = -1
        for elem in elements:
            # Kein Try-Except weil Indizes nur Nummern sein können!
            index = int(elem)
            letzte = index if (index > letzte) else letzte

        letzte += 1
        data["Elements"][str(letzte)] = json_dict

        # 2.2.2) Neue Daten eintragen
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)
