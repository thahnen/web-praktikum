#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Zur Verarbeitung der Daten im JSON-Format:
#   =========================================
#
#   1. Validierung der JSON-Daten
#       validate_integrity() -> Dictionary | Exception
#       ----------------------------------------------
#       => Testen, ob Datei existiert
#       => Testen, ob "Template" und "Elements" vorhanden
#       Das kommt noch:
#       => Testen, ob "Template" dem JSON-Template entspricht
#       => Testen, ob Elemente in "Elements" dem "Template" entspricht
#
#   2. Einlesen einer JSON-Datei
#       read_json_into_dict() -> Dictionary | Exception
#       -----------------------------------------------
#       => Rückgabe der validierten JSON-Dateien
#
#   3. Schreiben von JSON-Daten in Datei
#       write_json_into_file() -> Nichts | Exception
#       --------------------------------------------
#       => Überprüfung ob Update oder neues Element
#
#   4. Update von JSON-Daten
#       update_json_into_file() -> Nichts | Exception
#       ------------------------------------------
#       => Übergebenes JSON mit Datei vergleichen
#       => Überprüfen, ob andere JSON-Dateien mitgeändert werden müssen
#
#   5. Hinzufügen von JSON-Daten
#       add_json_into_file() -> Nichts | Exception
#       ------------------------------------------
#       => Bestehende JSON-Datei auf letztes Element überprüfen sowie "unique_id"
#       => Neues Element dahinter einfügen
#
#   6. Löschen von JSON-Daten
#       remove_json_from_file() -> Nichts | Exception
#       ---------------------------------------------
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
        # Annahme, dass JSON-Datei exisitert
        assert (os.path.exists(file_path) and not os.path.isdir(file_path))
        data = json.load(open(file_path))

        # Kurze Validierung, genauere folgt irgendwann ^^
        assert ("Template" in data and "Elements" in data)

        return data


    # read_json_into_dict() throws Exception
    def read_json_into_dict(self, filename):
        file_path = self.data_path + filename

        # Validierung der JSON-Datei
        data = self.validate_integrity(file_path)

        # Wenn alles ok so zurückgeben
        return data


    # write_json_into_file(...) throws Exception
    # TODO: Irgendwas funktioniert noch nicht mit dem Update!!!
    def write_json_into_file(self, filename, json_dict, update=False):
        #
        #   1) Erhaltene Daten mit Template aus JSON auf Richtigkeit prüfen
        #   2) Update oder neues Element hinzufügen?
        #   => 2.1) Update:
        #       - Muss die "Projektdaten.json" auch geändert werden?
        #       => ja:
        #           - Alte Daten zwischenspeichern und Neue Daten updaten
        #           - "Projektdaten.json" updaten
        #           - Alles ok, es passiert nichts [Application erkennt das]
        #       => nein:
        #           - Neue Daten updaten
        #           - Alles ok, es passiert nichts [Application erkennt das]
        #   => 2.2) Neu:
        #       - Index für neuen Eintrag herausfinden
        #       - Neue Daten eintragen mit neuem Index
        #       - Alles ok, es passiert nichts [Application erkennt das]
        #

        file_path = filename[0].lower() + filename[1::]
        file_path = self.data_path + file_path + ".json"

        # Validierung der JSON-Datei
        data = self.validate_integrity(file_path)

        elements = [x for x in data["Elements"]]
        templates = [x for x in data["Template"]]
        json_data = [x for x in json_dict]


        # 1) Auf Richtigkeit prüfen (alles Template-Items erfüllt und nicht doppelt!)
        # 1.1) Beide Dicts gleich lang (muss, sonst falsches JSON übergeben)
        if len(templates) != len(json_data):
            raise Exception()
        else:
            # 1.2) Beide Keys der Dicts auch gleich (muss, sonst falsches JSON übergeben)
            for x in range(0, len(templates)):
                if templates[x] != json_data[x]:
                    raise Exception()

        gefunden = False
        update_elem = None
        for elem in elements:
            if str(data["Elements"][elem]["unique_id"]) == json_dict["unique_id"]:
                update_elem = elem
                gefunden = True


        # 2) Update oder neues Element?
        if update:
            # 2.1) Update
            if not gefunden:
                # Objekt hat keine gültige unique_id, ggf anders reagieren?
                raise Exception()

            if (filename != "Projektdaten"):
                # Projektdaten mitändern!
                project_path = self.data_path + "projektdaten.json"

                # Validierung der JSON-Datei
                project_data = self.validate_integrity(file_path)

                # Alte ID abspeichern nach der gesucht werden soll!
                alte_id = data["Elements"][elem]["unique_id"]

                if filename == "Kundendaten":
                    # Nur nach Kunden-ID suchen
                    for elem in project_data["Elements"]:
                        if str(project_data["Elements"][elem]["unique_id"]) == alte_id:
                            # Alte ID gefunden -> durch neue ID ersetzen
                            project_data["Elements"][elem]["unique_id"] = json_dict["unique_id"]
                else:
                    # Nach allen Vorkommen der Mitarbeiter-ID suchen
                    for elem in project_data["Elements"]:
                        # 1. in Liste project_data["Elements"][elem]["mitarbeiter_ids"] gucken
                        alle_ids = project_data["Elements"][elem]["mitarbeiter_ids"]
                        if alte_id in alle_ids:
                            project_data["Elements"][elem]["mitarbeiter_ids"][alle_ids.index(alte_id)] = json_dict["unique_id"]

                        # 2. in allen Elementen n von project_data["Elements"][elem]["zuordnung_arbeit"]
                        #   => in Liste ...[elem]["zuordnung_arbeit"][n]["mitarbeiter_ids"] gucken
                        for key in project_data["Elements"][elem]["zuordnung_arbeit"]:
                            alle_ids = project_data["Elements"][elem]["zuordnung_arbeit"][key]["mitarbeiter_ids"]
                            if alte_id in alle_ids:
                                project_data["Elements"][elem]["zuordnung_arbeit"][key]["mitarbeiter_ids"][alle_ids.index(alte_id)] = json_dict["unique_id"]

                with open(project_path, "w") as project_file:
                    json.dump(project_data, project_file)

            # Projektdaten: d.h. es muss nichts anderes geändert werden
            data["Elements"][elem] = json_dict
            with open(file_path, "w") as json_file:
                json.dump(data, json_file)
            return

        # 2.2) Neu
        # DISCLAIMER: Wenn neue Projekte hinzugefügt werden nicht prüfen ob Kunden/ Mitarbeiter exisiteren!

        if gefunden:
            # Objekt mit der unique_id gibt es schon, ggf anders reagieren?
            raise Exception()

        letzte = -1
        for elem in elements:
            index = int(elem)
            letzte = index if (index > letzte) else letzte

        letzte += 1
        data["Elements"][str(letzte)] = json_dict

        with open(file_path, "w") as json_file:
            json.dump(data, json_file)
