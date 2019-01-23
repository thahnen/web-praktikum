<!--
    Variable Context mit Aufbau:
    => context-Typ = Projekt-Objekt
-->
<div class="overview_errors">
    <h2>Projekt bearbeiten:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="#context['unique_id']#" disabled>
        </li>
            <p>Komponenten</p>
            <input id="komponenten" type="text" value="#context['komponenten']#">
        </li>
    </ul>
    <button id="btn--projekt--back">Zurück</button>
    <button id="btn--projekt--edit--save">Speichern</button>
</div>
