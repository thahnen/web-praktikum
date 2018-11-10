## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<head>
    <meta charset="utf-8" />
    <meta name="robots" content="noindex,nofollow" />
    <meta http-equiv="expires" content="0" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <meta name="format-detection" content="telephone=no" />
    <meta name="author" content="Tobias Hahnen" />
    <!-- Später Titel generieren damit man nur ein Template braucht! -->
    <title>Mitarbeiterdaten</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/view.css" />
</head>
<body>
    <div class="div--header">
        <!-- Später Headline generieren damit man nur ein Template braucht! -->
        <h1>Mitarbeiterdaten: Überblick</h1>
    </div>

    <%include file="navbar.tpl"/>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
        <h2 class="h2--failure">Neu hinzufügen fehlgeschlagen!</h2>
    </div>

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
                <td class="tbl--data--elem">
                    % if object_key == "unique_id":
                    <!-- muss noch an jeweiligen Link angepasst werden (Kundendaten bzw. Mitarbeiterdaten) -->
                    <a class="a--elem" href="/mitarbeiterdaten/${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a>
                    % else:
                    ${data_o["Elements"][object][object_key]}
                    % endif
                </td>
                % endfor
            </tr>
            % endfor

            <!-- Kommt in ein eigenes aufklappbares Div! -->
            <!-- Leeres Element zum hinzufügen -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">
                    <input class="input--new" type="text" value="<${key}>" required />
                </th>
                % endfor
            </tr>
        </table>
    </div>

    <div class="div--btn">
        <button type="button" id="btn--new">
            <span>Neu hinzufügen</span>
        </button>
    </div>

    <script src="/js/view.js" charset="UTF-8"></script>
</body>
</html>
