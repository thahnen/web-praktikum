## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Projektdaten: Neu hinzufügen</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Projektdaten: Neu hinzufügen</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Projektdaten_Add" method="post">
        <div class="div--tbl">
            <table class="tbl--projects">
                % for key in data_o["Template"]:
                <tr>
                    % if key != "zuordnung_arbeit":
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endif

                    % if key == "unique_id":
                    <td class="tbl--data--elem">
                        <input class="input--data" type="text" value="Ich werde autogeneriert" required disabled />
                    </td>
                    % elif key == "nummer":
                    <td class="tbl--data--elem">
                        <input name="nummer" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "bezeichnung":
                    <td class="tbl--data--elem">
                        <input name="bezeichnung" class="input--data" type="text" value="${key}" required />
                    </td>
                    % elif key == "beschreibung":
                    <td class="tbl--data--elem">
                        <input name="beschreibung" class="input--data" type="text" value="${key}" required />
                    </td>
                    % elif key == "bearbeitungszeitraum":
                    <td class="tbl--data--elem">
                        <input name="bearbeitungszeitraum" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "budget":
                    <td class="tbl--data--elem">
                        <input name="budget" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "kunden_id":
                    <td class="tbl--data--elem">
                        <input name="kunden_id" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "mitarbeiter_ids":
                    <td class="tbl--data--elem">
                        <input name="mitarbeiter_ids" class="input--data" type="text" value="${key} mit Kommata getrennt angeben" required />
                    </td>
                    % elif key != "zuordnung_arbeit":
                    <td class="tbl--data--elem">
                        <input class="input--data" type="text" value="${key}" required />
                    </td>
                    % endif
                </tr>
                % endfor:
            </table>
        </div>
        <div class="div--btn">
            <input type="submit" id="btn--add" value="Zuordnung Arbeit erstellen">
        </div>
    </form>
</body>
</html>
