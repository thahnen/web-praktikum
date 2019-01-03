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

   subscribe (Subscriber, Message) {
      if (Message in this.Subscriber) {
         // Message bekannt, Liste der Subscriber untersuchen
         if (this.Subscriber[Message].indexOf(Subscriber) == -1) {
            this.Subscriber[Message].push(Subscriber);
         }
      } else {
         // Message noch nicht vorhanden, neu eintragen
         this.Subscriber[Message] = [Subscriber];
      }
   }

   unsubscribe (Subscriber, Message) {
      if (Message in this.Subscriber) {
         // Message bekannt, Liste der Subscriber untersuchen
         let Entry = this.Subscriber[Message];
         let index = Entry.indexOf(Subscriber);
         if (index >= 0) {
            // Eintrag entfernen
            Entry[index] = null;
            Entry = this.compact(Entry); // compact liefert Kopie!
            if (Entry.length == 0) {
               // keine Subscriber mehr, kann entfernt werden
               delete this.Subscriber[Message];
            }
         }
      } else {
         // Message nicht vorhanden, falsche Anforderung
      }
   }

   publish (Message, Data) {
      this.each(this.Subscriber, function (value, key) {
         // geliefert wird jeweils ein Wert, hier ein Array, und der Key
         if (key == Message) {
            // an alle Subscriber weitergeben
            this.each(value, function (entry, index) {
               // geliefert wird hier das Element und der Index
               this.defer(entry.notify, entry, Message, Data);
            });
         }
      })
   }

   defer (notifier, entry, Message, Data) {
      return setTimeout(function() {
         return notifier.apply(entry, [entry, Message, Data]);
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
