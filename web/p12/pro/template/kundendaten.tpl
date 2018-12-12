## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>: Übersicht</title>
    <script type="module" src="/js/view.js" charset="UTF-8"></script>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">: Übersicht</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <%include file="/elements/failure.tpl"/>
    <div class="div--tbl">
        <table>
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endfor
            </tr>

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
</body>
</html>
