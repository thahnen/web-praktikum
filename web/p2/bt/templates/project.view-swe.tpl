<!--
    Variable Context mit Aufbau:
    => context-Typ = Array
    => context[0...n] -> Projekt-Objekt
-->
<div class="overview_projects">
    <h2>Liste aller Projekte:</h2>
    <table>
        <tr>
            <th>Eindeutige Id</th>
            <th>Komponenten-Ids</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i = 0; loop_i < context.length; loop_i++@
        @entry_a = context[loop_i];@
        <tr id="tr--#entry_a['unique_id']#" class="tr--projekt">
            <td>#entry_a['unique_id']#</td>
            <td>#entry_a['komponenten']#</td>
        </tr>
    @endfor@
    </table>

    <button id="btn--projekt--edit">Markiertes Projekt bearbeiten</button>
    <button id="btn--projekt--add">Neues Projekt hinzufuegen</button>
    <button id="btn--projekt--delete">Markiertes Projekt loeschen</button>
</div>
