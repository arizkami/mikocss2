"""
Automatic Color Scheme System (Light/Dark Mode)
With legacy browser support
"""

def generate_color_scheme_system(generator):
    """Generate automatic light/dark color scheme system"""
    
    # CSS Variables for color scheme (IE11+)
    generator.css_content.append("""
/* Color Scheme Variables */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-tertiary: #e9ecef;
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --text-tertiary: #adb5bd;
  --border-color: #dee2e6;
  --shadow-color: rgba(0, 0, 0, 0.1);
  --link-color: #007bff;
  --link-hover: #0056b3;
}

/* Dark mode variables */
@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #1a1a1a;
    --bg-secondary: #2d2d2d;
    --bg-tertiary: #3a3a3a;
    --text-primary: #f8f9fa;
    --text-secondary: #adb5bd;
    --text-tertiary: #6c757d;
    --border-color: #495057;
    --shadow-color: rgba(0, 0, 0, 0.5);
    --link-color: #66b3ff;
    --link-hover: #3399ff;
  }
}

/* Manual dark mode class */
.dark-mode {
  --bg-primary: #1a1a1a;
  --bg-secondary: #2d2d2d;
  --bg-tertiary: #3a3a3a;
  --text-primary: #f8f9fa;
  --text-secondary: #adb5bd;
  --text-tertiary: #6c757d;
  --border-color: #495057;
  --shadow-color: rgba(0, 0, 0, 0.5);
  --link-color: #66b3ff;
  --link-hover: #3399ff;
}

/* Manual light mode class */
.light-mode {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-tertiary: #e9ecef;
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --text-tertiary: #adb5bd;
  --border-color: #dee2e6;
  --shadow-color: rgba(0, 0, 0, 0.1);
  --link-color: #007bff;
  --link-hover: #0056b3;
}
""")
    
    # Utility classes using CSS variables
    generator.add_rule(".bg-scheme-primary", {
        "background-color": "var(--bg-primary, #ffffff)"
    })
    
    generator.add_rule(".bg-scheme-secondary", {
        "background-color": "var(--bg-secondary, #f8f9fa)"
    })
    
    generator.add_rule(".bg-scheme-tertiary", {
        "background-color": "var(--bg-tertiary, #e9ecef)"
    })
    
    generator.add_rule(".text-scheme-primary", {
        "color": "var(--text-primary, #212529)"
    })
    
    generator.add_rule(".text-scheme-secondary", {
        "color": "var(--text-secondary, #6c757d)"
    })
    
    generator.add_rule(".text-scheme-tertiary", {
        "color": "var(--text-tertiary, #adb5bd)"
    })
    
    generator.add_rule(".border-scheme", {
        "border-color": "var(--border-color, #dee2e6)"
    })
    
    generator.add_rule(".shadow-scheme", {
        "box-shadow": "0 2px 4px var(--shadow-color, rgba(0, 0, 0, 0.1))"
    })
    
    generator.add_rule(".link-scheme", {
        "color": "var(--link-color, #007bff)"
    })
    
    generator.add_rule(".link-scheme:hover", {
        "color": "var(--link-hover, #0056b3)"
    })
    
    # Legacy browser fallbacks (IE9-10)
    generator.css_content.append("""
/* IE9-10 Fallbacks */
.bg-scheme-primary {
  background-color: #ffffff\\9;
}
.dark-mode .bg-scheme-primary {
  background-color: #1a1a1a\\9;
}

.text-scheme-primary {
  color: #212529\\9;
}
.dark-mode .text-scheme-primary {
  color: #f8f9fa\\9;
}
""")
    
    # Prefers color scheme utilities
    generator.css_content.append("""
/* Auto dark mode utilities */
@media (prefers-color-scheme: dark) {
  .auto-dark\\:bg-dark {
    background-color: #1a1a1a;
  }
  .auto-dark\\:text-light {
    color: #f8f9fa;
  }
  .auto-dark\\:border-dark {
    border-color: #495057;
  }
}

/* Auto light mode utilities */
@media (prefers-color-scheme: light) {
  .auto-light\\:bg-light {
    background-color: #ffffff;
  }
  .auto-light\\:text-dark {
    color: #212529;
  }
  .auto-light\\:border-light {
    border-color: #dee2e6;
  }
}
""")
    
    # Dark mode specific utilities (both auto and manual)
    # Auto dark mode (prefers-color-scheme)
    generator.add_rule(".dark\\:bg-gray-900", {
        "background-color": "#1a1a1a"
    }, "(prefers-color-scheme: dark)")
    
    generator.add_rule(".dark\\:text-white", {
        "color": "#ffffff"
    }, "(prefers-color-scheme: dark)")
    
    generator.add_rule(".dark\\:border-gray-700", {
        "border-color": "#495057"
    }, "(prefers-color-scheme: dark)")
    
    # Manual dark mode class
    generator.add_rule(".dark-mode .dark\\:bg-gray-900", {
        "background-color": "#1a1a1a"
    })
    
    generator.add_rule(".dark-mode .dark\\:text-white", {
        "color": "#ffffff"
    })
    
    generator.add_rule(".dark-mode .dark\\:border-gray-700", {
        "border-color": "#495057"
    })
    
    # Light mode specific utilities (both auto and manual)
    # Auto light mode (prefers-color-scheme)
    generator.add_rule(".light\\:bg-white", {
        "background-color": "#ffffff"
    }, "(prefers-color-scheme: light)")
    
    generator.add_rule(".light\\:text-black", {
        "color": "#000000"
    }, "(prefers-color-scheme: light)")
    
    generator.add_rule(".light\\:border-gray-300", {
        "border-color": "#dee2e6"
    }, "(prefers-color-scheme: light)")
    
    # Manual light mode class
    generator.add_rule(".light-mode .light\\:bg-white", {
        "background-color": "#ffffff"
    })
    
    generator.add_rule(".light-mode .light\\:text-black", {
        "color": "#000000"
    })
    
    generator.add_rule(".light-mode .light\\:border-gray-300", {
        "border-color": "#dee2e6"
    })


