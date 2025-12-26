"""
JavaScript Generator for Production
Generates minified CSS-in-JS and utility functions
"""
import json
import re

class JSGenerator:
    def __init__(self):
        self.js_content = []
    
    def css_to_js_object(self, css_content):
        """Convert CSS to JavaScript object format"""
        # Parse CSS rules into JS object
        rules = {}
        current_selector = None
        current_props = {}
        
        lines = css_content.split('\n')
        for line in lines:
            line = line.strip()
            
            # Skip comments and empty lines
            if line.startswith('/*') or line.startswith('*') or not line:
                continue
            
            # Detect selector
            if '{' in line and not line.startswith('@'):
                current_selector = line.split('{')[0].strip()
                current_props = {}
            
            # Detect property
            elif ':' in line and ';' in line and current_selector:
                prop = line.split(':')[0].strip()
                value = line.split(':')[1].replace(';', '').strip()
                current_props[prop] = value
            
            # End of rule
            elif '}' in line and current_selector:
                if current_props:
                    rules[current_selector] = current_props
                current_selector = None
                current_props = {}
        
        return rules
    
    def generate_css_in_js(self, css_content, var_name="styles"):
        """Generate CSS-in-JS format"""
        js = f"// Cogeden CSS-in-JS - Production Ready\n"
        js += f"// Generated: {self._get_timestamp()}\n\n"
        js += f"const {var_name} = {{\n"
        
        rules = self.css_to_js_object(css_content)
        
        for selector, props in rules.items():
            safe_key = self._sanitize_key(selector)
            js += f"  '{safe_key}': {{\n"
            for prop, value in props.items():
                js += f"    '{prop}': '{value}',\n"
            js += f"  }},\n"
        
        js += "};\n\n"
        js += f"export default {var_name};\n"
        
        return js
    
    def generate_utility_functions(self):
        """Generate utility functions for dynamic styling"""
        js = """
// Cogeden Utility Functions
// Production-ready helpers for legacy browser support

const CogedenUtils = {
  // Apply styles to element
  applyStyles: function(element, styles) {
    if (!element) return;
    for (var prop in styles) {
      if (styles.hasOwnProperty(prop)) {
        element.style[prop] = styles[prop];
      }
    }
  },

  // Add class with legacy support
  addClass: function(element, className) {
    if (!element) return;
    if (element.classList) {
      element.classList.add(className);
    } else {
      // IE9- fallback
      var classes = element.className.split(' ');
      if (classes.indexOf(className) === -1) {
        element.className += ' ' + className;
      }
    }
  },

  // Remove class with legacy support
  removeClass: function(element, className) {
    if (!element) return;
    if (element.classList) {
      element.classList.remove(className);
    } else {
      // IE9- fallback
      var classes = element.className.split(' ');
      var index = classes.indexOf(className);
      if (index > -1) {
        classes.splice(index, 1);
        element.className = classes.join(' ');
      }
    }
  },

  // Toggle class with legacy support
  toggleClass: function(element, className) {
    if (!element) return;
    if (element.classList) {
      element.classList.toggle(className);
    } else {
      // IE9- fallback
      if (this.hasClass(element, className)) {
        this.removeClass(element, className);
      } else {
        this.addClass(element, className);
      }
    }
  },

  // Check if element has class
  hasClass: function(element, className) {
    if (!element) return false;
    if (element.classList) {
      return element.classList.contains(className);
    } else {
      // IE9- fallback
      return element.className.split(' ').indexOf(className) > -1;
    }
  },

  // Query selector with IE7+ support
  query: function(selector, context) {
    context = context || document;
    if (context.querySelector) {
      return context.querySelector(selector);
    } else {
      // IE7 fallback
      return context.getElementById(selector.replace('#', ''));
    }
  },

  // Query all with IE7+ support
  queryAll: function(selector, context) {
    context = context || document;
    if (context.querySelectorAll) {
      return context.querySelectorAll(selector);
    } else {
      // IE7 fallback
      return context.getElementsByTagName(selector);
    }
  },

  // Add event listener with IE8+ support
  on: function(element, event, handler) {
    if (!element) return;
    if (element.addEventListener) {
      element.addEventListener(event, handler, false);
    } else if (element.attachEvent) {
      // IE8 fallback
      element.attachEvent('on' + event, handler);
    }
  },

  // Remove event listener with IE8+ support
  off: function(element, event, handler) {
    if (!element) return;
    if (element.removeEventListener) {
      element.removeEventListener(event, handler, false);
    } else if (element.detachEvent) {
      // IE8 fallback
      element.detachEvent('on' + event, handler);
    }
  },

  // Get computed style with IE8+ support
  getStyle: function(element, property) {
    if (!element) return null;
    if (window.getComputedStyle) {
      return window.getComputedStyle(element, null)[property];
    } else if (element.currentStyle) {
      // IE8 fallback
      return element.currentStyle[property];
    }
    return null;
  },

  // Detect IE version
  detectIE: function() {
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf('MSIE ');
    if (msie > 0) {
      return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
    }
    var trident = ua.indexOf('Trident/');
    if (trident > 0) {
      var rv = ua.indexOf('rv:');
      return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
    }
    return false;
  },

  // Check if browser is legacy
  isLegacyBrowser: function() {
    var ie = this.detectIE();
    return ie && ie <= 11;
  },

  // Polyfill for Array.indexOf (IE8-)
  arrayIndexOf: function(array, item) {
    if (Array.prototype.indexOf) {
      return array.indexOf(item);
    }
    for (var i = 0; i < array.length; i++) {
      if (array[i] === item) return i;
    }
    return -1;
  },

  // Polyfill for Array.forEach (IE8-)
  arrayForEach: function(array, callback) {
    if (Array.prototype.forEach) {
      array.forEach(callback);
    } else {
      for (var i = 0; i < array.length; i++) {
        callback(array[i], i, array);
      }
    }
  },

  // Create element with attributes
  createElement: function(tag, attributes, content) {
    var element = document.createElement(tag);
    if (attributes) {
      for (var attr in attributes) {
        if (attributes.hasOwnProperty(attr)) {
          element.setAttribute(attr, attributes[attr]);
        }
      }
    }
    if (content) {
      element.innerHTML = content;
    }
    return element;
  },

  // Inject CSS into page
  injectCSS: function(css) {
    var style = document.createElement('style');
    style.type = 'text/css';
    if (style.styleSheet) {
      // IE8 and below
      style.styleSheet.cssText = css;
    } else {
      style.appendChild(document.createTextNode(css));
    }
    document.head.appendChild(style);
  },

  // Responsive breakpoint checker
  matchMedia: function(query) {
    if (window.matchMedia) {
      return window.matchMedia(query).matches;
    }
    // Fallback for old browsers
    return false;
  },

  // Get viewport dimensions
  getViewport: function() {
    return {
      width: window.innerWidth || document.documentElement.clientWidth,
      height: window.innerHeight || document.documentElement.clientHeight
    };
  }
};

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CogedenUtils;
}
if (typeof define === 'function' && define.amd) {
  define(function() { return CogedenUtils; });
}

// Global export
window.CogedenUtils = CogedenUtils;
"""
        return js
    
    def generate_minified_loader(self, css_file):
        """Generate minified CSS loader"""
        js = f"""
// Cogeden CSS Loader - Minified
(function(){{var l=document.createElement('link');l.rel='stylesheet';l.href='{css_file}';document.head.appendChild(l);}})();
"""
        return js.strip()
    
    def generate_build_config(self):
        """Generate build configuration"""
        config = {
            "name": "cogeden-css",
            "version": "1.0.0",
            "description": "Ultimate CSS system for legacy browsers",
            "main": "dist/cogeden.min.css",
            "scripts": {
                "build": "python main.py dist/cogeden.css",
                "build:min": "python build.py --minify",
                "build:prod": "python build.py --production"
            },
            "files": [
                "dist/",
                "core/",
                "layouts/"
            ],
            "keywords": [
                "css",
                "legacy",
                "ie6",
                "ie7",
                "ie8",
                "ie9",
                "ie10",
                "ie11",
                "responsive",
                "utility"
            ],
            "browser_support": {
                "ie": "6-11",
                "chrome": "1+",
                "firefox": "1+",
                "safari": "3+",
                "opera": "9+",
                "servo": "all"
            }
        }
        return json.dumps(config, indent=2)
    
    def _sanitize_key(self, key):
        """Sanitize CSS selector for JS object key"""
        return key.replace('.', '').replace('#', '').replace(':', '_').replace(' ', '_')
    
    def _get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
