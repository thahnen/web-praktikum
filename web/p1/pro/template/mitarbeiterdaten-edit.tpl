## coding: utf-8
<%doc>
    Template zum editieren einzelner Mitarbeiterdaten!
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
    <title>Mitarbeiterdaten: ${data_o["Data"]["unique_id"]}</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="css/edit.css" />
    <script src="js/edit.js" charset="UTF-8"></script>
</head>
<body>
    <%doc>
        Nav-Bar einfügen!
    </%doc>

    <h1>Mitarbeiterdaten: ${data_o["Data"]["unique_id"]}</h1>
    <div>
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

            <!-- Table Data Row -->
            <tr>
                % for key in data_o["Data"]:
                <td>
                    <input type="text" name="" value="${data_o["Data"][key]}" disabled required>
                </td>
                % endfor
            </tr>
        </table>
    </div>
    <button type="button" id="btn--edit">Editieren</button>
    <button type="button" id="btn--save">Speichern</button>
</body>
</html>
