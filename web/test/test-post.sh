#!/usr/bin/env bash


# TODO: alles noch mit Farbe ausfüllen!
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NOCOL='\033[0m'


# Test, ob der Server ueberhaupt online ist !
curl 127.0.0.1:8080 &> /dev/null
if [[ $? -eq 0 ]]; then
	echo "Server not up and running on 127.0.0.1:8080 !"
	echo "Run> cd $HOME/GitHub/web-praktikum/web/p1/"
	echo "Run> python3 server.py"
	exit 1
fi

# Test, ob es auch der Server für Aufgabe 1.2 ist !
if [[ $(curl -I 127.0.0.1:8080/api 2>/dev/null | head -n 1 | cut -d$' ' -f2) -eq "404" ]]; then
    echo "Wrong Server up and running, use the one for 1.2 !"
    exit 1
fi


echo "Test aller 4 anwendbaren Funktionen auf eine JSON-Datei (aber halt nicht in der Reihenfolge):"
echo "1. Anfordern"
echo "2. Hinzufuegen"
echo "3. Update"
echo "4. Loeschen"


################################################################################
################################################################################
################################################################################


# 1. Kundendaten.json testen
echo ""
echo "Kundendaten.json"

K_GET() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : ""
}
EOF
}

K_NEW() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 99999,
		"nummer" : 99999,
		"bezeichnung" : "Test-Bezeichnung",
		"ansprechpartner" : "Test-Ansprechpartner",
		"ort" : "Test-Ort"
	}
}
EOF
}

K_UPDATE() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 99999,
		"nummer" : 66666,
		"bezeichnung" : "Bezeichnung-Test",
		"ansprechpartner" : "Ansprechpartner-Test",
		"ort" : "Ort-Test"
	}
}
EOF
}

K_DELETE() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : 99999
}
EOF
}

echo ""
echo "1. Anfordern (vor dem hinzufuegen):"
echo $(K_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_GET)" 127.0.0.1:8080/api/get

# funktioniert noch alles nicht, weil beim hinzufuegen eine neue unique_id generiert wird!
exit 1

echo ""
echo "2. Hinzufuegen:"
echo $(K_NEW)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Anfordern (nach dem hinzufuegen & vor dem update):"
echo $(K_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_GET)" 127.0.0.1:8080/api/get

echo ""
echo "4. Update:"
echo $(K_UPDATE)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "5. Anfordern (nach dem update & vor dem loeschen):"
echo $(K_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_GET)" 127.0.0.1:8080/api/get

echo ""
echo "6. Loeschen:"
echo $(K_DELETE)
echo ""
curl --header "Content-Type: application/json"  --request POST --data "$(K_DELETE)" 127.0.0.1:8080/api/delete
echo ""

echo ""
echo "7. Anfordern (nach dem loeschen):"
echo $(K_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(K_GET)" 127.0.0.1:8080/api/get

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	exit 1 ;;
	*)		;;
esac


################################################################################
################################################################################
################################################################################


# Mitarbeiterdaten.json testen
echo ""
echo "Mitarbeiterdaten.json"

M_GET() {
	cat <<EOF
{
	"link" : "Mitarbeiterdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : ""
}
EOF
}

M_NEW() {
	cat <<EOF
{
	"link" : "Mitarbeiterdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 77777,
		"name" : "Test-Name",
		"vorname" : "Test-Vorname",
		"funktion" : "Test-Funktion"
	}
}
EOF
}

M_UPDATE() {
	cat <<EOF
{
	"link" : "Mitarbeiterdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 77777,
		"name" : "Name-Test",
		"vorname" : "Vorname-Test",
		"funktion" : "Funktion-Test"
	}
}
EOF
}

M_DELETE() {
	cat <<EOF
{
	"link" : "Mitarbeiterdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : 77777
}
EOF
}

echo ""
echo "1. Anfordern (vor dem hinzufuegen):"
echo $(M_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_GET)" 127.0.0.1:8080/api/get

echo ""
echo "2. Hinzufuegen:"
echo $(M_NEW)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Anfordern (nach dem hinzufuegen & vor dem update):"
echo $(M_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_GET)" 127.0.0.1:8080/api/get

echo ""
echo "4. Update:"
echo $(M_UPDATE)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "5. Anfordern (nach dem update & vor dem loeschen):"
echo $(M_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_GET)" 127.0.0.1:8080/api/get

echo ""
echo "6. Loeschen:"
echo $(M_DELETE)
echo ""
curl --header "Content-Type: application/json"  --request POST --data "$(M_DELETE)" 127.0.0.1:8080/api/delete
echo ""

echo ""
echo "7. Anfordern (nach dem loeschen):"
echo $(M_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(M_GET)" 127.0.0.1:8080/api/get

read -n 1 -p "Weiter (y|n): " ANSWER
case $ANSWER in
	N|n)	exit 1 ;;
	*)		;;
esac


################################################################################
################################################################################
################################################################################


# Projektdaten.json testen
echo ""
echo "Projektdaten.json"

P_GET() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : ""
}
EOF
}

P_NEW() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 88888,
		"nummer" : 44444,
		"bezeichnung" : "Test-Bezeichnung",
		"beschreibung" : "Test-Beschreibung",
		"bearbeitungszeitraum" : 6,
		"budget" : 123,
		"kunden_id" : 12321,
		"mitarbeiter_ids" : [11111, 11112, 11113, 11114],
		"zuordnung_arbeit" : {
			"11111" : [2, 12, 3, 13, 4, 14],
			"11112" : [3, 13, 4, 14, 5, 15],
			"11113" : [4, 14, 5, 15, 6, 16],
			"11114" : [5, 15, 6, 16, 7, 17]
		}
	}
}
EOF
}

P_UPDATE() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : {
		"unique_id" : 88888,
		"nummer" : 45454,
		"bezeichnung" : "Bezeichnung-Test",
		"beschreibung" : "Beschreibung-Test",
		"bearbeitungszeitraum" : 3,
		"budget" : 543,
		"kunden_id" : 32123,
		"mitarbeiter_ids" : [11111, 21111, 31111],
		"zuordnung_arbeit" : {
			"11111" : [1, 2, 3],
			"21111" : [11, 22, 33],
			"31111" : [12, 34, 56]
		}
	}
}
EOF
}

P_DELETE() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
	"data" : 88888
}
EOF
}

echo ""
echo "1. Anfordern (vor dem hinzufuegen):"
echo $(P_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_GET)" 127.0.0.1:8080/api/get

echo ""
echo "2. Hinzufuegen:"
echo $(P_NEW)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Anfordern (nach dem hinzufuegen & vor dem update):"
echo $(P_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_GET)" 127.0.0.1:8080/api/get

echo ""
echo "4. Update:"
echo $(P_UPDATE)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "5. Anfordern (nach dem update & vor dem loeschen):"
echo $(P_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_GET)" 127.0.0.1:8080/api/get

echo ""
echo "6. Loeschen:"
echo $(P_DELETE)
echo ""
curl --header "Content-Type: application/json"  --request POST --data "$(P_DELETE)" 127.0.0.1:8080/api/delete
echo ""

echo ""
echo "7. Anfordern (nach dem loeschen):"
echo $(P_GET)
echo ""
curl --header "Content-Type: application/json" --request POST --data "$(P_GET)" 127.0.0.1:8080/api/get
