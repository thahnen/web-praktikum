## coding: utf-8
<%doc>
    Template für die Mitarbeiterdaten
    - mehr Sachen im Body neben der Tablle?
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
    <title>Mitarbeiterdaten</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="css/view.css" />
    <script src="js/view.js" charset="UTF-8"></script>
</head>
<body>
    <%doc>
        Nav-Bar einfügen!
    </%doc>

    <h1>Mitarbeiterdaten</h1>
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
            % if object_key == "unique_id":
            <td><a href="/mitarbeiterdaten?mitarbeiter_id=${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a></td>
            % else:
            <td>${data_o["Elements"][object][object_key]}</td>
            % endif
            % endfor
        </tr>
        % endfor
    </table>
</body>
</html>
