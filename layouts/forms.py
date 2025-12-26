"""
Form Utilities for Legacy Browsers
"""

def generate_form_utilities(generator):
    """Generate comprehensive form utilities"""
    
    # Form groups
    generator.add_rule(".form-group", {"margin-bottom": "16px"})
    
    # Form controls
    generator.add_rule(".form-control", {
        "display": "block",
        "width": "100%",
        "padding": "8px 12px",
        "font-size": "14px",
        "line-height": "1.5",
        "color": "#333",
        "background-color": "#fff",
        "border": "1px solid #ccc",
        "border-radius": "4px",
        "box-sizing": "border-box"
    })
    
    generator.add_rule(".form-control:focus", {
        "border-color": "#66afe9",
        "outline": "0",
        "box-shadow": "0 0 8px rgba(102, 175, 233, 0.6)"
    })
    
    generator.add_rule(".form-control:disabled", {
        "background-color": "#e9ecef",
        "opacity": "1",
        "cursor": "not-allowed"
    })
    
    # Input sizes
    generator.add_rule(".form-control-sm", {
        "padding": "4px 8px",
        "font-size": "12px",
        "border-radius": "3px"
    })
    
    generator.add_rule(".form-control-lg", {
        "padding": "12px 16px",
        "font-size": "18px",
        "border-radius": "6px"
    })
    
    # Labels
    generator.add_rule(".form-label", {
        "display": "inline-block",
        "margin-bottom": "4px",
        "font-weight": "600"
    })
    
    # Checkboxes and radios
    generator.add_rule(".form-check", {
        "position": "relative",
        "display": "block",
        "padding-left": "24px",
        "margin-bottom": "8px"
    })
    
    generator.add_rule(".form-check-input", {
        "position": "absolute",
        "margin-top": "4px",
        "margin-left": "-24px"
    })
    
    generator.add_rule(".form-check-label", {
        "margin-bottom": "0",
        "cursor": "pointer"
    })
    
    # Inline forms
    generator.add_rule(".form-inline", {
        "display": "-webkit-box",
        "display": "-ms-flexbox",
        "display": "flex",
        "-webkit-box-align": "center",
        "-ms-flex-align": "center",
        "align-items": "center"
    })
    
    generator.add_rule(".form-inline .form-control", {
        "display": "inline-block",
        "width": "auto",
        "vertical-align": "middle"
    })
    
    # Select
    generator.add_rule(".form-select", {
        "display": "block",
        "width": "100%",
        "padding": "8px 32px 8px 12px",
        "font-size": "14px",
        "line-height": "1.5",
        "color": "#333",
        "background-color": "#fff",
        "border": "1px solid #ccc",
        "border-radius": "4px",
        "appearance": "none"
    })
    
    # Textarea
    generator.add_rule(".form-textarea", {
        "resize": "vertical",
        "min-height": "80px"
    })
    
    # Form validation states
    generator.add_rule(".form-control.is-valid", {
        "border-color": "#28a745",
        "padding-right": "32px"
    })
    
    generator.add_rule(".form-control.is-invalid", {
        "border-color": "#dc3545",
        "padding-right": "32px"
    })
    
    generator.add_rule(".valid-feedback", {
        "display": "none",
        "margin-top": "4px",
        "font-size": "12px",
        "color": "#28a745"
    })
    
    generator.add_rule(".invalid-feedback", {
        "display": "none",
        "margin-top": "4px",
        "font-size": "12px",
        "color": "#dc3545"
    })
    
    generator.add_rule(".form-control.is-valid ~ .valid-feedback", {"display": "block"})
    generator.add_rule(".form-control.is-invalid ~ .invalid-feedback", {"display": "block"})
    
    # Input groups
    generator.add_rule(".input-group", {
        "position": "relative",
        "display": "-webkit-box",
        "display": "-ms-flexbox",
        "display": "flex",
        "-webkit-box-align": "stretch",
        "-ms-flex-align": "stretch",
        "align-items": "stretch",
        "width": "100%"
    })
    
    generator.add_rule(".input-group-text", {
        "display": "-webkit-box",
        "display": "-ms-flexbox",
        "display": "flex",
        "-webkit-box-align": "center",
        "-ms-flex-align": "center",
        "align-items": "center",
        "padding": "8px 12px",
        "font-size": "14px",
        "font-weight": "400",
        "line-height": "1.5",
        "color": "#495057",
        "text-align": "center",
        "white-space": "nowrap",
        "background-color": "#e9ecef",
        "border": "1px solid #ced4da",
        "border-radius": "4px"
    })
    
    # Fieldset
    generator.add_rule(".fieldset", {
        "min-width": "0",
        "padding": "0",
        "margin": "0",
        "border": "0"
    })
    
    generator.add_rule(".legend", {
        "display": "block",
        "width": "100%",
        "padding": "0",
        "margin-bottom": "8px",
        "font-size": "18px",
        "line-height": "inherit",
        "color": "inherit",
        "white-space": "normal"
    })
