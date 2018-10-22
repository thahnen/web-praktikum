## coding: utf-8
<%doc>
    Template für die Projektdaten
    - vlt. noch Veränderungen am Head-Teil?
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
  <title>Projektdaten</title>

  <!-- Das Favicon für alles den Tab, einfach von der HS geklaut :p -->
  <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
  <link rel="stylesheet" type="text/css" href="css/projektdaten.css" />

  <script src="js/projektdaten.js"></script>
</head>
<body>
  <h1>Projektdaten</h1>
  <table>
    <!-- Table Header Row -->
    <tr>
      % for key in data_o["template"]
      <th>${data_o["template"][key]}</th>
      % endfor
    </tr>

    <!-- Table Element Rows -->
    % for object in data_o["elements"]
    <tr>
      % for object_key in data_o["elements"][object]
      <td>${data_o["elements"][object][object_key]}</td>
      % endfor
    </tr>
    % endfor
  </table>
</body>
</html>
