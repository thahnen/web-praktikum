<!--
    Variable Context mit Aufbau:
    => context-Typ = Projekt-Objekt
-->
<div class="overview_errors">
    <h2>Fehlerursachenkategorie bearbeiten:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="#context['unique_id']#" disabled>
        </li>
            <p>Beschreibung</p>
            <input id="beschreibung" type="text" value="#context['beschreibung']#">
        </li>
    </ul>
    <button id="btn--katursache--back">Zurück</button>
    <button id="btn--katursache--edit--save">Speichern</button>
</div>
