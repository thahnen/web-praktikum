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
    <title>${data_o["Data"]["unique_id"]}</title>

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
        3. Bessere Ansicht
    -->
    <div class="div--header">
        <h1 id="headline">${data_o["Data"]["unique_id"]}</h1>
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


                % if key == "bearbeitungszeitraum" or key == "nummer" or key == "budget":
                <td class="tbl--data--elem">
                    <input type="number" min="1" value="${data_o["Data"][key]}" />
                </td>
                % elif key == "kunden_id":
                <!-- Kunden-ID -->
                <td class="tbl--data--elem">
                    <select name="kunden_id" size="5">
                        <!--
                            Alle möglichen Kunden anzeigen, schon den highlighten der angegeben ist.
                            GGF irgendwie mitgegeben? Oder per XMLHttpRequest abrufen?
                            Nach dem Schema:
                            <option value="kunden_id">Name, Vorname (kunden_id)</option>
                        -->
                        <option value="${data_o["Data"][key]}" selected>${data_o["Data"][key]}</option>
                    </select>
                </td>

                % elif key == "mitarbeiter_ids":
                <!-- Liste mit allen Mitarbeiter-IDs -->
                <td class="tbl--data--elem">
                    <select name="mitarbeiter_ids" size="5" multiple>
                        <!--
                            Alle möglichen Mitarbeiter anzeigen, schon die highlighten die angegeben sind.
                            GFF irgendwie mitgeben? Oder per XMLHttpRequest abrufen
                            Nach dem Schema:
                            <option value="mitarbeiter_id">Name, Vorname (mitarbeiter_id)</option>
                        -->
                        % for id in data_o["Data"][key]:
                        <option value="${id}" selected>${id}</option>
                        % endfor
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
                        % for zuordnung in data_o["Data"][key]:
                        <tr>
                            <th>${zuordnung}</th>
                            % for stunden in data_o["Data"][key][zuordnung]:
                            <td>
                                <input class="input--data" type="text" value="${stunden}" required />
                            </td>
                            % endfor
                        </tr>
                        % endfor
                    </table>
                </td>
                % else:
                <td class="tbl--data--elem">
                    <input class="input--data" type="text" value="${data_o["Data"][key]}" required />
                </td>
                % endif
            </tr>
            % endfor:
        </table>
    </div>

    <%include file="/elements/buttons-edit.tpl"/>

    <!--<script src="/js/edit-project.js" charset="utf-8"></script>-->
</body>
</html>
