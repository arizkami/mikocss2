"""
Button Utilities for Legacy Browsers
"""

def generate_button_utilities(generator):
    """Generate comprehensive button utilities"""
    
    # Base button
    generator.add_rule(".btn", {
        "display": "inline-block",
        "font-weight": "400",
        "text-align": "center",
        "white-space": "nowrap",
        "vertical-align": "middle",
        "user-select": "none",
        "border": "1px solid transparent",
        "padding": "8px 16px",
        "font-size": "14px",
        "line-height": "1.5",
        "border-radius": "4px",
        "cursor": "pointer",
        "transition": "all 0.15s ease-in-out"
    })
    
    generator.add_rule(".btn:hover", {
        "text-decoration": "none",
        "opacity": "0.85"
    })
    
    generator.add_rule(".btn:focus", {
        "outline": "0",
        "box-shadow": "0 0 0 3px rgba(0, 123, 255, 0.25)"
    })
    
    generator.add_rule(".btn:disabled", {
        "opacity": "0.65",
        "cursor": "not-allowed"
    })
    
    # Button variants
    generator.add_rule(".btn-primary", {
        "color": "#fff",
        "background-color": "#007bff",
        "border-color": "#007bff"
    })
    
    generator.add_rule(".btn-secondary", {
        "color": "#fff",
        "background-color": "#6c757d",
        "border-color": "#6c757d"
    })
    
    generator.add_rule(".btn-success", {
        "color": "#fff",
        "background-color": "#28a745",
        "border-color": "#28a745"
    })
    
    generator.add_rule(".btn-danger", {
        "color": "#fff",
        "background-color": "#dc3545",
        "border-color": "#dc3545"
    })
    
    generator.add_rule(".btn-warning", {
        "color": "#212529",
        "background-color": "#ffc107",
        "border-color": "#ffc107"
    })
    
    generator.add_rule(".btn-info", {
        "color": "#fff",
        "background-color": "#17a2b8",
        "border-color": "#17a2b8"
    })
    
    generator.add_rule(".btn-light", {
        "color": "#212529",
        "background-color": "#f8f9fa",
        "border-color": "#f8f9fa"
    })
    
    generator.add_rule(".btn-dark", {
        "color": "#fff",
        "background-color": "#343a40",
        "border-color": "#343a40"
    })
    
    # Outline buttons
    generator.add_rule(".btn-outline-primary", {
        "color": "#007bff",
        "background-color": "transparent",
        "border-color": "#007bff"
    })
    
    generator.add_rule(".btn-outline-primary:hover", {
        "color": "#fff",
        "background-color": "#007bff",
        "border-color": "#007bff"
    })
    
    # Button sizes
    generator.add_rule(".btn-sm", {
        "padding": "4px 8px",
        "font-size": "12px",
        "border-radius": "3px"
    })
    
    generator.add_rule(".btn-lg", {
        "padding": "12px 24px",
        "font-size": "18px",
        "border-radius": "6px"
    })
    
    # Block button
    generator.add_rule(".btn-block", {
        "display": "block",
        "width": "100%"
    })
    
    # Button group
    generator.add_rule(".btn-group", {
        "position": "relative",
        "display": "inline-block",
        "vertical-align": "middle"
    })
    
    generator.add_rule(".btn-group > .btn", {
        "position": "relative",
        "float": "left"
    })
    
    generator.add_rule(".btn-group > .btn:not(:first-child)", {
        "margin-left": "-1px",
        "border-top-left-radius": "0",
        "border-bottom-left-radius": "0"
    })
    
    generator.add_rule(".btn-group > .btn:not(:last-child)", {
        "border-top-right-radius": "0",
        "border-bottom-right-radius": "0"
    })
    
    # Link button
    generator.add_rule(".btn-link", {
        "font-weight": "400",
        "color": "#007bff",
        "background-color": "transparent",
        "border-color": "transparent"
    })
    
    generator.add_rule(".btn-link:hover", {
        "color": "#0056b3",
        "text-decoration": "underline",
        "background-color": "transparent",
        "border-color": "transparent"
    })
