#!/usr/bin/env bash


ORDNER_P1=$HOME/GitHub/web-praktikum/web/p1/pro
ORDNER_P11=$HOME/GitHub/web-praktikum/web/p11/pro
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NOCOL='\033[0m'


# Test auf alle unmodifizierten Dateien, damit erkennbar dass bis auf Server usw. alles gleich!
# => in /app/ alles!
# => in /content/ 404.html, 500.html
# => in /content/css standard.css
# => in /data/template/ kundendaten-tpl.json, mitarbeiterdaten-tpl.json, projektdaten-tpl.json
printf "\n\n${BLUE}Test auf alle Dateien, die sich auf jeden Fall nicht unterscheiden sollen!${NOCOL}\n\n"

diff $ORDNER_P1/app/__init__.py $ORDNER_P11/app/__init__.py &> /dev/null
if test $? -ne 0; then
    printf "${RED}/app/__init__.py unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/app/__init__.py unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/app/application.py $ORDNER_P11/app/application.py &> /dev/null
if test $? -ne 0; then
    printf "${RED}/app/application.py unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/app/application.py unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/app/database.py $ORDNER_P11/app/database.py &> /dev/null
if test $? -ne 0; then
    printf "${RED}/app/database.py unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/app/database.py unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/app/view.py $ORDNER_P11/app/view.py &> /dev/null
if test $? -ne 0; then
    printf "${RED}/app/view.py unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/app/view.py unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/content/404.html $ORDNER_P11/content/404.html &> /dev/null
if test $? -ne 0; then
    printf "${RED}/content/404.html unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/content/404.html unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/content/500.html $ORDNER_P11/content/500.html &> /dev/null
if test $? -ne 0; then
    printf "${RED}/content/500.html unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/content/500.html unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/content/css/standard.css $ORDNER_P11/content/css/standard.css &> /dev/null
if test $? -ne 0; then
    printf "${RED}/content/css/standard.css unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/content/css/standard.css unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/data/template/kundendaten-tpl.json $ORDNER_P11/data/template/kundendaten-tpl.json &> /dev/null
if test $? -ne 0; then
    printf "${RED}/data/template/kundendaten-tpl.json unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/data/template/kundendaten-tpl.json unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/data/template/mitarbeiterdaten-tpl.json $ORDNER_P11/data/template/mitarbeiterdaten-tpl.json &> /dev/null
if test $? -ne 0; then
    printf "${RED}/data/template/mitarbeiterdaten-tpl.json unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/data/template/mitarbeiterdaten-tpl.json unterscheiden sich nicht!${NOCOL}\n"

diff $ORDNER_P1/data/template/projektdaten-tpl.json $ORDNER_P11/data/template/projektdaten-tpl.json &> /dev/null
if test $? -ne 0; then
    printf "${RED}/data/template/projektdaten-tpl.json unterscheiden sich!${NOCOL}\n"
    exit
fi
printf "${GREEN}/data/template/projektdaten-tpl.json unterscheiden sich nicht!${NOCOL}\n"


# Test auf alle, auf jeden Fall, modifizierten Dateien
# => in / server.py
printf "\n\n${BLUE}Test auf alle Dateien, die sich auf jeden Fall unterscheiden sollen!${NOCOL}\n\n"

diff $ORDNER_P1/server.py $ORDNER_P11/server.py &> /dev/null
if test $? -eq 0; then
    printf "${RED}/server.py unterscheiden sich nicht!${NOCOL}\n"
    exit
fi
printf "${GREEN}/server.py unterscheiden sich!${NOCOL}\n"
