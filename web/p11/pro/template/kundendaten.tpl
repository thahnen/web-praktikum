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
    <title>Kundendaten: Übersicht</title>
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Kundendaten: Übersicht</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <form action="/POST_Kundendaten_Delete" method="post">
        <div class="div--tbl">
            <table>
                <!-- Table Header Row -->
                <tr class="tbl--header">
                    % for key in data_o["Template"]:
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endfor
                </tr>

                <!-- Table Elements Row -->
                % for object in data_o["Elements"]:
                <tr class="tbl--data">
                    % for object_key in data_o["Elements"][object]:
                    % if object_key == "unique_id":
                    <td class="tbl--data--elem">
                        <input type="checkbox" name="delete_unique_id" value="${data_o["Elements"][object][object_key]}">
                        <a href="/kundendaten/${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a>
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
            <p>
                <a href="/kundendaten/neu">Neu Hinzufügen</a>
            </p>
        </div>
    </form>
</body>
</html>
