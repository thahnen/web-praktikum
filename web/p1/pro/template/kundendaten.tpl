## coding: utf-8
<%doc>
    Template für die Kundendaten
    - vlt. noch Veränderungen am Head-Teil?
    - mehr Sachen im Body neben der Tablle?
    - Weitere Elemente in der JSON-Datei, damit es übersichtlicher wird?
    => ausschliesslich für Aufgabe 1!
</%doc>

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

    <!-- Das Favicon für alles den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <!--<link rel="stylesheet" type="text/css" href="css/kundendaten.css" />-->

    <!--<script src="js/kundendaten.js"></script>-->
</head>
<body>
    <h1>Kundendaten</h1>
    <table>
        <!-- Table Header Row -->
        <tr>
            % for key in data_o["Template"]:
            <th>${key}</th>
            % endfor
        </tr>
        <!-- Erste Zeile nur mit den Erläuterungen, kann weg -->
        <tr>
            % for key in data_o["Template"]:
            <th>${data_o["Template"][key]}</th>
            % endfor
        </tr>

        <!-- Table Elements Row -->
        % for object in data_o["Elements"]:
        <tr>
            % for object_key in data_o["Elements"][object]:
            <td>${data_o["Elements"][object][object_key]}</td>
            % endfor
        </tr>
        % endfor
    </table>
</body>
</html>
