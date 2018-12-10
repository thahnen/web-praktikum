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
        <div class="div--tbl">
            <table class="tbl--projects">
                % for key in data_o["Template"]:
                <tr>
                    % if key != "zuordnung_arbeit":
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endif


                    % if key == "unique_id":
                    <td class="tbl--data--elem">
                        <input id="${key}" class="input--data" type="text" value="Ich werde autogeneriert" required disabled />
                    </td>
                    % elif key == "nummer":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="nummer" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "bezeichnung":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="bezeichnung" class="input--data" type="text" value="${key}" required />
                    </td>
                    % elif key == "beschreibung":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="beschreibung" class="input--data" type="text" value="${key}" required />
                    </td>
                    % elif key == "bearbeitungszeitraum":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="bearbeitungszeitraum" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "budget":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="budget" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "kunden_id":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="kunden_id" type="number" min="1" value="1" required />
                    </td>
                    % elif key == "mitarbeiter_ids":
                    <td class="tbl--data--elem">
                        <input id="${key}" name="mitarbeiter_ids" class="input--data" type="text" value="${key} mit Kommata getrennt angeben" required />
                    </td>
                    % elif key != "zuordnung_arbeit":
                    <td class="tbl--data--elem">
                        <input class="input--data" type="text" value="${key}" required />
                    </td>
                    % endif
                </tr>
                % endfor:
            </table>
        </div>

        <div class="div--btn">
            <input type="submit" id="btn--add" value="Zuordnung Arbeit erstellen">
        </div>
    </form>
</body>
</html>
