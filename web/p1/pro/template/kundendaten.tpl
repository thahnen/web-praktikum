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
    <title>Kundendaten</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="css/view.css" />
</head>
<body>
    <div class="div--header">
        <h1>Kundendaten: Überblick</h1>
    </div>

    <div class="div--navbar">
        <ul class="ul--navbar">
            <li><a href="/">Index</a></li>
            <li><a href="/projektdaten">Projektdaten</a></li>
            <li><a href="/kundendaten">Kundendaten</a></li>
            <li><a href="/mitarbeiterdaten">Mitarbeiterdaten</a></li>
        </ul>
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

            <!-- Table Elements Row -->
            % for object in data_o["Elements"]:
            <tr class="tbl--data">
                % for object_key in data_o["Elements"][object]:
                <td class="tbl--data--elem">
                    % if object_key == "unique_id":
                    <a href="/kundendaten?kunden_id=${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a>
                    % else:
                    ${data_o["Elements"][object][object_key]}
                    % endif
                </td>
                % endfor
            </tr>
            % endfor
        </table>
    </div>

    <p id="p--new">Neues Element hinzufügen</p>
    <div class="div--new">
        <!-- Neues Element hinzufügen mittels ausklappbarem Div -->
        <!-- Wenn auf "Neues Element hinzufügen" gedrückt wurde -->
        <ul>
            <!-- li's ebenfalls generieren! -->
            <li>
                <input class="input--data" type="text" name="" value="Test123">
            </li>
        </ul>
        <button type="button" id="btn--new">
            <span>Hinzufügen</span>
        </button>
    </div>

    <script src="js/view.js" charset="UTF-8"></script>
</body>
</html>
