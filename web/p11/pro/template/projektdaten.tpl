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
    <title>Projektdaten: Übersicht</title>
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Projektdaten: Übersicht</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <form action="/POST_Projektdaten_Delete" method="post">
        <div class="div--tbl">
            <!-- ganz aussen ein Form drumherum und in den Table Elements Row je eine Checkbox -->
            <table class="tbl--projects">
                <!-- Table Header Row -->
                <tr class="tbl--header">
                    % for key in data_o["Template"]:
                    % if key == "zuordnung_arbeit":
                    <th class="tbl--header--elem">
                        Tabelle mit, den jeweiligen Mitarbeitern,<br/>
                        zugeordneten Wochenstunden<br/>
                        (List[mitarbeiter_id -> List[int]])
                    </th>
                    % else:
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endif
                    % endfor
                </tr>

                <!-- Table Data Row -->
                % for object_key in data_o["Elements"]:
                <tr class="tbl--data">
                    % for elem in data_o["Elements"][object_key]:
                    % if elem == "unique_id":
                    <td class="tbl--data--elem">
                        <input type="checkbox" name="delete_unique_id" value="${data_o["Elements"][object_key][elem]}">
                        <a href="/projektdaten/${data_o["Elements"][object_key][elem]}">${data_o["Elements"][object_key][elem]}</a>
                    </td>
                    % elif elem == "kunden_id":
                    <td class="tbl--data--elem">
                        <!-- Link zu dem jeweiligen Kunden -->
                        <a href="/kundendaten/${data_o["Elements"][object_key][elem]}">${data_o["Elements"][object_key][elem]}</a>
                    </td>
                    % elif elem == "mitarbeiter_ids":
                    <td class="tbl--data--elem">
                        <!-- Liste (oder ggf Tabelle) mit allen Mitarbeitern -->
                        <ul class="ul--mitarbeiter">
                            % for id in data_o["Elements"][object_key][elem]:
                            <li class="li--mitarbeiter">
                                <a href="/mitarbeiterdaten/${id}">${id}</a>
                            </li>
                            % endfor
                        </ul>
                    </td>
                    % elif elem == "zuordnung_arbeit":
                    <td class="tbl--data--elem">
                        <!-- Tabelle mit allen Mitarbeitern => Arbeitsstunden -->
                        <table class="tbl--zuordnung">
                            % for id in data_o["Elements"][object_key][elem]:
                            <tr class="tbl--zuordnung--row">
                                <th class="tbl--zuordnung--row--header">
                                    <a href="/mitarbeiterdaten/${id}">${id}</a>
                                </th>
                                % for stunden in data_o["Elements"][object_key][elem][id]:
                                <td class="tbl--zuordnung--row--data">${stunden}</td>
                                % endfor
                            </tr>
                            % endfor
                        </table>
                    </td>
                    % else:
                    <td class="tbl--data--elem">${data_o["Elements"][object_key][elem]}</td>
                    % endif
                    % endfor
                </tr>
                % endfor
            </table>
        </div>

        <div class="div--btn">
            <input type="submit" id="btn--delete" value="Löschen">
            <p>
                <a href="/projektdaten/neu">Neu Hinzufügen</a>
            </p>
        </div>
    </form>
</body>
</html>
