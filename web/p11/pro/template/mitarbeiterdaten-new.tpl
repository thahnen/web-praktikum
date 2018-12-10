## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Mitarbeiterdaten: Neu hinzufügen</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Mitarbeiterdaten: Neu hinzufügen</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Mitarbeiterdaten_Add" method="post">
        <%include file="/elements/kunden-mitarbeiter-new-form.tpl"/>
    </form>
</body>
</html>
