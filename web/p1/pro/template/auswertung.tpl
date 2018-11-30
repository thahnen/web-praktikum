## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8" />
    <meta name="robots" content="noindex,nofollow" />
    <meta name="expires" content="0" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <meta name="format-detection" content="telephone=no" />
    <meta name="author" content="Tobias Hahnen" />
    <title>Auswertung</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
</head>
<body>
<%doc>
    Genereller Aufbau der Website:
    =============================
    1) Überschrift
    2) Div mit je einer Tabelle pro Projekt, die untereinander angeordnet sind.
        => je eine Tabellen-Reihe pro Information (je nachdem ausklappbar)
        => 1. "unique_id":
            - nicht ausklappbar(?) nur "Projekt-Id: unique_id"
        => 2. "nummer":
            - nicht ausklappbar(?) nur "Interne Projekt-Nummer: nummer"
        => 3. "bezeichnung":
            - Vor dem ausklappen steht da "Projektbezeichnung:" mit Icon zum ausklappen
            - Nach dem ausklappen steht da die jeweilige Bezeichnung und Icon zum einklappen
        => 4. "beschreibung":
            - Vor dem ausklappen steht da "Projektbeschreibung:" mit Icon zum ausklappen
            - Nach dem ausklappen steht da die jeweilige Beschreibung und Icon zum einklappen
        => 5. "bearbeitungszeitraum":
            - nicht ausklappbar(?) nur "Bearbeitungszeitraum: x Wochen"
        => 6. "budget":
            - nicht ausklappbar(?) nur "Budget: x Euro"
        => 7. "kunden_id":
            - Vor dem ausklappen steht da "Kunde:" mit Icon zum ausklappen
            - Nach dem ausklappen steht da die Kundeninformation mit Icon zum einklappen
        => 8. "mitarbeiter_ids":
            - Vor dem ausklappen steht da "Beteiligte Mitarbeiter:" mit Icon zum ausklappen
            - Nach dem ausklappen steht da eine Liste mit Mitarbeiter-Informationen mit Icon zum einklappen
        => 9. "zuordnung_arbeit":
            - Vor dem ausklappen steht da "Wocheneinteilung der Arbeit:" mit Icon zum ausklappen
            - Nach dem ausklappen steht da der gesamte wöchentliche Aufwand und Zuordnung der Mitarbeiter mit Icon zum einklappen
</%doc>

    <div class="div--header">
        <h1 id="headline">Auswertung</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--tbl">
        % for object_key in data_o["Elements"]:
        <table class="tbl--projects">
            % for elem in data_o["Elements"][object_key]:
            <tr class="tbl--data">
                % if elem == "unique_id":
                <p id="${elem}">Projekt-Id: ${data_o["Elements"][object_key][elem]}</p>
                % elif elem == "nummer":
                <p id="${elem}">Interne Projekt-Nummer: ${data_o["Elements"][object_key][elem]}</p>
                % elif elem == "bezeichnung":
                <p id="${elem}">Projektbezeichnung: [Das Icon]</p>
                <p id="${elem}_info"><!-- Ich komme noch --></p>
                % elif elem == "beschreibung":
                <p id="${elem}">Projektbeschreibung: [Das Icon]</p>
                <p id="${elem}_info"><!-- Ich komme noch --></p>
                % elif elem == "bearbeitungszeitraum":
                <p id="${elem}">Bearbeitungszeitraum: ${data_o["Elements"][object_key][elem]} Wochen</p>
                % elif elem == "budget":
                <p id="${elem}">Budget: ${data_o["Elements"][object_key][elem]} Euro</p>
                % elif elem == "kunden_id":
                <p id="${elem}">Kunde: [Das Icon]</p>
                <div id="${elem}_info">
                    <li id="${elem}_info_li">
                        <!-- Hier alle möglichen Attribute -->
                    </li>
                </div>
                % elif elem == "mitarbeiter_ids":
                <p id="${elem}">Beteiligte Mitarbeiter: [Das Icon]</p>
                <div id="${elem}_info">
                    <li id="${elem}_info_li">
                        <!-- Hier je ein <li> für jeden Mitarbeiter? -->
                    </li>
                </div>
                % elif elem == "zuordnung_arbeit":
                <p id="${elem}">Wocheneinteilung der Arbeit: [Das Icon]</p>
                <p id="${elem}_gesamt">Stundenaufwand über gesamte Zeit: <!-- Alle zusammenaddiert --></p>
                <!-- Hier eine Tabelle mit den Zuordnungen sowie für jede Woche insgesamte Anzahl -->
                % endif
            </tr>
            % endfor
        </table>
        % endfor
    </div>

    <!--<script src="/js/auswertung.js" charset="UTF-8"></script>-->
</body>
</html>
