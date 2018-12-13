## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    % if data_o["erfolgreich"]:
    <title>Erfolgreich :)</title>
    % else:
    <title>Nicht erfolgreich :(</title>
    %endif
</head>
<body>
    <div class="div--header">
        % if data_o["erfolgreich"]:
        <h1 id="headline">Erfolgreich :)</h1>
        % else:
        <h1 id="headline">Nicht erfolgreich :(</h1>
        %endif
    </div>
    <%include file="/elements/navbar.tpl"/>
    <div>
        % if data_o["erfolgreich"]:
        <h2>Die durchgeführte Funktion war erfolgreich :)</h2>
        % else:
        <h2>Die durchgeführte Funktion war nicht erfolgreich :(</h2>
        <h3>Haben sie vielleicht falsche Werte angegeben oder wird das von ihnen ausgewählte Element verwendet?</h3>
        %endif
    </div>
</body>
</html>
