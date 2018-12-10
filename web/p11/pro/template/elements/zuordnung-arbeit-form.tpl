## coding: utf-8
<%doc>
    Das Form-Element für die Hinzufügen- / Bearbeiten-Seite (Zuordnung Arbeit) der Projekte der 1.1 Aufgabe!
</%doc>
        % for key in data_o:
        % if key == "mitarbeiter_ids":
        <input type="hidden" name="${key}" value="${data_o[key]}">
        <table>
            <tr>
                <th>ID / Woche</th>
                % for woche in range(1, data_o["bearbeitungszeitraum"]+1):
                <th>Woche ${woche}</th>
                % endfor
            </tr>

            % for mitarbeiter in range(0, len(data_o[key])):
            <tr>
                <td>${data_o[key][mitarbeiter]}</td>
                % for woche in range(1, data_o["bearbeitungszeitraum"]+1):
                <td>
                    <input type="number" name="zuordnung_arbeit" value="">
                </td>
                % endfor
            </tr>
            % endfor
        </table>
        % else:
        <input type="hidden" name="${key}" value="${data_o[key]}">
        % endif
        % endfor
        <div class="div--btn">
            <input type="submit" id="btn--add" value="Hinzufügen">
        </div>
