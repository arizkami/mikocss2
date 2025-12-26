"""
Grid System for Legacy Browsers
Float-based grid with flexbox fallback
"""

def generate_grid_utilities(generator):
    """Generate comprehensive grid system"""
    
    # Container
    generator.add_rule(".container", {
        "width": "100%",
        "padding-right": "15px",
        "padding-left": "15px",
        "margin-right": "auto",
        "margin-left": "auto"
    })
    
    generator.add_rule(".container-fluid", {
        "width": "100%",
        "padding-right": "15px",
        "padding-left": "15px",
        "margin-right": "auto",
        "margin-left": "auto"
    })
    
    # Row
    generator.add_rule(".row", {
        "display": "-webkit-box",
        "display": "-ms-flexbox",
        "display": "flex",
        "-ms-flex-wrap": "wrap",
        "flex-wrap": "wrap",
        "margin-right": "-15px",
        "margin-left": "-15px"
    })
    
    # Legacy row (float-based for IE9-)
    generator.add_rule(".row-legacy", {
        "margin-right": "-15px",
        "margin-left": "-15px",
        "*zoom": "1"
    })
    
    generator.add_rule(".row-legacy:before", {"content": "\" \"", "display": "table"})
    generator.add_rule(".row-legacy:after", {"content": "\" \"", "display": "table", "clear": "both"})
    
    # Column base
    generator.add_rule("[class*='col-']", {
        "position": "relative",
        "width": "100%",
        "padding-right": "15px",
        "padding-left": "15px"
    })
    
    # Generate columns (1-12)
    for i in range(1, 13):
        width = f"{(i / 12) * 100}%"
        
        # Flexbox columns
        generator.add_rule(f".col-{i}", {
            "-webkit-box-flex": "0",
            "-ms-flex": f"0 0 {width}",
            "flex": f"0 0 {width}",
            "max-width": width
        })
        
        # Float-based columns (IE9- fallback)
        generator.add_rule(f".col-legacy-{i}", {
            "float": "left",
            "width": width,
            "*display": "inline",  # IE6/7
            "*zoom": "1"
        })
    
    # Auto column
    generator.add_rule(".col-auto", {
        "-webkit-box-flex": "0",
        "-ms-flex": "0 0 auto",
        "flex": "0 0 auto",
        "width": "auto",
        "max-width": "100%"
    })
    
    # Column offsets
    for i in range(0, 12):
        if i > 0:
            offset = f"{(i / 12) * 100}%"
            generator.add_rule(f".offset-{i}", {"margin-left": offset})
    
    # Column ordering
    for i in range(1, 13):
        generator.add_rule(f".order-{i}", {"-webkit-box-ordinal-group": str(i+1), "-ms-flex-order": str(i), "order": str(i)})
    
    generator.add_rule(".order-first", {"-webkit-box-ordinal-group": "0", "-ms-flex-order": "-1", "order": "-1"})
    generator.add_rule(".order-last", {"-webkit-box-ordinal-group": "14", "-ms-flex-order": "13", "order": "13"})
    
    # No gutters
    generator.add_rule(".no-gutters", {"margin-right": "0", "margin-left": "0"})
    generator.add_rule(".no-gutters > [class*='col-']", {"padding-right": "0", "padding-left": "0"})
    
    # Align items
    generator.add_rule(".align-items-start", {
        "-webkit-box-align": "start",
        "-ms-flex-align": "start",
        "align-items": "flex-start"
    })
    
    generator.add_rule(".align-items-center", {
        "-webkit-box-align": "center",
        "-ms-flex-align": "center",
        "align-items": "center"
    })
    
    generator.add_rule(".align-items-end", {
        "-webkit-box-align": "end",
        "-ms-flex-align": "end",
        "align-items": "flex-end"
    })
    
    # Justify content
    generator.add_rule(".justify-content-start", {
        "-webkit-box-pack": "start",
        "-ms-flex-pack": "start",
        "justify-content": "flex-start"
    })
    
    generator.add_rule(".justify-content-center", {
        "-webkit-box-pack": "center",
        "-ms-flex-pack": "center",
        "justify-content": "center"
    })
    
    generator.add_rule(".justify-content-end", {
        "-webkit-box-pack": "end",
        "-ms-flex-pack": "end",
        "justify-content": "flex-end"
    })
    
    generator.add_rule(".justify-content-between", {
        "-webkit-box-pack": "justify",
        "-ms-flex-pack": "justify",
        "justify-content": "space-between"
    })
    
    generator.add_rule(".justify-content-around", {
        "-ms-flex-pack": "distribute",
        "justify-content": "space-around"
    })
