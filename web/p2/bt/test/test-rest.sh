#!/usr/bin/env bash


# TODO: ALLE anderen moeglichen REST-Anfragen hinzufuegen!


# Test, ob der Server ueberhaupt online ist !
curl 127.0.0.1:8080 &> /dev/null
if test $? -ne 0; then
	echo "Server not up and running on 127.0.0.1:8080 !"
	echo "Run> cd $HOME/GitHub/web-praktikum/web/p1/"
	echo "Run> python3 server.py"
	exit
fi


RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NOCOL='\033[0m'


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\n\nUEBERPRUEFT WIRD 127.0.0.1:8080/projekt\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/projekt:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/projekt)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/projekt

printf "\nGET http://127.0.0.1:8080/projekt/1\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/projekt/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/projekt/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

PROJEKT_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"komponenten" : []
}
EOF
}

printf "\nPOST http://127.0.0.1/projekt + Daten\n"
echo "Uebermittelte Daten: $(PROJEKT_POST)"
PROJEKT_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(PROJEKT_POST)" 127.0.0.1:8080/projekt | jq ".unique_id")
echo "Neue Projekt-Id: ${PROJEKT_ID}"

#
# Hier ggf. noch ein GET mit der Projekt-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

PROJEKT_PUT() {
    cat <<EOF
{
    "unique_id" : $PROJEKT_ID,
    "komponenten" : [1, 2, 3, 4, 5]
}
EOF
}

printf "\nPUT http://127.0.0.1/projekt/$PROJEKT_ID + Daten\n"
echo "Uebermittelte Daten: $(PROJEKT_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(PROJEKT_PUT)" 127.0.0.1:8080/projekt/$PROJEKT_ID)

#
# Hier ggf. noch ein GET mit der Projekt-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/projekt/$PROJEKT_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/projekt/$PROJEKT_ID)

#
# Hier ggf. noch ein GET mit der allen Projekten
#


printf "\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/projektkomponenten\n"
printf "HTTP-Methoden: GET:\n"
printf "==================\n"

printf "\nGET http://127.0.0.1:8080/projektkomponenten/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/projektkomponenten/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/projektkomponenten/1


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/komponente\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/komponente:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/komponente)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/komponente

printf "\nGET http://127.0.0.1:8080/komponente/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/komponente/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/komponente/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

KOMPONENTE_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"fehler" : []
}
EOF
}

printf "\nPOST http://127.0.0.1/komponente/1 + Daten\n"
echo "Uebermittelte Daten: $(KOMPONENTE_POST)"
KOMPONENTE_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(KOMPONENTE_POST)" 127.0.0.1:8080/komponente/1 | jq ".unique_id")
echo "Neue Komponente-Id: ${KOMPONENTE_ID}"

#
# Hier ggf. noch ein GET mit der Komponente-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################


KOMPONENTE_PUT() {
    cat <<EOF
{
    "unique_id" : $KOMPONENTE_ID,
    "fehler" : [1, 2, 3]
}
EOF
}

printf "\nPUT http://127.0.0.1/komponente/$KOMPONENTE_ID + Daten\n"
echo "Uebermittelte Daten: $(KOMPONENTE_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(KOMPONENTE_PUT)" 127.0.0.1:8080/komponente/$KOMPONENTE_ID)

#
# Hier ggf. noch ein GET mit der Komponente-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/komponente/$KOMPONENTE_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/komponente/$KOMPONENTE_ID)

#
# Hier ggf. noch ein GET mit der allen Komponenten
#


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/qsmitarbeiter\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/qsmitarbeiter:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/qsmitarbeiter)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/qsmitarbeiter

printf "\nGET http://127.0.0.1:8080/qsmitarbeiter/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/qsmitarbeiter/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/qsmitarbeiter/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

QSMITARBEITER_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"username" : "abcdef",
	"password" : "abcdef"
}
EOF
}

printf "\nPOST http://127.0.0.1/qsmitarbeiter + Daten\n"
echo "Uebermittelte Daten: $(QSMITARBEITER_POST)"
QSMITARBEITER_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(QSMITARBEITER_POST)" 127.0.0.1:8080/qsmitarbeiter | jq ".unique_id")
echo "Neue QS-Mitarbeiter-Id: ${QSMITARBEITER_ID}"

#
# Hier ggf. noch ein GET mit der QS-Mitarbeiter-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################


