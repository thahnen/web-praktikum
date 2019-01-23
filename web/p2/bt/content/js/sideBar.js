'use strict';

// REVIEW: Eigentlich soweit fertig!

export default class {
    constructor (name, template) {
        this.elem_name = name;
        this.template_name = template;
        this.html_element = document.querySelector(this.elem_name);

        if (this.html_element == null) {
            alert("[SideBar] HTML-Element nicht gefunden!")
            return;
        }

        this.html_element.addEventListener("click", function(event) {
            APPUTIL.eventService.publish("app.cmd", [
                event.target.dataset.action, null
            ]);
        });
    }

    render (data) {
        let markup = APPUTIL.templateManager.execute(this.template_name, data);
        if (markup == null) {
            alert("[SideBar] Template nicht renderbar!")
            return;
        }

        this.html_element.innerHTML = markup;
    }
}
