//------------------------------------------------------------------------------
// Template-Engine: Compiler
//------------------------------------------------------------------------------

'use strict'

var APPUTIL = APPUTIL || {};

APPUTIL.Generator = class {
    constructor () { this.reset(); }

    reset () { this.code_after = ['var result_after = [];\n']; }

    write (text) {
        // Escape-Zeichen bei Strings ergänzen
        let text_source = text.replace(/"/g, '\\"');
        text_source = text_source.replace(/'/g, "\\'");
        this.code_after.push('result_after.push("' + text_source + '");\n');
    }

    code (code_source) {
        if (code_source.startsWith('if')) {
            this.code_after.push('if (' + code_source.substr(2) + ') {\n');
        } else if (code_source.startsWith('else')) {
            this.code_after.push('} else {\n');
        } else if (code_source.startsWith('endif')) {
            this.code_after.push('}\n');
        } else if (code_source.startsWith('for')) {
            this.code_after.push('for (' + code_source.substr(3) + ') {\n');
        } else if (code_source.startsWith('endfor')) {
            this.code_after.push('}\n');
        } else if (code_source.startsWith('include')) {
            // Aufbau: include template data-object
            let parts = code_source.split(' '); // einfache Lösung
            this.code_after.push('result_after.push(new APPUTIL.TemplateManager().execute("' + parts[1] + '",' + parts[2] + '));\n');
        } else {
            this.code_after.push(code_source + '\n');
        }
    }

    substitute (substitute_source) {
        let value = substitute_source == null ? '' : String(substitute_source);
        this.code_after.push('result_after.push(' + value + ');\n');
    }

    generate () {
        let result = this.code_after.join('') + ' return result_after.join("");';
        let func = new Function ('context', result);
        return func;
    }
}


APPUTIL.TemplateCompiler = class {
    constructor () {
        this.generator = new APPUTIL.Generator();
        this.reset();
    }

    reset () {
        this.generator.reset();
        this.preservePRE = false;
        this.preservePOST = false;
    }

    setPRE (on_was_soll_die_variable) {
        if ((on_was_soll_die_variable == undefined) || (on_was_soll_die_variable == false)) {
            this.preservePRE = false;
        } else {
            this.preservePRE = true;
        }
    }

    setPOST (on_was_soll_die_variable) {
        if ((on_was_soll_die_variable == undefined) || (on_was_soll_die_variable == false)) {
            this.preservePOST = false;
        } else {
            this.preservePOST = true;
        }
    }

    compile (code_source) {
        let state = 0;
        let pos = 0;
        let len = code_source.length;
        let text_source = '';
        let code_script = '';
        let substitute_source = '';
        this.generator.reset();

        // Test, ob das Zeichen noch einmal vorhanden (bsp bei @ ... @)
        var doubletest = function (buchstabe) {
            let status = false;

            if ((pos + 1) < len) {
                if ((code_source[pos] == buchstabe) && (code_source[pos+1] == buchstabe)) {
                    status = true;
                }
            }
            return status;
        }

        while (pos < len) {
            switch (state) {
                case 0:
                    // outside
                    if (code_source[pos] == '@') {
                        if (doubletest('@') == false) {
                            state = 2;
                            code_script = '';
                        } else { // als normales Zeichen verarbeiten, ein Zeichen überlesen
                            state = 1;
                            text_source = '@';
                            pos++;
                        }
                    } else if (code_source[pos] == '#') {
                        if (doubletest('#') == false) {
                            state = 3;
                            substitute_source = '';
                        } else { // als normales Zeichen verarbeiten, ein Zeichen überlesen
                            state = 1;
                            text_source = '#';
                            pos++;
                        }
                    } else if ((code_source[pos] == ' ') || (code_source[pos] == '\t')) {
                        state = 4;
                        text_source = '';
                        pos--; // Zeichen erneut verarbeiten
                    } else {
                        state = 1;
                        text_source = '';
                        pos--; // Zeichen erneut verarbeiten
                    }
                    break;
                case 1:
                    // inText
                    if (code_source[pos] == '@') {
                        if (doubletest('@') == false) { // Textende, neuer Code
                            state = 0;
                            this.generator.write(text_source);
                            pos--; // Zeichen erneut verarbeiten
                        } else { // als normales Zeichen verarbeiten, ein Zeichen überlesen
                            text_source += '@';
                            pos++;
                        }
                    } else if (code_source[pos] == '#') {
                        if (doubletest('#') == false) { // Textende, neue Substitution
                            state = 0;
                            this.generator.write(text_source);
                            pos--; // Zeichen erneut verarbeiten
                        } else { // als normales Zeichen verarbeiten, ein Zeichen überlesen
                            text_source += '#';
                            pos++;
                        }
                    } else if ((code_source[pos] == ' ') || (code_source[pos] == '\t')) { // Textende
                        state = 0;
                        this.generator.write(text_source);
                        pos--; // Zeichen erneut verarbeiten
                    } else {
                        // sammeln
                        if ((code_source[pos] != '\n') && (code_source[pos] != '\r')) {
                            text_source += code_source[pos];
                        } else if (code_source[pos] == '\n') {
                            text_source += '\\n';
                        } else {
                            text_source += '\\r';
                        }
                    }
                    break;
                case 2:
                    // inCode
                    if (code_source[pos] == '@') {
                        if (doubletest('@') == false) { // zu Ende, erzeugen
                            this.generator.code(code_script);
                            state = 5;  //0
                        } else { // als normales Zeichen verarbeiten, ein Zeichen überlesen
                            code_script += '@';
                            pos++;
                        }
                    } else {
                        // sammeln
                        code_script += code_source[pos];
                    }
                    break;
                case 3:
                    // inSubst
                    if (code_source[pos] == '#') { // zu Ende, erzeugen
                        this.generator.substitute(substitute_source);
                        state = 0;
                    } else {
                        // sammeln
                        substitute_source += code_source[pos];
                    }
                    break;
                case 4:
                    // pre-code-whitespace
                    switch (code_source[pos]) {
                        case ' ':
                        case '\t':
                            // sammeln
                            text_source += code_source[pos];
                            break;
                        default:
                            state = 0;
                            if (code_source[pos] != '@') {
                                this.generator.write(text_source);
                            } else {
                                if (doubletest('@') == false) { // Whitespace vor Code-Beginn erkannt
                                    if (this.preservePRE == true) {
                                        this.generator.write(text_source);
                                    }
                                }
                            }
                            pos--; // Zeichen erneut verarbeiten
                    }
                    break;
                case 5:
                    // post-code-whitespace
                    switch (code_source[pos]) {
                        case '\n':
                            text_source += '\\n';
                            state = 0;
                            break;
                        case '\r':
                            text_source += '\\r';
                            state = 0;
                            break;
                        case ' ':
                        case '\t':
                            // sammeln
                            text_source += code_source[pos];
                            break;
                        default:
                            // Whitespace nach Code erkannt
                            if (this.preservePOST == true) {
                                this.generator.write(text_source);
                            }
                            state = 0;
                            pos--; // Zeichen erneut verarbeiten
                    }
                    break;
            }
            pos++;
        }

        // welcher Zustand liegt abschließend vor?
        if (state == 1) {
            this.generator.write(text_source);
        } else if (state == 2) {
            this.generator.code(code_script);
        } else if (state == 3) {
            this.generator.substitute(substitute_source);
        } else if (state == 4) {
            if (this.preservePRE == true) this.generator.write(text_source);
        } else if (state == 5) {
            if (this.preservePOST == true) this.generator.write(text_source);
        }

        return this.generator.generate();
    }
}
