<!--
    Variable Context mit Aufbau:
    => context-Typ = Projekt-Objekt
-->
<div class="overview_errors">
    <h2>Fehlerkategorie bearbeiten:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="#context['unique_id']#" disabled>
        </li>
            <p>Beschreibung</p>
            <input id="beschreibung" type="text" value="#context['beschreibung']#">
        </li>
    </ul>
    <button id="btn--katfehler--back">Zurück</button>
    <button id="btn--katfehler--edit--save">Speichern</button>
</div>