QSMITARBEITER_PUT() {
    cat <<EOF
{
    "unique_id" : $QSMITARBEITER_ID,
    "username" : "uvwxyz",
	"password" : "uvwxyz"
}
EOF
}

printf "\nPUT http://127.0.0.1/qsmitarbeiter/$QSMITARBEITER_ID + Daten\n"
echo "Uebermittelte Daten: $(QSMITARBEITER_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(QSMITARBEITER_PUT)" 127.0.0.1:8080/qsmitarbeiter/$QSMITARBEITER_ID)

#
# Hier ggf. noch ein GET mit der QS-Mitarbeiter-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/qsmitarbeiter/$QSMITARBEITER_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/qsmitarbeiter/$QSMITARBEITER_ID)

#
# Hier ggf. noch ein GET mit der allen QS-Mitarbeitern
#


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/swentwickler\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/swentwickler:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/swentwickler)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/swentwickler

printf "\nGET http://127.0.0.1:8080/swentwickler/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/swentwickler/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/swentwickler/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

SWENTWICKLER_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"username" : "fedcba",
	"password" : "fedcba"
}
EOF
}

printf "\nPOST http://127.0.0.1/swentwickler + Daten\n"
echo "Uebermittelte Daten: $(SWENTWICKLER_POST)"
SWENTWICKLER_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(SWENTWICKLER_POST)" 127.0.0.1:8080/swentwickler | jq ".unique_id")
echo "Neue SW-Entwickler-Id: ${SWENTWICKLER_ID}"

#
# Hier ggf. noch ein GET mit der SW-Entwickler-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

SWENTWICKLER_PUT() {
    cat <<EOF
{
    "unique_id" : $SWENTWICKLER_ID,
    "username" : "zyxwvu",
	"password" : "zyxwvu"
}
EOF
}

printf "\nPUT http://127.0.0.1/swentwickler/$SWENTWICKLER_ID + Daten\n"
echo "Uebermittelte Daten: $(SWENTWICKLER_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(SWENTWICKLER_PUT)" 127.0.0.1:8080/swentwickler/$SWENTWICKLER_ID)

#
# Hier ggf. noch ein GET mit der SW-Entwickler-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/swentwickler/$SWENTWICKLER_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/swentwickler/$SWENTWICKLER_ID)

#
# Hier ggf. noch ein GET mit der allen SW-Entwicklern
#


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/katfehler\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/katfehler:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/katfehler)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/katfehler

printf "\nGET http://127.0.0.1:8080/katfehler/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/katfehler/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/katfehler/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

KATFEHLER_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"beschreibung" : "Fehlerkategorie"
}
EOF
}

printf "\nPOST http://127.0.0.1/katfehler + Daten\n"
echo "Uebermittelte Daten: $(KATFEHLER_POST)"
KATFEHLER_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(KATFEHLER_POST)" 127.0.0.1:8080/katfehler | jq ".unique_id")
echo "Neue Katfehler-Id: ${KATFEHLER_ID}"

#
# Hier ggf. noch ein GET mit der Katfehler-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################


KATFEHLER_PUT() {
    cat <<EOF
{
    "unique_id" : $KATFEHLER_ID,
    "beschreibung" : "Nicht Fehlerkategorie"
}
EOF
}

printf "\nPUT http://127.0.0.1/katfehler/$KATFEHLER_ID + Daten\n"
echo "Uebermittelte Daten: $(KATFEHLER_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(KATFEHLER_PUT)" 127.0.0.1:8080/katfehler/$KATFEHLER_ID)

#
# Hier ggf. noch ein GET mit der Katfehler-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/katfehler/$KATFEHLER_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/katfehler/$KATFEHLER_ID)

#
# Hier ggf. noch ein GET mit der allen Katfehlern
#


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/katursache\n"
printf "HTTP-Methoden: GET | POST | PUT | DELETE:\n"
printf "========================================\n"

printf "\nGET http://127.0.0.1:8080/katursache:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/katursache)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/katursache

printf "\nGET http://127.0.0.1:8080/katursache/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/katursache/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/katursache/1

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

KATURSACHE_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"beschreibung" : "Fehlerursachenkategorie"
}
EOF
}

printf "\nPOST http://127.0.0.1/katursache + Daten\n"
echo "Uebermittelte Daten: $(KATURSACHE_POST)"
KATURSACHE_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(KATURSACHE_POST)" 127.0.0.1:8080/katursache | jq ".unique_id")
echo "Neue Katursache-Id: ${KATURSACHE_ID}"

#
# Hier ggf. noch ein GET mit der Katursache-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################


