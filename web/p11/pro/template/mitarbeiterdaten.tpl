## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Mitarbeiterdaten: Übersicht</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Mitarbeiterdaten: Übersicht</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Mitarbeiterdaten_Delete" method="post">
        <div class="div--tbl">
            <table>
                <tr class="tbl--header">
                    % for key in data_o["Template"]:
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endfor
                </tr>

                % for object in data_o["Elements"]:
                <tr class="tbl--data">
                    % for object_key in data_o["Elements"][object]:
                    % if object_key == "unique_id":
                    <td class="tbl--data--elem">
                        <input type="radio" name="delete_unique_id" value="${data_o["Elements"][object][object_key]}">
                        <a href="/mitarbeiterdaten/${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a>
                    </td>
                    % else:
                    <td class="tbl--data--elem">${data_o["Elements"][object][object_key]}</td>
                    % endif
                    % endfor
                </tr>
                % endfor
            </table>
        </div>
        <div class="div--btn">
            <input type="submit" id="btn--delete" value="Löschen">
            <p><a href="/mitarbeiterdaten/neu">Neu Hinzufügen</a></p>
        </div>
    </form>
</body>
</html>
