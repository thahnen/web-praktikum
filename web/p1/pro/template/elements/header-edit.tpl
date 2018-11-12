## coding: utf-8
<%doc>
    Das Head-Element für jedes "[...]-edit.tpl"-Template.
    Für alle Seiten, auf denen man Daten editieren kann gleich.
</%doc>
<head>
    <meta charset="utf-8" />
    <meta name="robots" content="noindex,nofollow" />
    <meta http-equiv="expires" content="0" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <meta name="format-detection" content="telephone=no" />
    <meta name="author" content="Tobias Hahnen" />
    <title>${data_o["Data"]["unique_id"]}</title>

    <!-- Das Favicon für den Tab, einfach von der HS geklaut :p -->
    <link rel="icon" href="https://www.hs-niederrhein.de/fileadmin/images/layout/icons/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/edit.css" />
</head>