KATURSACHE_PUT() {
    cat <<EOF
{
    "unique_id" : $KATURSACHE_ID,
    "beschreibung" : "Nicht Fehlerursachenkategorie"
}
EOF
}

printf "\nPUT http://127.0.0.1/katursache/$KATURSACHE_ID + Daten\n"
echo "Uebermittelte Daten: $(KATURSACHE_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(KATURSACHE_PUT)" 127.0.0.1:8080/katursache/$KATURSACHE_ID)

#
# Hier ggf. noch ein GET mit der Katursache-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

printf "\nDELETE http://127.0.0.1/katursache/$KATURSACHE_ID\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request DELETE 127.0.0.1:8080/katursache/$KATURSACHE_ID)

#
# Hier ggf. noch ein GET mit der allen Katursachen
#


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/fehler\n"
printf "HTTP-Methoden: GET | POST | PUT:\n"
printf "===============================\n"

printf "\nGET http://127.0.0.1:8080/fehler:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/fehler)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/fehler

printf "\nGET http://127.0.0.1:8080/fehler/1:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/fehler/1)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/fehler/1

printf "\nGET http://127.0.0.1:8080/fehler/?type=erkannt:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/fehler/?type=erkannt)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/fehler/?type=erkannt

printf "\nGET http://127.0.0.1:8080/fehler/?type=behoben:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/fehler/?type=behoben)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/fehler/?type=behoben

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################

FEHLER_POST() {
	cat <<EOF
{
	"unique_id" : 12345,
	"type" : "erkannt",
	"erkannt" : {
		"beschreibung" : "Erkannter Fehler",
		"bearbeiter" : 1,
		"datum" : "01.01.2001",
		"fehlerkategorien" : [1, 2]
	},
	"beseitigt" : {
		"beschreibung" : null,
		"bearbeiter" : null,
		"datum" : null,
		"fehlerursachenkategorie" : null
	}
}
EOF
}

printf "\nPOST http://127.0.0.1/fehler + Daten\n"
echo "Uebermittelte Daten: $(FEHLER_POST)"
FEHLER_ID=$(curl -s --header "Content-Type: application/json" --request POST --data "$(FEHLER_POST)" 127.0.0.1:8080/fehler | jq ".unique_id")
echo "Neue Fehler-Id: ${FEHLER_ID}"

#
# Hier ggf. noch ein GET mit der Fehler-Id
#

printf "\n________________________________________________________________________________\n\n"
################################################################################################################################################################


FEHLER_PUT() {
    cat <<EOF
{
    "unique_id" : $FEHLER_ID,
	"type" : "behoben",
	"erkannt" : {
		"beschreibung" : "Erkannter Fehler",
		"bearbeiter" : 1,
		"datum" : "01.01.2001",
		"fehlerkategorien" : [1, 2]
	},
	"beseitigt" : {
		"beschreibung" : "Fehler wurde beseitigt",
		"bearbeiter" : 2,
		"datum" : "12.12.2012",
		"fehlerursachenkategorie" : [2, 3]
	}
}
EOF
}

printf "\nPUT http://127.0.0.1/fehler/$FEHLER_ID + Daten\n"
echo "Uebermittelte Daten: $(FEHLER_PUT)"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" --header "Content-Type: application/json" --request PUT --data "$(FEHLER_PUT)" 127.0.0.1:8080/fehler/$FEHLER_ID)

#
# Hier ggf. noch ein GET mit der Fehler-Id


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/prolist\n"
printf "HTTP-Methoden: GET:\n"
printf "==================\n"

printf "\nGET http://127.0.0.1:8080/prolist:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/prolist)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/prolist


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/katlist\n"
printf "HTTP-Methoden: GET:\n"
printf "==================\n"

printf "\nGET http://127.0.0.1:8080/katlist:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/katlist)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/katlist


printf "\n\n${RED}================================================================================\n\n"

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	printf "\nBeende...\n${NOCOL}"
            exit;;
	*)		;;
esac

printf "\n\n================================================================================${NOCOL}\n\n"


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


printf "\nUEBERPRUEFT WIRD 127.0.0.1:8080/templates\n"
printf "HTTP-Methoden: GET:\n"
printf "==================\n"

printf "\nGET http://127.0.0.1:8080/templates:\n"
printf "HTTP-Rueckgabe-Code: "
echo $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/templates)
#printf "Zurueckgegebene JSON-Daten: "
#curl -s http://127.0.0.1:8080/templates
