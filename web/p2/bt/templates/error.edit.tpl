<!--
    Variable Context mit Aufbau:
    => context-Typ = Fehler-Objekt
-->
<div class="overview_errors">
    <h2>Fehler bearbeiten:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="#context['unique_id']#" disabled>
        </li>
        <li>
            <p>Typ</p>
            <input id="type" type="text" value="#context['type']#">
        </li>
        <li>
            <p>Komponenten-Id</p>
            <input id="komponente" type="number" value="#context['komponente']#" disabled>
        </li>
        <li>
            <p>Erkannt -> Beschreibung</p>
            <input id="erkannt.beschreibung" type="text" value="#context['erkannt']['beschreibung']#" disabled>
        </li>
        <li>
            <p>Erkannt -> Id des QSM</p>
            <input id="erkannt.bearbeiter" type="number" value="#context['erkannt']['bearbeiter']#" disabled>
        </li>
        <li>
            <p>Erkannt -> Erfassungs-Datum</p>
            <input id="erkannt.datum" type="text" value="#context['erkannt']['datum']#" disabled>
        </li>
        <li>
            <p>Erkannt -> Fehlerkategorien-Ids</p>
            <input id="erkannt.fehlerkategorien" type="text" value="#context['erkannt']['fehlerkategorien']#" disabled>
        </li>
        <li>
            <p>Beseitigt -> Beschreibung</p>
            <input id="beseitigt.beschreibung" type="text" value="#context['beseitigt']['beschreibung']#">
        </li>
        <li>
            <p>Beseitigt -> Bearbeiter</p>
            <input id="beseitigt.bearbeiter" type="number" value="#context['beseitigt']['bearbeiter']#" disabled>
        </li>
        <li>
            <p>Beseitigt -> Bearbeitungs-Datum</p>
            <input id="beseitigt.datum" type="text" value="#context['beseitigt']['datum']#">
        </li>
        <li>
            <p>Beseitigt -> Fehlerursachenkategorie-Id</p>
            <input id="beseitigt.fehlerursachenkategorie" type="number" value="#context['beseitigt']['fehlerursachenkategorie']#">
        </li>
    </ul>
    <button id="btn--fehler--back">Zurück</button>
    <button id="btn--fehler--edit--save">Speichern</button>
</div>
