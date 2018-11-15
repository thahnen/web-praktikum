## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<%include file="/elements/header-view.tpl"/>
<body>
    <div class="div--header">
        <h1 id="headline">: Übersicht</h1>
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

            <!-- Table Elements Row -->
            % for object in data_o["Elements"]:
            <tr class="tbl--data">
                % for object_key in data_o["Elements"][object]:
                <td class="tbl--data--elem">${data_o["Elements"][object][object_key]}</td>
                % endfor
            </tr>
            % endfor
        </table>
    </div>

    <%include file="/elements/buttons-view.tpl"/>

    <script src="/js/view.js" charset="UTF-8"></script>
</body>
</html>
