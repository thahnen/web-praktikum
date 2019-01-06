//------------------------------------------------------------------------------
// Einfache Anforderungen per Fetch-API
//------------------------------------------------------------------------------
'use strict';

var APPUTIL = APPUTIL || {};

APPUTIL.Requester = class {
    constructor () { }

    request (pfad, erfolg_callback, fail_callback) {
        fetch(pfad).then(function (response) {
            let rueckgabe = null;
            if(response.ok) { // 200er-Status-Code
                rueckgabe = response.text().then(function (text) {
                    console.log("[Requester] request->erfolg");
                    erfolg_callback(text);
                });
            } else {
                rueckgabe = response.text().then(function (text) {
                    console.log("[Requester] request->fail");
                    fail_callback(text);
                });
            }
            return rueckgabe;
        }).catch(function (error) {
            console.log("[Requester] fetch-Problem: ", error.message);
        });
    }
}
