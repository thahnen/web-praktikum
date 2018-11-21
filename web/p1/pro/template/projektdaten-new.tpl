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
    <title>Projektdaten: Neu hinzufügen</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
    <!--<link rel="stylesheet" type="text/css" href="/css/p-edit-new.css">-->
</head>
<body>
    <!--
        TODO:
        1. Veränderung des Bearbeitungszeitraums verändert Zuordnung Arbeit dynamisch!
        2. Eigene JS/CSS Datei (Mitarbeiter-IDs/Kunden-IDs laden)
        3. Bessere Ansicht, beide Spalten jeweils 50% gross
    -->
    <div class="div--header">
        <h1 id="headline">Projektdaten: Neu hinzufügen</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <h2 class="h2--failure">Fehler</h2>
    </div>

    <div class="div--tbl">
        <table class="tbl--projects">
            % for key in data_o["Template"]:
            <tr>
                % if key == "kunden_id":
                <!-- Kunden-ID -->
                <th class="tbl--header--elem">
                    Kunden-ID:<br/>
                    (Keine Mehrfachauswahl möglich!)<br/>
                    (List[kunden_id])
                </th>

                % elif key == "mitarbeiter_ids":
                <!-- Liste mit allen Mitarbeiter-IDs -->
                <th class="tbl--header--elem">
                    Mitarbeiterliste:<br/>
                    (Mehrfachauswahl möglich!)<br/>
                    (List[mitarbeiter_id])
                </th>

                % elif key == "zuordnung_arbeit":
                <!-- Zuordnung Arbeit -->
                <th class="tbl--header--elem">
                    Tabelle mit, den jeweiligen Mitarbeitern,<br/>
                    zugeordneten Wochenstunden<br/>
                    (List[mitarbeiter_id -> List[int]])
                </th>

                % else:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endif


                % if key == "bearbeitungszeitraum" or key == "nummer":
                <td class="tbl--data--elem">
                    <input type="number" min="1" value="1" />
                </td>
                % elif key == "kunden_id":
                <!-- Kunden-ID -->
                <td class="tbl--data--elem">
                    <select name="kunden_id" size="5">
                        <!--
                            Elemente werden aus Kunden-IDs autogeneriert!
                            Nur eine Option auswählbar, Abruf alle paar Sekunden?
                            Nach dem Schema:
                            <option value="kunden_id">Name, Vorname (kunden_id)</option>
                        -->
                    </select>
                </td>

                % elif key == "mitarbeiter_ids":
                <!-- Liste mit allen Mitarbeiter-IDs -->
                <td class="tbl--data--elem">
                    <select name="mitarbeiter_ids" size="5" multiple>
                        <!--
                            Elemente werden aus Mitarbeiter-IDs autogeneriert!
                            Nur eine Option auswählbar, Abruf alle paar Sekunden?
                            Nach dem Schema:
                            <option value="mitarbeiter_id">Name, Vorname (mitarbeiter_id)</option>
                        -->
                    </select>
                </td>
                % elif key == "zuordnung_arbeit":
                <td class="tbl--data--elem">
                    <table>
                        <!--
                            Zuordnung der Mitarbeiter und Wochenstunden.
                            Autogeneriert je nachdem wie viele Wochenstunden.
                            Nach dem Schema:
                            <tr>
                                <th>mitarbeiter_id</th>
                                <td>Stunden Woche 1</td>
                                <td>Stunden Woche 2</td>
                                <td>...</td>
                            </tr>
                        -->
                    </table>
                </td>
                % else:
                <td class="tbl--data--elem">
                    <input class="input--data" type="text" value="${key}" required />
                </td>
                % endif
            </tr>
            % endfor:
        </table>
    </div>

    <%include file="/elements/buttons-new.tpl"/>

    <!--<script src="/js/new-projekt.js" charset="utf-8"></script>-->
</body>
</html>
