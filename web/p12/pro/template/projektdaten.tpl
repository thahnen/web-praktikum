## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>: Übersicht</title>
    <script type="module" src="/js/view.js" charset="UTF-8"></script>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">: Übersicht</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <%include file="/elements/failure.tpl"/>
    <div class="div--tbl">
        <table class="tbl--projects">
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

            % for object_key in data_o["Elements"]:
            <tr class="tbl--data">
                % for elem in data_o["Elements"][object_key]:
                % if elem == "kunden_id":
                <td class="tbl--data--elem">
                    <a href="/kundendaten/${data_o["Elements"][object_key][elem]}">${data_o["Elements"][object_key][elem]}</a>
                </td>
                % elif elem == "mitarbeiter_ids":
                <td class="tbl--data--elem">
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
    <%include file="/elements/buttons-view.tpl"/>
</body>
</html>
