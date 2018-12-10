## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Bearbeiten: ${data_o["Data"]["unique_id"]}</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Bearbeiten: ${data_o["Data"]["unique_id"]}</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Projektdaten_Update" method="post">
        <div class="div--tbl">
            <table class="tbl--projects">
                % for key in data_o["Template"]:
                <tr>
                    % if key != "zuordnung_arbeit":
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endif

                    % if key == "unique_id":
                    <td class="tbl--data--elem">
                        <input class="input--data" type="text" value="${data_o["Data"][key]}" required disabled />
                        <input type="hidden" name="unique_id" value="${data_o["Data"][key]}">
                    </td>
                    % elif key == "nummer":
                    <td class="tbl--data--elem">
                        <input name="nummer" class="input--data input--edit" type="number" min="1" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "bezeichnung":
                    <td class="tbl--data--elem">
                        <input name="bezeichnung" class="input--data input--edit" type="text" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "beschreibung":
                    <td class="tbl--data--elem">
                        <input name="beschreibung" class="input--data input--edit" type="text" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "bearbeitungszeitraum":
                    <td class="tbl--data--elem">
                        <input name="bearbeitungszeitraum" class="input--data input--edit" type="number" min="1" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "budget":
                    <td class="tbl--data--elem">
                        <input name="budget" class="input--data input--edit" type="number" min="1" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "kunden_id":
                    <td class="tbl--data--elem">
                        <input name="kunden_id" class="input--data input--edit" type="number" min="1" value="${data_o["Data"][key]}" required />
                    </td>
                    % elif key == "mitarbeiter_ids":
                    <td class="tbl--data--elem">
                        <input name="mitarbeiter_ids" class="input--data" type="text" value="${str(data_o["Data"][key]).strip("[]")}" required />
                        <input name="zuordnung_arbeit" class="input--data" type="hidden" value="${data_o["Data"]["zuordnung_arbeit"]}" required />
                        <input type="hidden" name="not_done" value="true">
                    </td>
                    % endif
                </tr>
                % endfor:
            </table>
        </div>
        <div class="div--btn">
            <input type="submit" id="btn--update" value="Zuordnung Arbeit bearbeiten">
        </div>
    </form>
</body>
</html>
