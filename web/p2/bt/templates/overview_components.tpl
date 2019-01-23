<!--
    Variable Context mit Aufbau:
    => context-Typ = Array
    => context[0...n] -> Komponente-Objekt
-->
<div class="overview_components">
    <h2>Liste aller Komponenten:</h2>
    <table>
        <tr>
            <th>Eindeutige Id</th>
            <th>Fehler-Ids</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i = 0; loop_i < context.length; loop_i++@
        @entry_a = context[loop_i];@
        <tr id="tr--#entry_a['unique_id']#" class="tr--komponente">
            <td>#entry_a['unique_id']#</td>
            <td>#entry_a['fehler']#</td>
        </tr>
    @endfor@
    </table>

    <button id="btn--komponente--sort">Nach Projekten sortiert</button>
    <button id="btn--komponente--edit">Markierte Komponente bearbeiten</button>
    <button id="btn--komponente--add">Neue Komponente hinzufuegen</button>
</div>