def generate_theme_switcher_js():
    """Generate JavaScript for theme switching"""
    js = """
// Cogeden Theme Switcher
// Supports automatic and manual light/dark mode

(function() {
  'use strict';
  
  var CogedenTheme = {
    // Get current theme
    getTheme: function() {
      // Check localStorage
      var stored = localStorage.getItem('cogeden-theme');
      if (stored) return stored;
      
      // Check system preference
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark';
      }
      
      return 'light';
    },
    
    // Set theme
    setTheme: function(theme) {
      var html = document.documentElement;
      
      // Remove existing theme classes
      html.classList.remove('light-mode', 'dark-mode');
      
      // Add new theme class
      if (theme === 'dark') {
        html.classList.add('dark-mode');
      } else {
        html.classList.add('light-mode');
      }
      
      // Save to localStorage
      try {
        localStorage.setItem('cogeden-theme', theme);
      } catch (e) {
        // localStorage not available
      }
      
      // Dispatch event
      if (typeof CustomEvent !== 'undefined') {
        var event = new CustomEvent('themechange', { detail: { theme: theme } });
        document.dispatchEvent(event);
      }
    },
    
    // Toggle theme
    toggleTheme: function() {
      var current = this.getTheme();
      var newTheme = current === 'dark' ? 'light' : 'dark';
      this.setTheme(newTheme);
      return newTheme;
    },
    
    // Initialize theme
    init: function() {
      var theme = this.getTheme();
      this.setTheme(theme);
      
      // Listen for system theme changes
      if (window.matchMedia) {
        var darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        // Modern browsers
        if (darkModeQuery.addEventListener) {
          darkModeQuery.addEventListener('change', function(e) {
            if (!localStorage.getItem('cogeden-theme')) {
              CogedenTheme.setTheme(e.matches ? 'dark' : 'light');
            }
          });
        }
        // IE10-11
        else if (darkModeQuery.addListener) {
          darkModeQuery.addListener(function(e) {
            if (!localStorage.getItem('cogeden-theme')) {
              CogedenTheme.setTheme(e.matches ? 'dark' : 'light');
            }
          });
        }
      }
    },
    
    // Create theme toggle button
    createToggleButton: function(container, options) {
      options = options || {};
      var button = document.createElement('button');
      button.className = options.className || 'btn btn-secondary';
      button.setAttribute('aria-label', 'Toggle theme');
      button.innerHTML = options.lightIcon || '☀️';
      
      var self = this;
      button.onclick = function() {
        var newTheme = self.toggleTheme();
        button.innerHTML = newTheme === 'dark' ? 
          (options.darkIcon || '🌙') : 
          (options.lightIcon || '☀️');
      };
      
      // Set initial icon
      var currentTheme = this.getTheme();
      button.innerHTML = currentTheme === 'dark' ? 
        (options.darkIcon || '🌙') : 
        (options.lightIcon || '☀️');
      
      if (container) {
        if (typeof container === 'string') {
          container = document.querySelector(container);
        }
        if (container) {
          container.appendChild(button);
        }
      }
      
      return button;
    }
  };
  
  // Auto-initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      CogedenTheme.init();
    });
  } else {
    CogedenTheme.init();
  }
  
  // Export
  window.CogedenTheme = CogedenTheme;
  
  // Module export
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CogedenTheme;
  }
})();
"""
    return js
