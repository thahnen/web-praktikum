<!--
    Variable Context mit Aufbau:
    => context-Typ = Array
    => context[0...n] -> Fehlerkategorie-Objekt
-->
<div class="overview_projects">
    <h2>Liste aller Fehlerkategorien:</h2>
    <table>
        <tr>
            <th>Eindeutige Id</th>
            <th>Beschreibung</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i = 0; loop_i < context.length; loop_i++@
        @entry_a = context[loop_i];@
        <tr id="tr--#entry_a['unique_id']#" class="tr--katfehler">
            <td>#entry_a['unique_id']#</td>
            <td>#entry_a['beschreibung']#</td>
        </tr>
    @endfor@
    </table>

    <button id="btn--katfehler--edit">Markierte Fehlerkategorie bearbeiten</button>
    <button id="btn--katfehler--delete">Markierte Fehlerkategorie loeschen</button>
    <button id="btn--katfehler--add">Neue Fehlerkategorie hinzufuegen</button>
</div>
