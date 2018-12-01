## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<%include file="/elements/header-edit.tpl"/>
<body>
    <div class="div--header">
        <h1 id="headline">${data_o["Data"]["unique_id"]}</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <h2 class="h2--failure">Fehler</h2>
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
                <th class="tbl--header--elem tbl--header--info">${key}</th>
                % endfor
            </tr>

            <!-- Table Data Row -->
            <tr class="tbl--data">
                % for key in data_o["Data"]:
                <td class="tbl--data--elem">
                    % if key == "unique_id":
                    <input class="input--data" type="text" value="${data_o["Data"][key]}" required disabled />
                    % else:
                    <input class="input--data input--edit" type="text" value="${data_o["Data"][key]}" required />
                    % endif
                </td>
                % endfor
            </tr>
        </table>
    </div>

    <%include file="/elements/buttons-edit.tpl"/>
    <script src="/js/edit.js" charset="UTF-8"></script>
</body>
</html>
