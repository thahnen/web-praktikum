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
    <title>Mitarbeiterdaten: Neu hinzufügen</title>
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Mitarbeiterdaten: Neu hinzufügen</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <form action="/POST_Mitarbeiterdaten_Add" method="post">
        <div class="div--tbl">
            <table>
                <!-- Table Header Row -->
                <tr class="tbl--header">
                    % for key in data_o["Template"]:
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endfor
                </tr>

                <!-- Table Data Row -->
                <tr class="tbl--data">
                    % for key in data_o["Template"]:
                    <td class="tbl--data--elem">
                        % if key == "unique_id":
                        <input class="input--data" type="text" value="Wird Autogeneriert ;)" required disabled />
                        % else:
                        <input class="input--data input--edit" type="text" name="${key}" value="${key}" required />
                        % endif
                    </td>
                    % endfor
                </tr>
            </table>
        </div>

        <div class="div--btn">
            <input type="submit" id="btn--add" value="Hinzufügen">
        </div>
    </form>
</body>
</html>
