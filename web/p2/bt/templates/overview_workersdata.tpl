<!--
    Variable Context mit Aufbau:
    => context-Typ = Array
    => context[0...n] -> SWE-Objekt bzw. QSM-Objekt
-->
<div class="overview_projects">
    <h2>Liste aller -Arbeiter:</h2>
    <table>
        <tr>
            <th>Eindeutige Id</th>
            <th>Username</th>
            <th>Password-Hash</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i = 0; loop_i < context.length; loop_i++@
        @entry_a = context[loop_i];@
        <tr id="tr--#entry_a['unique_id']#" class="tr--arbeiter">
            <td>#entry_a['unique_id']#</td>
            <td>#entry_a['username']#</td>
            <td>#entry_a['password']#</td>
        </tr>
    @endfor@
    </table>

    <button id="btn--arbeiter--edit">Markierten -Arbeiter bearbeiten</button>
    <button id="btn--arbeiter--add">Neuen -Arbeiter hinzufuegen</button>
</div>
