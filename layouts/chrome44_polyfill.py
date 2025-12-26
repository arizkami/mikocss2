"""
Chrome 44 and Old Browser Polyfills
Fixes compatibility issues without removing features
"""

def generate_chrome44_fixes(generator):
    """Generate fixes for Chrome 44 and older browsers"""
    
    # CSS Variables fallback for browsers that don't support them
    generator.css_content.append("""
/* Chrome 44 and older browser fallbacks */

/* Fallback colors for browsers without CSS variable support */
.bg-scheme-primary {
  background-color: #ffffff;
  background-color: var(--bg-primary, #ffffff);
}

.bg-scheme-secondary {
  background-color: #f8f9fa;
  background-color: var(--bg-secondary, #f8f9fa);
}

.bg-scheme-tertiary {
  background-color: #e9ecef;
  background-color: var(--bg-tertiary, #e9ecef);
}

.text-scheme-primary {
  color: #212529;
  color: var(--text-primary, #212529);
}

.text-scheme-secondary {
  color: #6c757d;
  color: var(--text-secondary, #6c757d);
}

.text-scheme-tertiary {
  color: #adb5bd;
  color: var(--text-tertiary, #adb5bd);
}

.border-scheme {
  border-color: #dee2e6;
  border-color: var(--border-color, #dee2e6);
}

.shadow-scheme {
  -webkit-box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 4px var(--shadow-color, rgba(0, 0, 0, 0.1));
}

.link-scheme {
  color: #007bff;
  color: var(--link-color, #007bff);
}

.link-scheme:hover {
  color: #0056b3;
  color: var(--link-hover, #0056b3);
}

/* Dark mode fallbacks for Chrome 44 */
.dark-mode .bg-scheme-primary {
  background-color: #1a1a1a;
}

.dark-mode .bg-scheme-secondary {
  background-color: #2d2d2d;
}

.dark-mode .bg-scheme-tertiary {
  background-color: #3a3a3a;
}

.dark-mode .text-scheme-primary {
  color: #f8f9fa;
}

.dark-mode .text-scheme-secondary {
  color: #adb5bd;
}

.dark-mode .text-scheme-tertiary {
  color: #6c757d;
}

.dark-mode .border-scheme {
  border-color: #495057;
}

.dark-mode .shadow-scheme {
  -webkit-box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.dark-mode .link-scheme {
  color: #66b3ff;
}

.dark-mode .link-scheme:hover {
  color: #3399ff;
}

/* Light mode explicit fallbacks */
.light-mode .bg-scheme-primary {
  background-color: #ffffff;
}

.light-mode .text-scheme-primary {
  color: #212529;
}
""")
    
    # Fix for animations in old Chrome
    generator.css_content.append("""
/* Animation fixes for Chrome 44 and older */

/* Ensure all animations have -webkit- prefix */
.animate-pulse {
  -webkit-animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.animate-spin {
  -webkit-animation: spin 1s linear infinite;
  animation: spin 1s linear infinite;
}

.animate-bounce {
  -webkit-animation: bounce 1s infinite;
  animation: bounce 1s infinite;
}

.animate-ping {
  -webkit-animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
  animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
}

.animate-fade-in {
  -webkit-animation: fadeIn 0.5s ease-in;
  animation: fadeIn 0.5s ease-in;
}

.animate-fade-out {
  -webkit-animation: fadeOut 0.5s ease-out;
  animation: fadeOut 0.5s ease-out;
}

.animate-slide-in-left {
  -webkit-animation: slideInLeft 0.5s ease-out;
  animation: slideInLeft 0.5s ease-out;
}

.animate-slide-in-right {
  -webkit-animation: slideInRight 0.5s ease-out;
  animation: slideInRight 0.5s ease-out;
}

.animate-shake {
  -webkit-animation: shake 0.5s ease-in-out;
  animation: shake 0.5s ease-in-out;
}

.animate-wiggle {
  -webkit-animation: wiggle 1s ease-in-out infinite;
  animation: wiggle 1s ease-in-out infinite;
}

.animate-heartbeat {
  -webkit-animation: heartbeat 1.5s ease-in-out infinite;
  animation: heartbeat 1.5s ease-in-out infinite;
}

/* Animation duration with -webkit- prefix */
.animate-duration-75 { -webkit-animation-duration: 75ms; animation-duration: 75ms; }
.animate-duration-100 { -webkit-animation-duration: 100ms; animation-duration: 100ms; }
.animate-duration-150 { -webkit-animation-duration: 150ms; animation-duration: 150ms; }
.animate-duration-200 { -webkit-animation-duration: 200ms; animation-duration: 200ms; }
.animate-duration-300 { -webkit-animation-duration: 300ms; animation-duration: 300ms; }
.animate-duration-500 { -webkit-animation-duration: 500ms; animation-duration: 500ms; }
.animate-duration-700 { -webkit-animation-duration: 700ms; animation-duration: 700ms; }
.animate-duration-1000 { -webkit-animation-duration: 1000ms; animation-duration: 1000ms; }

/* Animation delay with -webkit- prefix */
.animate-delay-75 { -webkit-animation-delay: 75ms; animation-delay: 75ms; }
.animate-delay-100 { -webkit-animation-delay: 100ms; animation-delay: 100ms; }
.animate-delay-150 { -webkit-animation-delay: 150ms; animation-delay: 150ms; }
.animate-delay-200 { -webkit-animation-delay: 200ms; animation-delay: 200ms; }
.animate-delay-300 { -webkit-animation-delay: 300ms; animation-delay: 300ms; }
.animate-delay-500 { -webkit-animation-delay: 500ms; animation-delay: 500ms; }
.animate-delay-700 { -webkit-animation-delay: 700ms; animation-delay: 700ms; }
.animate-delay-1000 { -webkit-animation-delay: 1000ms; animation-delay: 1000ms; }

/* Animation iteration with -webkit- prefix */
.animate-once { -webkit-animation-iteration-count: 1; animation-iteration-count: 1; }
.animate-twice { -webkit-animation-iteration-count: 2; animation-iteration-count: 2; }
.animate-infinite { -webkit-animation-iteration-count: infinite; animation-iteration-count: infinite; }

/* Animation direction with -webkit- prefix */
.animate-normal { -webkit-animation-direction: normal; animation-direction: normal; }
.animate-reverse { -webkit-animation-direction: reverse; animation-direction: reverse; }
.animate-alternate { -webkit-animation-direction: alternate; animation-direction: alternate; }

/* Animation fill mode with -webkit- prefix */
.animate-fill-none { -webkit-animation-fill-mode: none; animation-fill-mode: none; }
.animate-fill-forwards { -webkit-animation-fill-mode: forwards; animation-fill-mode: forwards; }
.animate-fill-backwards { -webkit-animation-fill-mode: backwards; animation-fill-mode: backwards; }
.animate-fill-both { -webkit-animation-fill-mode: both; animation-fill-mode: both; }

/* Animation play state with -webkit- prefix */
.animate-paused { -webkit-animation-play-state: paused; animation-play-state: paused; }
.animate-running { -webkit-animation-play-state: running; animation-play-state: running; }
""")
    
    # Flexbox fixes for old Chrome
    generator.css_content.append("""
/* Flexbox fixes for Chrome 44 and older */
.flex {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
}

.inline-flex {
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
}

.flex-row {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -webkit-flex-direction: row;
  -ms-flex-direction: row;
  flex-direction: row;
}

.flex-col {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
}

.items-center {
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}

.justify-between {
  -webkit-box-pack: justify;
  -webkit-justify-content: space-between;
  -ms-flex-pack: justify;
  justify-content: space-between;
}

.flex-wrap {
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
}
""")


