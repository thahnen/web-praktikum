## coding: utf-8
<!DOCTYPE html>
<html lang="de">
<head>
    <%include file="/elements/header.tpl"/>
    <title>Bearbeiten: ${data_o["unique_id"]}</title>
</head>
<body>
    <div class="div--header">
        <h1 id="headline">Bearbeiten: ${data_o["unique_id"]}</h1>
    </div>
    <%include file="/elements/navbar.tpl"/>
    <form action="/POST_Projektdaten_Update" method="post">
        <%include file="/elements/zuordnung-arbeit-form.tpl"/>
    </form>
</body>
</html>
