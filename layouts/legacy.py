"""
Legacy Browser Specific Utilities
IE6-11, Old Chrome, Firefox, Safari
"""

def generate_legacy_utilities(generator):
    """Generate legacy browser specific utilities"""
    
    # IE hasLayout trigger (fixes many IE6/7 bugs)
    generator.add_rule(".haslayout", {"*zoom": "1"})
    
    # IE6/7 min-height hack
    generator.add_rule(".min-h-100", {
        "min-height": "100px",
        "_height": "100px"  # IE6 hack
    })
    
    # IE6/7 max-width hack
    generator.add_rule(".max-w-container", {
        "max-width": "1200px",
        "_width": "1200px"  # IE6 hack
    })
    
    # PNG transparency fix for IE6
    generator.add_rule(".png-fix", {
        "behavior": "url(iepngfix.htc)"  # Requires iepngfix.htc file
    })
    
    # IE6 double margin bug fix
    generator.add_rule(".float-left-ie6", {
        "float": "left",
        "_display": "inline"  # IE6 fix
    })
    
    generator.add_rule(".float-right-ie6", {
        "float": "right",
        "_display": "inline"  # IE6 fix
    })
    
    # IE7 overflow fix
    generator.add_rule(".overflow-fix", {
        "overflow": "hidden",
        "*overflow": "visible"  # IE7 hack
    })
    
    # IE8 box-shadow alternative (using border)
    generator.add_rule(".shadow-ie8", {
        "border": "1px solid #ccc",
        "\\9": ""  # IE8 and below
    })
    
    # Clearfix for all browsers
    generator.add_rule(".cf:before", {"content": "\" \"", "display": "table"})
    generator.add_rule(".cf:after", {"content": "\" \"", "display": "table", "clear": "both"})
    generator.add_rule(".cf", {"*zoom": "1"})
    
    # IE conditional classes helper
    generator.add_rule(".ie6-only", {"display": "none"})
    generator.add_rule(".ie7-only", {"display": "none"})
    generator.add_rule(".ie8-only", {"display": "none"})
    generator.add_rule(".ie9-only", {"display": "none"})
    
    # Old Firefox scrollbar styling
    generator.add_rule(".scrollbar-thin", {
        "scrollbar-width": "thin",
        "scrollbar-color": "#888 #f1f1f1"
    })
    
    # Webkit scrollbar (Chrome, Safari)
    generator.add_rule(".scrollbar-custom::-webkit-scrollbar", {"width": "8px"})
    generator.add_rule(".scrollbar-custom::-webkit-scrollbar-track", {"background": "#f1f1f1"})
    generator.add_rule(".scrollbar-custom::-webkit-scrollbar-thumb", {
        "background": "#888",
        "border-radius": "4px"
    })
    generator.add_rule(".scrollbar-custom::-webkit-scrollbar-thumb:hover", {"background": "#555"})
    
    # IE10+ specific (remove clear button from inputs)
    generator.add_rule("input::-ms-clear", {"display": "none"})
    generator.add_rule("input::-ms-reveal", {"display": "none"})
    
    # Old Safari text size adjust
    generator.add_rule(".text-size-adjust", {
        "-webkit-text-size-adjust": "100%",
        "-ms-text-size-adjust": "100%",
        "text-size-adjust": "100%"
    })
    
    # Font smoothing for old browsers
    generator.add_rule(".font-smooth", {
        "-webkit-font-smoothing": "antialiased",
        "-moz-osx-font-smoothing": "grayscale"
    })
    
    # IE9 SVG overflow fix
    generator.add_rule("svg:not(:root)", {"overflow": "hidden"})
    
    # Old browser button reset
    generator.add_rule(".btn-reset", {
        "background": "none",
        "border": "0",
        "color": "inherit",
        "font": "inherit",
        "line-height": "normal",
        "overflow": "visible",
        "padding": "0",
        "cursor": "pointer",
        "-webkit-appearance": "button",
        "-moz-appearance": "button"
    })
    
    # IE6/7 inline-block simulation
    generator.add_rule(".inline-block-legacy", {
        "display": "inline-block",
        "*display": "inline",
        "*zoom": "1"
    })
    
    # Old browser text selection
    generator.add_rule(".no-select", {
        "-webkit-user-select": "none",
        "-moz-user-select": "none",
        "-ms-user-select": "none",
        "user-select": "none"
    })
    
    # IE6/7 position fixed fallback
    generator.add_rule(".fixed-legacy", {
        "position": "fixed",
        "_position": "absolute",  # IE6 fallback
        "_top": "expression(eval(document.documentElement.scrollTop))"  # IE6 expression
    })
    
    # Old browser placeholder color
    generator.add_rule("::placeholder", {"color": "#999", "opacity": "1"})
    generator.add_rule("::-webkit-input-placeholder", {"color": "#999"})
    generator.add_rule("::-moz-placeholder", {"color": "#999", "opacity": "1"})
    generator.add_rule(":-ms-input-placeholder", {"color": "#999"})
    generator.add_rule(":-moz-placeholder", {"color": "#999", "opacity": "1"})
