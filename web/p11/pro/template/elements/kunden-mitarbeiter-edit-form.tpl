## coding: utf-8
<%doc>
    Das Form-Element für die Hinzufügen-Seite der Kunden und Mitarbeiter der 1.1 Aufgabe!
</%doc>
        <div class="div--tbl">
            <table>
                <tr class="tbl--header">
                    % for key in data_o["Template"]:
                    <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                    % endfor
                </tr>

                <tr class="tbl--data">
                    % for key in data_o["Data"]:
                    <td class="tbl--data--elem">
                        % if key == "unique_id":
                        <input class="input--data" type="text" value="${data_o["Data"][key]}" required disabled />
                        <input type="hidden" name="${key}" value="${data_o["Data"][key]}">
                        %elif key == "nummer":
                        <input class="input--data input--edit" type="number" name="${key}" value="${data_o["Data"][key]}" required />
                        % else:
                        <input class="input--data input--edit" type="text" name="${key}" value="${data_o["Data"][key]}" required />
                        % endif
                    </td>
                    % endfor
                </tr>
            </table>
        </div>
        <div class="div--btn">
            <input type="submit" id="btn--update" value="Bearbeiten">
        </div>
