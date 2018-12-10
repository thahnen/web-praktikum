## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Bearbeiten: ${data_o["Data"]["unique_id"]}</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Bearbeiten: ${data_o["Data"]["unique_id"]}</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Mitarbeiterdaten_Update" method="post">
        <%include file="/elements/kunden-mitarbeiter-edit-form.tpl"/>
    </form>
</body>
</html>
