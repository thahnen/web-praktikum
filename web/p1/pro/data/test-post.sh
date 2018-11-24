#!/bin/bash


# Test, ob Server ueberhaupt online !
curl 127.0.0.1:8080 &> /dev/null
if test $? -ne 0; then
	echo "Server not up and running on 127.0.0.1:8080!"
	echo "Run> cd $HOME/GitHub/web-praktikum/web/p1/"
	echo "Run> python3 server.py"
	exit
fi


echo "Test aller 4 anwendbaren Funktionen auf eine JSON-Datei:"
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
echo "1. Anfordern:"
echo $(K_GET)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(K_GET)" 127.0.0.1:8080/api/get

echo ""
echo "2. Hinzufuegen:"
echo $(K_NEW)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(K_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Update:"
echo $(K_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(K_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "4. Loeschen:"
echo $(K_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(K_DELETE)" 127.0.0.1:8080/api/delete
echo ""

read -n 1 -p "Weiter (y|n): " ANSWER
if test "$ANSWER" != "y"; then
	echo ""
	exit
fi
echo ""


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
echo "1. Anfordern:"
echo $(M_GET)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(M_GET)" 127.0.0.1:8080/api/get

echo ""
echo "2. Hinzufuegen:"
echo $(M_NEW)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(M_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Update:"
echo $(M_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(M_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "4. Loeschen:"
echo $(M_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(M_DELETE)" 127.0.0.1:8080/api/delete
echo ""

read -n 1 -p "Weiter (y|n): " ANSWER
if test "$ANSWER" != "y"; then
	echo ""
	exit
fi
echo ""


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
echo "1. Anfordern:"
echo $(P_GET)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(P_GET)" 127.0.0.1:8080/api/get

echo ""
echo "2. Hinzufuegen:"
echo $(P_NEW)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(P_NEW)" 127.0.0.1:8080/api/new

echo ""
echo "3. Update:"
echo $(P_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(P_UPDATE)" 127.0.0.1:8080/api/update

echo ""
echo "4. Loeschen:"
echo $(P_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(P_DELETE)" 127.0.0.1:8080/api/delete
echo ""
