## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>: Neu hinzufügen</title>
    <script type="module" src="/js/new-project.js" charset="utf-8"></script>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">: Neu hinzufügen</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <%include file="/elements/failure.tpl"/>
    <div class="div--tbl">
        <table class="tbl--projects">
            % for key in data_o["Template"]:
            <tr>
                % if key == "kunden_id":
                <th class="tbl--header--elem">
                    Kunden-ID:<br/>
                    (Keine Mehrfachauswahl möglich!)<br/>
                    (List[kunden_id])
                </th>
                % elif key == "mitarbeiter_ids":
                <th class="tbl--header--elem">
                    Mitarbeiterliste:<br/>
                    (Mehrfachauswahl möglich!)<br/>
                    (List[mitarbeiter_id])
                </th>
                % elif key == "zuordnung_arbeit":
                <th class="tbl--header--elem">
                    Tabelle mit, den jeweiligen Mitarbeitern,<br/>
                    zugeordneten Wochenstunden<br/>
                    (List[mitarbeiter_id -> List[int]])
                </th>
                % else:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endif


                % if key == "unique_id":
                <td class="tbl--data--elem">
                    <input id="${key}" class="input--data" type="text" value="Ich werde autogeneriert" required disabled />
                </td>
                % elif key == "nummer":
                <td class="tbl--data--elem">
                    <input id="${key}" type="number" min="1" value="1" required />
                </td>
                % elif key == "bezeichnung":
                <td class="tbl--data--elem">
                    <input id="${key}" class="input--data" type="text" value="${key}" required />
                </td>
                % elif key == "beschreibung":
                <td class="tbl--data--elem">
                    <input id="${key}" class="input--data" type="text" value="${key}" required />
                </td>
                % elif key == "bearbeitungszeitraum":
                <td class="tbl--data--elem">
                    <input id="${key}" type="number" min="1" value="1" required />
                </td>
                % elif key == "budget":
                <td class="tbl--data--elem">
                    <input id="${key}" type="number" min="1" value="1" required />
                </td>
                % elif key == "kunden_id":
                <td class="tbl--data--elem">
                    <select id="select_kunden_id" name="kunden_id" size="5">
                        <!--
                            Elemente werden aus Kunden-IDs autogeneriert!
                            Nur eine Option auswählbar
                            Nach dem Schema:
                            <option value="kunden_id">(kunden_id) Name</option>
                        -->
                    </select>
                </td>
                % elif key == "mitarbeiter_ids":
                <td class="tbl--data--elem">
                    <select id="select_mitarbeiter_ids" name="mitarbeiter_ids" size="5" multiple>
                        <!--
                            Elemente werden aus Mitarbeiter-IDs autogeneriert!
                            Nach dem Schema:
                            <option value="mitarbeiter_id">(mitarbeiter_id) Name</option>
                        -->
                    </select>
                </td>
                % elif key == "zuordnung_arbeit":
                <td class="tbl--data--elem">
                    <table id="zuordnung_arbeit">
                        <!--
                            Zuordnung der Mitarbeiter und Wochenstunden.
                            Autogeneriert je nachdem wie viele Wochenstunden.
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
</body>
</html>
