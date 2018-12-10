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
    <title>Projektdaten: Neu hinzufügen</title>
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/standard.css" />
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Projektdaten: Neu hinzufügen</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <form action="/POST_Projektdaten_Add" method="post">
        <!-- -->
        % for key in data_o:
        % if key == "mitarbeiter_ids":
        <input type="hidden" name="${key}" value="${data_o[key]}">
        <table>
            <tr>
                <th>ID / Woche</th>
                % for woche in range(1, data_o["bearbeitungszeitraum"]+1):
                <th>Woche ${woche}</th>
                % endfor
            </tr>

            % for mitarbeiter in range(0, len(data_o[key])):
            <tr>
                <td>${data_o[key][mitarbeiter]}</td>
                % for woche in range(1, data_o["bearbeitungszeitraum"]+1):
                <td>
                    <input type="number" name="zuordnung_arbeit" value="">
                </td>
                % endfor
            </tr>
            % endfor
        </table>
        % else:
        <input type="hidden" name="${key}" value="${data_o[key]}">
        % endif
        % endfor

        <div class="div--btn">
            <input type="submit" id="btn--add" value="Hinzufügen">
        </div>
    </form>
</body>
</html>
