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

echo "Muss neuem Stand angepasst werden !!!"
exit


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


# Mitarbeiterdaten.json testen
echo ""
echo "Mitarbeiterdaten.json"

M_ADD() {
	cat <<EOF
{
	"link" : "Mitarbeiterdaten",
	"method" : "new",
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
	"method" : "edit",
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
	"method" : "delete",
	"data" : 77777
}
EOF
}

echo "1. Hinzufuegen:"
echo $(M_ADD)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(M_ADD)" 127.0.0.1:8080/update
echo ""

echo "2. Update:"
echo $(M_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(M_UPDATE)" 127.0.0.1:8080/update
echo ""

echo "3. Loeschen:"
echo $(M_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(M_DELETE)" 127.0.0.1:8080/update
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

P_ADD() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"method" : "new",
	"data" : {
		"unique_id" : 88888,
		"nummer" : 44444,
		"bezeichnung" : "Test-Bezeichnung",
		"beschreibung" : "Test-Beschreibung",
		"bearbeitungszeitraum" : {
			"anfang" : "Test-Anfang",
			"ende" : "Test-Ende"
		},
		"budget" : 123.45,
		"kunden_id" : 12321,
		"mitarbeiter_ids" : [11111, 11112, 11113, 11114],
		"zuordnung_arbeit" : {
			"1" : {
				"stunden" : 44444,
				"mitarbeiter_ids" : [11111, 11114]
			}
		}
	}
}
EOF
}

P_UPDATE() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"method" : "edit",
	"data" : {
		"unique_id" : 88888,
		"nummer" : 45454,
		"bezeichnung" : "Bezeichnung-Test",
		"beschreibung" : "Beschreibung-Test",
		"bearbeitungszeitraum" : {
			"anfang" : "Anfang-Test",
			"ende" : "Ende-Test"
		},
		"budget" : 543.21,
		"kunden_id" : 32123,
		"mitarbeiter_ids" : [11111, 21111, 31111, 41111],
		"zuordnung_arbeit" : {
			"1" : {
				"stunden" : 45454,
				"mitarbeiter_ids" : [11111, 41111]
			}
		}
	}
}
EOF
}

P_DELETE() {
	cat <<EOF
{
	"link" : "Projektdaten",
	"method" : "delete",
	"data" : 88888
}
EOF
}

echo "1. Hinzufuegen:"
echo $(P_ADD)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(P_ADD)" 127.0.0.1:8080/update
echo ""

echo "2. Update:"
echo $(P_UPDATE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json" --request POST --data "$(P_UPDATE)" 127.0.0.1:8080/update
echo ""

echo "3. Loeschen:"
echo $(P_DELETE)
echo ""
# Erst einkommentieren, wenn alles klappt!
curl --header "Content-Type: application/json"  --request POST --data "$(P_DELETE)" 127.0.0.1:8080/update
echo ""
