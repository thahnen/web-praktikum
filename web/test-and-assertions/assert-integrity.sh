#!/usr/bin/env bash


ORDNER_P1=$HOME/GitHub/web-praktikum/web/p1/pro
ORDNER_P11=$HOME/GitHub/web-praktikum/web/p11/pro

# Test auf alle unmodifizierten Dateien, damit erkennbar dass bis auf Server usw. alles gleich!
# => in /app/ alles!
# => in /content/ min. 404.html, 500.html
# => in /data/ min template/kundendaten-tpl.json, template/mitarbeiterdaten-tpl.json, template/projektdaten-tpl.json
echo "Test auf alle Dateien, die sich auf jeden Fall nicht unterscheiden sollen!"
echo ""

diff $ORDNER_P1/app/__init__.py $ORDNER_P11/app/__init__.py &> /dev/null
if test $? -ne 0; then
    echo "/app/__init__.py unterscheiden sich!"
    exit
fi
echo "/app/__init__.py unterscheiden sich nicht!"

diff $ORDNER_P1/app/application.py $ORDNER_P11/app/application.py &> /dev/null
if test $? -ne 0; then
    echo "/app/application.py unterscheiden sich!"
    exit
fi
echo "/app/application.py unterscheiden sich nicht!"

diff $ORDNER_P1/app/database.py $ORDNER_P11/app/database.py &> /dev/null
if test $? -ne 0; then
    echo "/app/database.py unterscheiden sich!"
    exit
fi
echo "/app/database.py unterscheiden sich nicht!"

diff $ORDNER_P1/app/view.py $ORDNER_P11/app/view.py &> /dev/null
if test $? -ne 0; then
    echo "/app/view.py unterscheiden sich!"
    exit
fi
echo "/app/view.py unterscheiden sich nicht!"

diff $ORDNER_P1/content/404.html $ORDNER_P11/content/404.html &> /dev/null
if test $? -ne 0; then
    echo "/content/404.html unterscheiden sich!"
    exit
fi
echo "/content/404.html unterscheiden sich nicht!"

diff $ORDNER_P1/content/500.html $ORDNER_P11/content/500.html &> /dev/null
if test $? -ne 0; then
    echo "/content/500.html unterscheiden sich!"
    exit
fi
echo "/content/500.html unterscheiden sich nicht!"

diff $ORDNER_P1/data/template/kundendaten-tpl.json $ORDNER_P11/data/template/kundendaten-tpl.json &> /dev/null
if test $? -ne 0; then
    echo "/data/template/kundendaten-tpl.json unterscheiden sich!"
    exit
fi
echo "/data/template/kundendaten-tpl.json unterscheiden sich nicht!"

diff $ORDNER_P1/data/template/mitarbeiterdaten-tpl.json $ORDNER_P11/data/template/mitarbeiterdaten-tpl.json &> /dev/null
if test $? -ne 0; then
    echo "/data/template/mitarbeiterdaten-tpl.json unterscheiden sich!"
    exit
fi
echo "/data/template/mitarbeiterdaten-tpl.json unterscheiden sich nicht!"

diff $ORDNER_P1/data/template/projektdaten-tpl.json $ORDNER_P11/data/template/projektdaten-tpl.json &> /dev/null
if test $? -ne 0; then
    echo "/data/template/projektdaten-tpl.json unterscheiden sich!"
    exit
fi
echo "/data/template/projektdaten-tpl.json unterscheiden sich nicht!"


# Test auf alle, auf jeden Fall, modifizierten Dateien
# => in / server.py
echo "Test auf alle Dateien, die sich auf jeden Fall unterscheiden sollen!"
echo ""

diff $ORDNER_P1/server.py $ORDNER_P11/server.py &> /dev/null
if test $? -eq 0; then
    echo "/server.py unterscheiden sich nicht!"
    exit
fi
echo "/server.py unterscheiden sich!"
