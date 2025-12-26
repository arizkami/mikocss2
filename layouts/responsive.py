"""
Responsive Utilities - Super Responsive System
xs (480px), sm (640px), md (768px), lg (1024px), xl (1280px), 2xl (1536px)
"""

def generate_responsive(generator, breakpoints, spacing, font_sizes, widths):
    """Generate comprehensive responsive breakpoint utilities"""
    for bp_name, bp_size in breakpoints.items():
        media = f"(min-width: {bp_size})"
        
        # Display utilities
        generator.add_rule(f".{bp_name}\\:block", {"display": "block"}, media)
        generator.add_rule(f".{bp_name}\\:inline", {"display": "inline"}, media)
        generator.add_rule(f".{bp_name}\\:inline-block", {"display": "inline-block"}, media)
        generator.add_rule(f".{bp_name}\\:flex", {"display": "flex"}, media)
        generator.add_rule(f".{bp_name}\\:inline-flex", {"display": "inline-flex"}, media)
        generator.add_rule(f".{bp_name}\\:hidden", {"display": "none"}, media)
        generator.add_rule(f".{bp_name}\\:invisible", {"visibility": "hidden"}, media)
        generator.add_rule(f".{bp_name}\\:visible", {"visibility": "visible"}, media)
        
        # Flexbox utilities
        generator.add_rule(f".{bp_name}\\:flex-row", {"flex-direction": "row"}, media)
        generator.add_rule(f".{bp_name}\\:flex-col", {"flex-direction": "column"}, media)
        generator.add_rule(f".{bp_name}\\:flex-wrap", {"flex-wrap": "wrap"}, media)
        generator.add_rule(f".{bp_name}\\:flex-nowrap", {"flex-wrap": "nowrap"}, media)
        
        generator.add_rule(f".{bp_name}\\:items-start", {"align-items": "flex-start"}, media)
        generator.add_rule(f".{bp_name}\\:items-center", {"align-items": "center"}, media)
        generator.add_rule(f".{bp_name}\\:items-end", {"align-items": "flex-end"}, media)
        generator.add_rule(f".{bp_name}\\:items-stretch", {"align-items": "stretch"}, media)
        
        generator.add_rule(f".{bp_name}\\:justify-start", {"justify-content": "flex-start"}, media)
        generator.add_rule(f".{bp_name}\\:justify-center", {"justify-content": "center"}, media)
        generator.add_rule(f".{bp_name}\\:justify-end", {"justify-content": "flex-end"}, media)
        generator.add_rule(f".{bp_name}\\:justify-between", {"justify-content": "space-between"}, media)
        generator.add_rule(f".{bp_name}\\:justify-around", {"justify-content": "space-around"}, media)
        
        generator.add_rule(f".{bp_name}\\:flex-1", {"flex": "1 1 0%"}, media)
        generator.add_rule(f".{bp_name}\\:flex-auto", {"flex": "1 1 auto"}, media)
        generator.add_rule(f".{bp_name}\\:flex-none", {"flex": "none"}, media)
        
        # Float utilities
        generator.add_rule(f".{bp_name}\\:float-left", {"float": "left"}, media)
        generator.add_rule(f".{bp_name}\\:float-right", {"float": "right"}, media)
        generator.add_rule(f".{bp_name}\\:float-none", {"float": "none"}, media)
        
        # Position utilities
        generator.add_rule(f".{bp_name}\\:static", {"position": "static"}, media)
        generator.add_rule(f".{bp_name}\\:relative", {"position": "relative"}, media)
        generator.add_rule(f".{bp_name}\\:absolute", {"position": "absolute"}, media)
        generator.add_rule(f".{bp_name}\\:fixed", {"position": "fixed"}, media)
        generator.add_rule(f".{bp_name}\\:sticky", {"position": "sticky"}, media)
        
        # Text alignment
        generator.add_rule(f".{bp_name}\\:text-left", {"text-align": "left"}, media)
        generator.add_rule(f".{bp_name}\\:text-center", {"text-align": "center"}, media)
        generator.add_rule(f".{bp_name}\\:text-right", {"text-align": "right"}, media)
        generator.add_rule(f".{bp_name}\\:text-justify", {"text-align": "justify"}, media)
        
        # Font sizes
        for name, size in font_sizes.items():
            generator.add_rule(f".{bp_name}\\:text-{name}", {"font-size": size}, media)
        
        # Font weights
        generator.add_rule(f".{bp_name}\\:font-thin", {"font-weight": "100"}, media)
        generator.add_rule(f".{bp_name}\\:font-light", {"font-weight": "300"}, media)
        generator.add_rule(f".{bp_name}\\:font-normal", {"font-weight": "400"}, media)
        generator.add_rule(f".{bp_name}\\:font-medium", {"font-weight": "500"}, media)
        generator.add_rule(f".{bp_name}\\:font-semibold", {"font-weight": "600"}, media)
        generator.add_rule(f".{bp_name}\\:font-bold", {"font-weight": "700"}, media)
        generator.add_rule(f".{bp_name}\\:font-black", {"font-weight": "900"}, media)
        
        # Spacing - Margin
        for name, size in spacing.items():
            generator.add_rule(f".{bp_name}\\:m-{name}", {"margin": size}, media)
            generator.add_rule(f".{bp_name}\\:mt-{name}", {"margin-top": size}, media)
            generator.add_rule(f".{bp_name}\\:mb-{name}", {"margin-bottom": size}, media)
            generator.add_rule(f".{bp_name}\\:ml-{name}", {"margin-left": size}, media)
            generator.add_rule(f".{bp_name}\\:mr-{name}", {"margin-right": size}, media)
            generator.add_rule(f".{bp_name}\\:mx-{name}", {"margin-left": size, "margin-right": size}, media)
            generator.add_rule(f".{bp_name}\\:my-{name}", {"margin-top": size, "margin-bottom": size}, media)
        
        # Spacing - Padding
        for name, size in spacing.items():
            generator.add_rule(f".{bp_name}\\:p-{name}", {"padding": size}, media)
            generator.add_rule(f".{bp_name}\\:pt-{name}", {"padding-top": size}, media)
            generator.add_rule(f".{bp_name}\\:pb-{name}", {"padding-bottom": size}, media)
            generator.add_rule(f".{bp_name}\\:pl-{name}", {"padding-left": size}, media)
            generator.add_rule(f".{bp_name}\\:pr-{name}", {"padding-right": size}, media)
            generator.add_rule(f".{bp_name}\\:px-{name}", {"padding-left": size, "padding-right": size}, media)
            generator.add_rule(f".{bp_name}\\:py-{name}", {"padding-top": size, "padding-bottom": size}, media)
        
        # Width utilities
        for name, val in widths.items():
            generator.add_rule(f".{bp_name}\\:w-{name}", {"width": val}, media)
            generator.add_rule(f".{bp_name}\\:h-{name}", {"height": val}, media)
        
        # Specific width/height values
        for i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64]:
            generator.add_rule(f".{bp_name}\\:w-{i}", {"width": f"{i*4}px"}, media)
            generator.add_rule(f".{bp_name}\\:h-{i}", {"height": f"{i*4}px"}, media)
        
        generator.add_rule(f".{bp_name}\\:max-w-full", {"max-width": "100%"}, media)
        generator.add_rule(f".{bp_name}\\:max-h-full", {"max-height": "100%"}, media)
        
        # Overflow
        generator.add_rule(f".{bp_name}\\:overflow-auto", {"overflow": "auto"}, media)
        generator.add_rule(f".{bp_name}\\:overflow-hidden", {"overflow": "hidden"}, media)
        generator.add_rule(f".{bp_name}\\:overflow-visible", {"overflow": "visible"}, media)
        generator.add_rule(f".{bp_name}\\:overflow-scroll", {"overflow": "scroll"}, media)
        
        # Opacity
        for i in [0, 25, 50, 75, 100]:
            generator.add_rule(f".{bp_name}\\:opacity-{i}", {"opacity": str(i/100)}, media)
        
        # Z-index
        for z in [0, 10, 20, 30, 40, 50]:
            generator.add_rule(f".{bp_name}\\:z-{z}", {"z-index": str(z)}, media)
        
        # Cursor
        generator.add_rule(f".{bp_name}\\:cursor-pointer", {"cursor": "pointer"}, media)
        generator.add_rule(f".{bp_name}\\:cursor-not-allowed", {"cursor": "not-allowed"}, media)
        
        # Border radius
        generator.add_rule(f".{bp_name}\\:rounded-none", {"border-radius": "0"}, media)
        generator.add_rule(f".{bp_name}\\:rounded", {"border-radius": "4px"}, media)
        generator.add_rule(f".{bp_name}\\:rounded-lg", {"border-radius": "8px"}, media)
        generator.add_rule(f".{bp_name}\\:rounded-full", {"border-radius": "9999px"}, media)
