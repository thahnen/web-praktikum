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
    <div class="div--header">
        <h1 id="headline">Auswertung</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--tbl">
        % for object_key in data_o:
        <h2 id="${object_key}_header">Projekt: ${data_o[object_key]["unique_id"]} [ausklappen]</h2>
        <table class="tbl--projects">
            % for elem in data_o[object_key]:
            % if elem != "unique_id":
            <tr class="tbl--data">
                <td class="tbl--data--elem">
                    % if elem == "nummer":
                    <h4>Interne Projekt-Nummer: ${data_o[object_key][elem]}</h4>
                    % elif elem == "bezeichnung":
                    <h4>Projektbezeichnung: ${data_o[object_key][elem]}</h4>
                    % elif elem == "beschreibung":
                    <h4>Projektbeschreibung: ${data_o[object_key][elem]}</h4>
                    % elif elem == "bearbeitungszeitraum":
                    <h4>Bearbeitungszeitraum: ${data_o[object_key][elem]} Wochen</h4>
                    % elif elem == "budget":
                    <h4>Budget: ${data_o[object_key][elem]} US$</h4>
                    % elif elem == "kunden_id":
                    <h4 class="${elem}">Kunde: ${data_o[object_key][elem]["unique_id"]} [ausklappen]</h4>
                    <div class="${elem}_info">
                        <ul>
                            <li>${data_o[object_key][elem]["bezeichnung"]} (Ansprechpartner: ${data_o[object_key][elem]["ansprechpartner"]})</li>
                            <li>
                                <a href="/kundendaten/${data_o[object_key][elem]["unique_id"]}">Direkter Link zum Kunden</a>
                            </li>
                        </ul>
                    </div>
                    % elif elem == "mitarbeiter_ids":
                    <h4 class="${elem}">Beteiligte Mitarbeiter: [ausklappen]</h4>
                    <div class="${elem}_info">
                        <ul>
                            % for m_id in data_o[object_key][elem]:
                            <li>
                                <a href="/mitarbeiterdaten/${m_id["unique_id"]}">(${m_id["unique_id"]}) ${m_id["name"]}, ${m_id["vorname"]}</a>
                            </li>
                            % endfor
                        </ul>
                    </div>
                    % elif elem == "zuordnung_arbeit":
                    <h4 class="${elem}">Wocheneinteilung der Arbeit: [ausklappen]</h4>
                    <div class="${elem}_info">
                        <p>Stundenaufwand über alle Wochen: ${data_o[object_key][elem]["gesamt_anzahl"]} (Stunden)</p>
                        <table>
                            <tr>
                                <th>Id / Woche</th>
                                % for week in range(data_o[object_key]["bearbeitungszeitraum"]):
                                <th>Woche ${week}</th>
                                % endfor
                            </tr>
                            % for elem_i in data_o[object_key][elem]:
                            % if elem_i != "gesamt_anzahl" and elem_i == "gesamt_woche_n":
                            <tr>
                                <th>Gesamt pro Woche</th>
                                % for week in range(int(data_o[object_key]["bearbeitungszeitraum"])):
                                <td>${data_o[object_key][elem][elem_i][week]}</td>
                                % endfor
                            </tr>
                            % elif elem_i != "gesamt_anzahl":
                            <tr>
                                <th>${elem_i}</th>
                                % for week in range(int(data_o[object_key]["bearbeitungszeitraum"])):
                                <td>${data_o[object_key][elem][elem_i][week]}</td>
                                % endfor
                            </tr>
                            % endif
                            % endfor
                        </table>
                    </div>
                    % endif
                </td>
            </tr>
            % endif
            % endfor
        </table>
        <br />
        % endfor
    </div>

    <!--<script src="/js/auswertung.js" charset="UTF-8"></script>-->
</body>
</html>
