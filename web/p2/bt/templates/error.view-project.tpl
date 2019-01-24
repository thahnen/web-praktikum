<div class="overview_errors">
    <h2>Liste aller Fehler nach Projekt sortiert:</h2>
    <table>
        <tr>
            <th>Eindeutige Id</th>
            <th>Typ</th>
            <th>Komponenten-Id</th>
            <th>Erkannt -> Beschreibung</th>
            <th>Erkannt -> Id des QSM</th>
            <th>Erkannt -> Erfassungs-Datum</th>
            <th>Erkannt -> Id der Fehlerkategorien-Ids</th>
            <th>Beseitigt -> Beschreibung</th>
            <th>Beseitigt -> Id des SWE</th>
            <th>Beseitigt -> Bearbeitungs-Datum</th>
            <th>Beseitigt -> Fehlerursachenkategorie-Id</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i = 0; loop_i < context.length; loop_i++@
        @entry_a = context[loop_i];@
        <tr id="tr--#entry_a['unique_id']#" class="tr--fehler">
            <td>#entry_a['unique_id']#</td>
            <td>#entry_a['type']#</td>
            <td>#entry_a['komponente']#</td>
            <td>#entry_a['erkannt']['beschreibung']#</td>
            <td>#entry_a['erkannt']['bearbeiter']#</td>
            <td>#entry_a['erkannt']['datum']#</td>
            <td>#entry_a['erkannt']['fehlerkategorien']#</td>
            <td>#entry_a['beseitigt']['beschreibung']#</td>
            <td>#entry_a['beseitigt']['bearbeiter']#</td>
            <td>#entry_a['beseitigt']['datum']#</td>
            <td>#entry_a['beseitigt']['fehlerursachenkategorie']#</td>
        </tr>
    @endfor@
    </table>
    <button id="btn--fehler--erkannt">Alle erkannten Fehler anzeigen</button>
    <button id="btn--fehler--behoben">Alle behobenen Fehler anzeigen</button>
    <button id="btn--fehler--add">Neuen Fehler hinzufuegen</button>
</div>
