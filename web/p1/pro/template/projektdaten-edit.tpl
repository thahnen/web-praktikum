## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<%include file="header-edit.tpl"/>
<body>
    <div class="div--header">
        <h1 id="headline">${data_o["Data"]["unique_id"]}</h1>
    </div>

    <%include file="navbar.tpl"/>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
        <h2>Speichern fehlgeschlagen!</h2>
    </div>

    <div class="div--tbl">
        <table>
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

    <%include file="buttons-edit.tpl"/>

    <script src="js/edit.js" charset="UTF-8"></script>
</body>
</html>
