#!/bin/bash


# Test, ob Server ueberhaupt online !
curl 127.0.0.1:8080 &> /dev/null
if test $? -ne 0; then
	echo "Server not up and running on 127.0.0.1:8080!"
	exit
fi


echo "Test aller 3 anwendbaren Funktionen auf eine JSON-Datei:"
echo "1. Hinzufuegen"
echo "2. Update"
echo "3. Loeschen"


################################################################################
################################################################################
################################################################################


# 1. Kundendaten.json testen
echo ""
echo "Kundendaten.json"

K_ADD() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"method" : "new",
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
	"method" : "edit",
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
	"method" : "delete",
	"data" : 99999
}
EOF
}

echo "1. Hinzufuegen:"
echo $(K_ADD)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(K_ADD)" 127.0.0.1:8080/update
echo ""

echo "2. Update:"
echo $(K_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(K_UPDATE)" 127.0.0.1:8080/update
echo ""

echo "3. Loeschen:"
echo $(K_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(K_DELETE)" 127.0.0.1:8080/update
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


# das kommt weg wenn der Rest da ist!
exit
# Mitarbeiterdaten.json testen
echo ""
echo "Mitarbeiterdaten.json"

# Noch für Mitarbeiter machen
M_ADD() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"method" : "new",
	"data" : {
	}
}
EOF
}

# Noch für Mitarbeiter machen
M_UPDATE() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"method" : "edit",
	"data" : {
	}
}
EOF
}

# Noch für Mitarbeiter machen
M_DELETE() {
	cat <<EOF
{
	"link" : "Kundendaten",
	"method" : "delete",
	"data" : 11111
}
EOF
}
