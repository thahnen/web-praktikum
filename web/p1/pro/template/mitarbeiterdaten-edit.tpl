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
    <title>Mitarbeiterdaten: ${data_o["Data"]["unique_id"]}</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="css/edit.css" />
    <script src="js/edit.js" charset="UTF-8"></script>
</head>
<body>
    <div class="div--header">
        <h1>Mitarbeiterdaten: ${data_o["Data"]["unique_id"]}</h1>
    </div>

    <div class="div--navbar">
        <ul class="ul--navbar">
            <li>
                <a href="/">Index</a>
            </li>
            <li>
                <a href="/projektdaten">Projektdaten</a>
            </li>
            <li>
                <a href="/kundendaten">Kundendaten</a>
            </li>
            <li>
                <a href="/mitarbeiterdaten">Mitarbeiterdaten</a>
            </li>
        </ul>
    </div>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
        <h2 class="h2--failure">Speichern fehlgeschlagen!</h2>
    </div>

    <div class="div--tbl">
        <table>
            <!-- Table Header Row -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${key}</th>
                % endfor
            </tr>
            <!-- Erste Zeile nur mit den Erläuterungen, kann weg -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endfor
            </tr>

            <!-- Table Data Row -->
            <tr class="tbl--data">
                % for key in data_o["Data"]:
                <td class="tbl--data--elem">
                    % if key != "unique_id":
                    <input class="input--data" type="text" value="${data_o["Data"][key]}" disabled required>
                    % else:
                    ${data_o["Data"][key]}
                    % endif
                </td>
                % endfor
            </tr>
        </table>
    </div>

    <div class="div--btn">
        <button type="button" id="btn--edit">
            <span>Editieren</span>
        </button>
        <button type="button" id="btn--save">
            <span>Speichern</span>
        </button>
    </div>
</body>
</html>
