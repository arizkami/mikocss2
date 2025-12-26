"""
Table Utilities for Legacy Browsers
"""

def generate_table_utilities(generator):
    """Generate comprehensive table utilities"""
    
    # Table layout
    generator.add_rule(".table", {"display": "table", "width": "100%"})
    generator.add_rule(".table-auto", {"table-layout": "auto"})
    generator.add_rule(".table-fixed", {"table-layout": "fixed"})
    
    # Table borders
    generator.add_rule(".table-border-collapse", {"border-collapse": "collapse"})
    generator.add_rule(".table-border-separate", {"border-collapse": "separate"})
    
    # Table cell spacing
    generator.add_rule(".table-spacing-0", {"border-spacing": "0"})
    generator.add_rule(".table-spacing-1", {"border-spacing": "4px"})
    generator.add_rule(".table-spacing-2", {"border-spacing": "8px"})
    
    # Table row
    generator.add_rule(".table-row", {"display": "table-row"})
    generator.add_rule(".table-row-group", {"display": "table-row-group"})
    
    # Table cell
    generator.add_rule(".table-cell", {"display": "table-cell"})
    generator.add_rule(".table-header-group", {"display": "table-header-group"})
    generator.add_rule(".table-footer-group", {"display": "table-footer-group"})
    
    # Vertical alignment for cells
    generator.add_rule(".align-baseline", {"vertical-align": "baseline"})
    generator.add_rule(".align-top", {"vertical-align": "top"})
    generator.add_rule(".align-middle", {"vertical-align": "middle"})
    generator.add_rule(".align-bottom", {"vertical-align": "bottom"})
    generator.add_rule(".align-text-top", {"vertical-align": "text-top"})
    generator.add_rule(".align-text-bottom", {"vertical-align": "text-bottom"})
    
    # Table striped rows
    generator.add_rule(".table-striped tbody tr:nth-child(odd)", {"background-color": "#f9f9f9"})
    generator.add_rule(".table-striped tbody tr:nth-child(even)", {"background-color": "#ffffff"})
    
    # Table hover effect
    generator.add_rule(".table-hover tbody tr:hover", {
        "background-color": "#f5f5f5",
        "cursor": "pointer"
    })
    
    # Table bordered
    generator.add_rule(".table-bordered", {"border": "1px solid #ddd"})
    generator.add_rule(".table-bordered th", {"border": "1px solid #ddd", "padding": "8px"})
    generator.add_rule(".table-bordered td", {"border": "1px solid #ddd", "padding": "8px"})
    
    # Table responsive wrapper
    generator.add_rule(".table-responsive", {
        "overflow-x": "auto",
        "-webkit-overflow-scrolling": "touch",
        "width": "100%"
    })
    
    # Table compact
    generator.add_rule(".table-compact th", {"padding": "4px"})
    generator.add_rule(".table-compact td", {"padding": "4px"})
    
    # Table spacious
    generator.add_rule(".table-spacious th", {"padding": "12px"})
    generator.add_rule(".table-spacious td", {"padding": "12px"})
