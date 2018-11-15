## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<%include file="/elements/header-new.tpl"/>
<body>
    <div class="div--header">
        <!-- Später Headline generieren damit man nur ein Template braucht! -->
        <h1 id="headline">: Neu hinzufügen</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
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
                % for key in data_o["Template"]:
                <td class="tbl--data--elem">
                    <input class="input--data" type="text" value="${key}" required />
                </td>
                % endfor
            </tr>
        </table>
    </div>

    <%include file="/elements/buttons-new.tpl"/>

    <script src="/js/new.js" charset="UTF-8"></script>
</body>
</html>
