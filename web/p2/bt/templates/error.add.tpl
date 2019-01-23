<!--
    Variable Context mit Aufbau:
    => context-Typ = Fehler-Objekt
-->
<div class="overview_errors">
    <h2>Fehler hinzufuegen:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="1234567890" disabled>
        </li>
        <li>
            <p>Typ</p>
            <input id="type" type="text" value="erkannt" disabled>
        </li>
        <li>
            <p>Komponenten-Id</p>
            <input id="komponente" type="number" value="0">
        </li>
        <li>
            <p>Erkannt -> Beschreibung</p>
            <input id="erkannt.beschreibung" type="text" value="Hier Fehlerbeschreibung eintragen">
        </li>
        <li>
            <p>Erkannt -> Id des QSM</p>
            <input id="erkannt.bearbeiter" type="number" value="0">
        </li>
        <li>
            <p>Erkannt -> Erfassungs-Datum</p>
            <input id="erkannt.datum" type="text" value="Hier das Erfassungs-Datum eintragen">
        </li>
        <li>
            <p>Erkannt -> Fehlerkategorien-Ids</p>
            <input id="erkannt.fehlerkategorien" type="text" value="Hier Fehlerkategorie-Ids mit Kommata getrennt eintragen">
        </li>
        <li>
            <p>Beseitigt -> Beschreibung</p>
            <input id="beseitigt.beschreibung" type="text" value="null"disabled>
        </li>
        <li>
            <p>Beseitigt -> Bearbeiter</p>
            <input id="beseitigt.bearbeiter" type="number" value="0">
        </li>
        <li>
            <p>Beseitigt -> Bearbeitungs-Datum</p>
            <input id="beseitigt.datum" type="text" value="null" disabled>
        </li>
        <li>
            <p>Beseitigt -> Fehlerursachenkategorie-Id</p>
            <input id="beseitigt.fehlerursachenkategorie" type="number" value="0" disabled>
        </li>
    </ul>
    <button id="btn--fehler--back">Zurück</button>
    <button id="btn--fehler--add--add">Hinzufuegen</button>
</div>