def generate_chrome44_js_polyfill():
    """Generate JavaScript polyfills for Chrome 44"""
    js = """
// Chrome 44 and Old Browser Polyfills
// Ensures compatibility without removing features

(function() {
  'use strict';
  
  // Polyfill for classList (partial support in old browsers)
  if (!('classList' in document.createElement('_'))) {
    (function(view) {
      if (!('Element' in view)) return;
      
      var classListProp = 'classList',
          protoProp = 'prototype',
          elemCtrProto = view.Element[protoProp],
          objCtr = Object,
          strTrim = String[protoProp].trim || function() {
            return this.replace(/^\\s+|\\s+$/g, '');
          },
          arrIndexOf = Array[protoProp].indexOf || function(item) {
            var i = 0, len = this.length;
            for (; i < len; i++) {
              if (i in this && this[i] === item) {
                return i;
              }
            }
            return -1;
          },
          DOMEx = function(type, message) {
            this.name = type;
            this.code = DOMException[type];
            this.message = message;
          },
          checkTokenAndGetIndex = function(classList, token) {
            if (token === '') {
              throw new DOMEx('SYNTAX_ERR', 'An invalid or illegal string was specified');
            }
            if (/\\s/.test(token)) {
              throw new DOMEx('INVALID_CHARACTER_ERR', 'String contains an invalid character');
            }
            return arrIndexOf.call(classList, token);
          },
          ClassList = function(elem) {
            var trimmedClasses = strTrim.call(elem.getAttribute('class') || ''),
                classes = trimmedClasses ? trimmedClasses.split(/\\s+/) : [],
                i = 0,
                len = classes.length;
            for (; i < len; i++) {
              this.push(classes[i]);
            }
            this._updateClassName = function() {
              elem.setAttribute('class', this.toString());
            };
          },
          classListProto = ClassList[protoProp] = [],
          classListGetter = function() {
            return new ClassList(this);
          };
      
      DOMEx[protoProp] = Error[protoProp];
      classListProto.item = function(i) {
        return this[i] || null;
      };
      classListProto.contains = function(token) {
        token += '';
        return checkTokenAndGetIndex(this, token) !== -1;
      };
      classListProto.add = function() {
        var tokens = arguments,
            i = 0,
            l = tokens.length,
            token,
            updated = false;
        do {
          token = tokens[i] + '';
          if (checkTokenAndGetIndex(this, token) === -1) {
            this.push(token);
            updated = true;
          }
        } while (++i < l);
        
        if (updated) {
          this._updateClassName();
        }
      };
      classListProto.remove = function() {
        var tokens = arguments,
            i = 0,
            l = tokens.length,
            token,
            updated = false,
            index;
        do {
          token = tokens[i] + '';
          index = checkTokenAndGetIndex(this, token);
          while (index !== -1) {
            this.splice(index, 1);
            updated = true;
            index = checkTokenAndGetIndex(this, token);
          }
        } while (++i < l);
        
        if (updated) {
          this._updateClassName();
        }
      };
      classListProto.toggle = function(token, force) {
        token += '';
        
        var result = this.contains(token),
            method = result ? force !== true && 'remove' : force !== false && 'add';
        
        if (method) {
          this[method](token);
        }
        
        if (force === true || force === false) {
          return force;
        } else {
          return !result;
        }
      };
      classListProto.toString = function() {
        return this.join(' ');
      };
      
      if (objCtr.defineProperty) {
        var classListPropDesc = {
          get: classListGetter,
          enumerable: true,
          configurable: true
        };
        try {
          objCtr.defineProperty(elemCtrProto, classListProp, classListPropDesc);
        } catch (ex) {
          if (ex.number === -0x7FF5EC54) {
            classListPropDesc.enumerable = false;
            objCtr.defineProperty(elemCtrProto, classListProp, classListPropDesc);
          }
        }
      } else if (objCtr[protoProp].__defineGetter__) {
        elemCtrProto.__defineGetter__(classListProp, classListGetter);
      }
    }(self));
  }
  
  // Polyfill for localStorage (in case it's not available)
  if (typeof localStorage === 'undefined') {
    window.localStorage = {
      _data: {},
      setItem: function(id, val) { return this._data[id] = String(val); },
      getItem: function(id) { return this._data.hasOwnProperty(id) ? this._data[id] : null; },
      removeItem: function(id) { return delete this._data[id]; },
      clear: function() { return this._data = {}; }
    };
  }
  
  // Polyfill for matchMedia (basic support)
  if (!window.matchMedia) {
    window.matchMedia = function(query) {
      return {
        matches: false,
        media: query,
        addListener: function() {},
        removeListener: function() {}
      };
    };
  }
  
  // Polyfill for CustomEvent
  if (typeof window.CustomEvent !== 'function') {
    function CustomEvent(event, params) {
      params = params || { bubbles: false, cancelable: false, detail: undefined };
      var evt = document.createEvent('CustomEvent');
      evt.initCustomEvent(event, params.bubbles, params.cancelable, params.detail);
      return evt;
    }
    CustomEvent.prototype = window.Event.prototype;
    window.CustomEvent = CustomEvent;
  }
  
  // Polyfill for Array.indexOf (IE8-)
  if (!Array.prototype.indexOf) {
    Array.prototype.indexOf = function(searchElement, fromIndex) {
      var k;
      if (this == null) {
        throw new TypeError('"this" is null or not defined');
      }
      var o = Object(this);
      var len = o.length >>> 0;
      if (len === 0) {
        return -1;
      }
      var n = +fromIndex || 0;
      if (Math.abs(n) === Infinity) {
        n = 0;
      }
      if (n >= len) {
        return -1;
      }
      k = Math.max(n >= 0 ? n : len - Math.abs(n), 0);
      while (k < len) {
        if (k in o && o[k] === searchElement) {
          return k;
        }
        k++;
      }
      return -1;
    };
  }
  
  // Polyfill for Array.forEach (IE8-)
  if (!Array.prototype.forEach) {
    Array.prototype.forEach = function(callback, thisArg) {
      var T, k;
      if (this == null) {
        throw new TypeError('this is null or not defined');
      }
      var O = Object(this);
      var len = O.length >>> 0;
      if (typeof callback !== 'function') {
        throw new TypeError(callback + ' is not a function');
      }
      if (arguments.length > 1) {
        T = thisArg;
      }
      k = 0;
      while (k < len) {
        var kValue;
        if (k in O) {
          kValue = O[k];
          callback.call(T, kValue, k, O);
        }
        k++;
      }
    };
  }
  
  // Console polyfill for old browsers
  if (!window.console) {
    window.console = {
      log: function() {},
      warn: function() {},
      error: function() {},
      info: function() {}
    };
  }
  
})();
"""
    return js
