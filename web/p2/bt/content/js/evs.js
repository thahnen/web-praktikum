//------------------------------------------------------------------------------
// Event-Service: asynchroner Nachrichtenaustausch
//------------------------------------------------------------------------------

'use strict'

var APPUTIL = APPUTIL || {};

APPUTIL.EventService = class {
    constructor () {
        this.Data = null;
        this.Subscriber = {};
        this.Method = null;
    }

    subscribe (subscriber, message) {
        if (message in this.Subscriber) {
            // Message bekannt, Liste der Subscriber untersuchen
            if (this.Subscriber[message].indexOf(subscriber) == -1) {
                this.Subscriber[message].push(subscriber);
            }
        } else {
            // Message noch nicht vorhanden, neu eintragen
            this.Subscriber[message] = [subscriber];
        }
    }

    unsubscribe (subscriber, message) {
        if (message in this.Subscriber) {
            // Message bekannt, Liste der Subscriber untersuchen
            let entry = this.Subscriber[message];
            let index = entry.indexOf(subscriber);

            if (index >= 0) {
                // Eintrag entfernen
                entry[index] = null;
                entry = this.compact(entry); // compact liefert Kopie!

                if (entry.length == 0) {
                    // keine Subscriber mehr, kann entfernt werden
                    delete this.Subscriber[message];
                }
            }
        } else {
            // Message nicht vorhanden, falsche Anforderung
        }
    }

    publish (message, data) {
        this.each(this.Subscriber, function (value, key) {
            // geliefert wird jeweils ein Wert, hier ein Array, und der Key
            if (key == message) {
                // an alle Subscriber weitergeben
                this.each(value, function (entry, index) {
                    // geliefert wird hier das Element und der Index
                    this.defer(entry.notify, entry, message, data);
                });
            }
        })
    }

    defer (notifier, entry, message, data) {
        return setTimeout(function() {
            return notifier.apply(entry, [entry, message, data]);
        }, 1);
    }

    each (object, iterator) {
        for (let key in object) {
            iterator.call(this, object[key], key);
        }
    }

    findAll (object, iterator) {
        let results = [];

        this.each(object, function(value, index) {
            if (iterator.call(this, value, index)) {
                results.push(value);
            }
        });

        return results;
    }

    compact (object) {
        return this.findAll(object, function(value) {
            return value != null;
        });
    }
}
