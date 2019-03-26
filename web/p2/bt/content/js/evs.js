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
            if (this.Subscriber[message].indexOf(subscriber) == -1) {
                this.Subscriber[message].push(subscriber);
            }
        } else {
            this.Subscriber[message] = [subscriber];
        }
    }

    unsubscribe (subscriber, message) {
        if (message in this.Subscriber) {
            let entry = this.Subscriber[message];
            let index = entry.indexOf(subscriber);

            if (index >= 0) {
                entry[index] = null;
                entry = this.compact(entry);

                if (entry.length == 0) delete this.Subscriber[message];
            }
        } else {
            console.log("[EventService] unsubscribe->falsche Anforderung");
        }
    }

    publish (message, data) {
        this.each(this.Subscriber, function (value, key) {
            if (key == message) {
                this.each(value, function (entry, index) {
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
        for (let key in object) iterator.call(this, object[key], key);
    }

    findAll (object, iterator) {
        let results = [];
        this.each(object, function(value, index) {
            if (iterator.call(this, value, index)) results.push(value);
        });
        return results;
    }

    compact (object) {
        return this.findAll(object, function(value) { return value != null; });
    }
}
