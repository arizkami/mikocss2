"""
List Utilities for Legacy Browsers
"""

def generate_list_utilities(generator):
    """Generate comprehensive list utilities"""
    
    # List reset
    generator.add_rule(".list-none", {
        "list-style": "none",
        "padding": "0",
        "margin": "0"
    })
    
    generator.add_rule(".list-disc", {"list-style-type": "disc"})
    generator.add_rule(".list-decimal", {"list-style-type": "decimal"})
    generator.add_rule(".list-circle", {"list-style-type": "circle"})
    generator.add_rule(".list-square", {"list-style-type": "square"})
    generator.add_rule(".list-roman", {"list-style-type": "upper-roman"})
    generator.add_rule(".list-alpha", {"list-style-type": "lower-alpha"})
    
    # List position
    generator.add_rule(".list-inside", {"list-style-position": "inside"})
    generator.add_rule(".list-outside", {"list-style-position": "outside"})
    
    # Inline list
    generator.add_rule(".list-inline", {
        "padding-left": "0",
        "list-style": "none"
    })
    
    generator.add_rule(".list-inline > li", {
        "display": "inline-block",
        "padding-right": "8px",
        "padding-left": "8px"
    })
    
    # Unstyled list
    generator.add_rule(".list-unstyled", {
        "padding-left": "0",
        "list-style": "none"
    })
    
    # Description list
    generator.add_rule(".dl-horizontal dt", {
        "float": "left",
        "width": "160px",
        "clear": "left",
        "text-align": "right",
        "overflow": "hidden",
        "text-overflow": "ellipsis",
        "white-space": "nowrap"
    })
    
    generator.add_rule(".dl-horizontal dd", {
        "margin-left": "180px"
    })
    
    # List group
    generator.add_rule(".list-group", {
        "display": "-webkit-box",
        "display": "-ms-flexbox",
        "display": "flex",
        "-webkit-box-orient": "vertical",
        "-webkit-box-direction": "normal",
        "-ms-flex-direction": "column",
        "flex-direction": "column",
        "padding-left": "0",
        "margin-bottom": "0"
    })
    
    generator.add_rule(".list-group-item", {
        "position": "relative",
        "display": "block",
        "padding": "12px 16px",
        "margin-bottom": "-1px",
        "background-color": "#fff",
        "border": "1px solid rgba(0, 0, 0, 0.125)"
    })
    
    generator.add_rule(".list-group-item:first-child", {
        "border-top-left-radius": "4px",
        "border-top-right-radius": "4px"
    })
    
    generator.add_rule(".list-group-item:last-child", {
        "margin-bottom": "0",
        "border-bottom-right-radius": "4px",
        "border-bottom-left-radius": "4px"
    })
    
    generator.add_rule(".list-group-item:hover", {
        "background-color": "#f8f9fa",
        "cursor": "pointer"
    })
    
    generator.add_rule(".list-group-item.active", {
        "z-index": "2",
        "color": "#fff",
        "background-color": "#007bff",
        "border-color": "#007bff"
    })
    
    # List spacing
    generator.add_rule(".list-spaced > li", {"margin-bottom": "8px"})
    generator.add_rule(".list-spaced-lg > li", {"margin-bottom": "16px"})
