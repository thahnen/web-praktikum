<!--
    Variable Context mit Aufbau:
    => context-Typ = Projekt-Objekt
-->
<div class="overview_errors">
    <h2>Komponente bearbeiten:</h2>
    <ul>
        <li>
            <p>Eindeutige Id</p>
            <input id="unique_id" type="number" value="#context['unique_id']#" disabled>
        </li>
            <p>Fehler</p>
            <input id="fehler" type="text" value="#context['fehler']#">
        </li>
    </ul>
    <button id="btn--komponente--back">Zurück</button>
    <button id="btn--komponente--edit--save">Speichern</button>
</div>
