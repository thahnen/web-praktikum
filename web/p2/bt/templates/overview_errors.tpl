<!--
    Übersicht der Fehler, die bestimmter QSM gemeldet hat (unterteilt in erkannt/ bearbeitet)
    Variable Context mit Aufbau:
    => context-Typ = Array
    1) context[0] -> Array
    1.1) context[0][0...n] = Fehler-Objekt (die erkannten)
    2) context[1] -> Array
    2.1) context[0][0...n] = Fehler-Objekt (die bearbeiteten)
-->
<div class="overview_errors">
    <h2>Liste der erkannten Fehler:</h2>
    <table>
    @var erkannt;@
    @var i;@
    @for i = 0; i < context[0].lengt; i++@
        @erkannt = context[0][i];@
        <tr id="#erkannt['unique_id']#">
            <td>#erkannt['unique_id']#</td>
            <td>#erkannt['type']#</td>
            <td>#erkannt['erkannt']#</td>
            <td>#erkannt['beseitigt']#</td>
        </tr>
    @endfor@
    </table>
    <h2>Liste der bearbeiteten Fehler:</h2>
    <table>
    @var bearbeitet;@
    @var j;@
    @for j = 0; j < context[1].length; j++@
        @bearbeitet = context[1][j];@
        <tr id="#bearbeitet['unique_id']#">
            <td>#bearbeitet['unique_id']#</td>
            <td>#bearbeitet['type']#</td>
            <td>#bearbeitet['erkannt']#</td>
            <td>#bearbeitet['beseitigt']#</td>
        </tr>
    </table>
</div>
