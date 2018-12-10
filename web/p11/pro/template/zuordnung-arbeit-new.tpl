## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Projektdaten: Neu hinzufügen</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Projektdaten: Neu hinzufügen</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Projektdaten_Add" method="post">
        <%include file="/elements/zuordnung-arbeit-form.tpl"/>
    </form>
</body>
</html>
