## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>: Neu hinzufügen</title>
    <script type="module" src="/js/new.js" charset="UTF-8"></script>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">: Neu hinzufügen</h1>
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
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem tbl--header--info">${key}</th>
                % endfor
            </tr>

            <tr class="tbl--data">
                % for key in data_o["Template"]:
                <td class="tbl--data--elem">
                    % if key == "unique_id":
                    <input class="input--data" type="text" value="Wird Autogeneriert ;)" required disabled />
                    % else:
                    <input class="input--data input--edit" type="text" value="${key}" required />
                    % endif
                </td>
                % endfor
            </tr>
        </table>
    </div>
    <%include file="/elements/buttons-new.tpl"/>
</body>
</html>
