## coding: utf-8
<!DOCTYPE html>
<html lang="de" x-ms-format-detection="none">
<%include file="/elements/header-view.tpl"/>
<body>
    <div class="div--header">
        <h1 id="headline">: Überblick</h1>
    </div>

    <%include file="/elements/navbar.tpl"/>

    <div class="div--failure">
        <!-- Vom XMLHttpRequest Fehler auswerten? -->
        <h2 class="h2--failure">Fehler</h2>
    </div>

    <div class="div--tbl">
        <table>
            <!-- Table Header Row -->
            <tr class="tbl--header">
                % for key in data_o["Template"]:
                <th class="tbl--header--elem">${data_o["Template"][key]}</th>
                % endfor
            </tr>

            <!-- Table Elements Row -->
            % for object in data_o["Elements"]:
            <tr class="tbl--data">
                % for object_key in data_o["Elements"][object]:
                <td class="tbl--data--elem">
                    % if object_key == "bearbeitungszeitraum":
                    <!-- Irgendwie schön eine Zeitspanne anzeigen -->
                    <ul>
                        <li>Beginn: ${data_o["Elements"][object][object_key]["anfang"]}</li>
                        <li>Ende: ${data_o["Elements"][object][object_key]["ende"]}</li>
                    </ul>
                    % elif object_key == "kunden_id":
                    <a class="a--elem" href="/kundendaten/${data_o["Elements"][object][object_key]}">${data_o["Elements"][object][object_key]}</a>
                    % elif object_key == "mitarbeiter_ids":
                    <!-- Irgendwie schön die Mitarbeiterliste anzeigen -->
                    <ul>
                        % for id in data_o["Elements"][object][object_key]:
                        <li><a class="a--elem" href="/mitarbeiterdaten/${id}">${id}</a></li>
                        % endfor
                    </ul>
                    % elif object_key == "zuordnung_arbeit":
                    <!-- Irgendwie schön die Zuordnung anzeigen -->
                    <ul>
                        % for zu_o in data_o["Elements"][object][object_key]:
                        <li>
                            ${data_o["Elements"][object][object_key][zu_o]["stunden"]}
                            <ul>
                                % for zu_o_mid in data_o["Elements"][object][object_key][zu_o]["mitarbeiter_ids"]:
                                <li>${zu_o_mid}</li>
                                % endfor
                            </ul>
                        </li>
                        % endfor
                    </ul>
                    % else:
                    ${data_o["Elements"][object][object_key]}
                    % endif
                </td>
                % endfor
            </tr>
            % endfor
        </table>
    </div>

    <%include file="/elements/buttons-view.tpl"/>

    <script src="/js/view.js" charset="UTF-8"></script>
</body>
</html>
