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
    <title>${data_o["Data"]["unique_id"]}</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/edit.css" />
</head>
<body>
    <!--
        TODO:
        1. Veränderung des Bearbeitungszeitraums verändert Zuordnung Arbeit dynamisch!
        2. Eigene JS/CSS Datei (Mitarbeiter-IDs/Kunden-IDs laden)
        3. Bessere Ansicht
    -->
    <div class="div--header">
        <h1 id="headline">${data_o["Data"]["unique_id"]}</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <h2 class="h2--failure">Fehler</h2>
    </div>

    <div class="div--tbl">
        <table class="tbl--projects">
            <!-- Table Header Row -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endfor
            </tr>

            <!-- Erste Zeile nur mit den Erläuterungen, kann weg -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${key}</th>
                % endfor
            </tr>

            <!-- Table Data Row -->
            <tr class="tbl--data">
                % for key in data_o["Data"]:
                <td class="tbl--data--elem">
                    % if key != "unique_id":
                    <input class="input--data" type="text" value="${data_o["Data"][key]}" disabled required />
                    % else:
                    ${data_o["Data"][key]}
                    % endif
                </td>
                % endfor
            </tr>
        </table>
    </div>

    <%include file="/elements/buttons-edit.tpl"/>

    <!--<script src="/js/edit-projekt.js" charset="utf-8"></script>-->
    <script src="/js/edit.js" charset="UTF-8"></script>
</body>
</html>
