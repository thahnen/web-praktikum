## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<%include file="/elements/header-new.tpl"/>
<body>
    <div class="div--header">
        <!-- Später Headline generieren damit man nur ein Template braucht! -->
        <h1 id="headline">: Neu hinzufügen</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
        <h2 class="h2--failure">Fehler</h2>
    </div>

    <div class="div--tbl">
        <table>
            % for key in data_o["Template"]:
            <tr>
                % if key == "bearbeitungszeitraum":
                <!-- Bearbeitungszeitraum -->
                <th class="tbl--header--elem">
                    Bearbeitungszeitraum:<br/>
                    1. Anfangsdatum<br/>
                    2. Enddatum
                </th>

                % elif key == "kunden_id":
                <!-- Kunden-ID -->
                <th class="tbl--header--elem">
                    Kunden-ID:<br/>
                    (Keine Mehrfachauswahl möglich!)
                </th>

                % elif key == "mitarbeiter_ids":
                <!-- Liste mit allen Mitarbeiter-IDs -->
                <th class="tbl--header--elem">
                    Mitarbeiterliste:<br/>
                    (Mehrfachauswahl möglich!)
                </th>

                % elif key == "zuordnung_arbeit":
                <!-- Zuordnung Arbeit -->
                <th class="tbl--header--elem">
                    Zuordnung der Arbeit:<br/>
                    1. Stunden<br/>
                    2. Mitarbeiterliste<br/>
                    (Mehrfachauswahl möglich!)
                </th>

                % else:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endif

                % if key == "bearbeitungszeitraum":
                <!-- Bearbeitungszeitraum -->
                <td class="tbl--data--elem">
                    <input type="date" required />
                    <input type="date" required />
                </td>
                % elif key == "kunden_id":
                <!-- Kunden-ID -->
                <td class="tbl--data--elem">
                    <select name="kunden_id" size="5">
                        <!-- Elemente werden aus Kunden-IDs autogeneriert! -->
                        <option value="11223344">Chef 1</option>
                        <option value="44332211">Chef 2</option>
                    </select>
                </td>

                % elif key == "mitarbeiter_ids":
                <!-- Liste mit allen Mitarbeiter-IDs -->
                <td class="tbl--data--elem">
                    <select name="mitarbeiter_ids" size="5" multiple>
                        <!-- Elemente werden aus Mitarbeiter-IDs autogeneriert! -->
                        <option value="11223344">Abu Gaben</option>
                        <option value="44332211">Gabe Newell</option>
                    </select>
                </td>
                % elif key == "zuordnung_arbeit":
                <td class="tbl--data--elem">
                    <!-- Zuordnung der Arbeit -->
                    <input type="text" name="" value="Stunden">
                    <select name="" size="3" multiple>
                        <!-- Elemente werden aus Mitarbeiter-IDs autogeneriert! -->
                        <option value="no_value">Test123</option>
                        <option value="11223344">Abu Gaben</option>
                        <option value="44332211">Gabe Newell</option>
                    </select>
                    <input type="button" name="" value="Add">
                    <ul>
                        <li>Test</li>
                    </ul>
                </td>
                % else:
                <td class="tbl--data--elem">
                    <input class="input--data" type="text" value="${key}" required />
                </td>
                % endif
            </tr>
            % endfor:
        </table>
    </div>

    <%include file="/elements/buttons-new.tpl"/>

    <!--<script src="/js/new-projektdaten.js" charset="UTF-8"></script>-->
</body>
</html>
