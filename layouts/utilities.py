"""
Layout Utilities Generator
"""

def generate_spacing(generator, spacing):
    """Generate margin and padding utilities"""
    for name, size in spacing.items():
        # Margin
        generator.add_rule(f".m-{name}", {"margin": size})
        generator.add_rule(f".mt-{name}", {"margin-top": size})
        generator.add_rule(f".mb-{name}", {"margin-bottom": size})
        generator.add_rule(f".ml-{name}", {"margin-left": size})
        generator.add_rule(f".mr-{name}", {"margin-right": size})
        generator.add_rule(f".mx-{name}", {"margin-left": size, "margin-right": size})
        generator.add_rule(f".my-{name}", {"margin-top": size, "margin-bottom": size})
        # Padding
        generator.add_rule(f".p-{name}", {"padding": size})
        generator.add_rule(f".pt-{name}", {"padding-top": size})
        generator.add_rule(f".pb-{name}", {"padding-bottom": size})
        generator.add_rule(f".pl-{name}", {"padding-left": size})
        generator.add_rule(f".pr-{name}", {"padding-right": size})
        generator.add_rule(f".px-{name}", {"padding-left": size, "padding-right": size})
        generator.add_rule(f".py-{name}", {"padding-top": size, "padding-bottom": size})

def generate_display(generator):
    """Generate display utilities"""
    generator.add_rule(".block", {"display": "block"})
    generator.add_rule(".inline", {"display": "inline"})
    generator.add_rule(".inline-block", {"display": "inline-block"})
    generator.add_rule(".hidden", {"display": "none"})
    generator.add_rule(".invisible", {"visibility": "hidden"})
    generator.add_rule(".visible", {"visibility": "visible"})

def generate_float(generator):
    """Generate float utilities"""
    generator.add_rule(".float-left", {"float": "left"})
    generator.add_rule(".float-right", {"float": "right"})
    generator.add_rule(".float-none", {"float": "none"})
    generator.add_rule(".clearfix:after", {"content": "\" \"", "display": "table", "clear": "both"})
    generator.add_rule(".clearfix", {"*zoom": "1"})
    generator.add_rule(".clear-both", {"clear": "both"})
    generator.add_rule(".clear-left", {"clear": "left"})
    generator.add_rule(".clear-right", {"clear": "right"})

def generate_flexbox(generator):
    """Generate flexbox utilities"""
    generator.add_rule(".flex", {"display": "flex"})
    generator.add_rule(".inline-flex", {"display": "inline-flex"})
    generator.add_rule(".flex-row", {"flex-direction": "row"})
    generator.add_rule(".flex-col", {"flex-direction": "column"})
    generator.add_rule(".flex-wrap", {"flex-wrap": "wrap"})
    generator.add_rule(".flex-nowrap", {"flex-wrap": "nowrap"})
    
    generator.add_rule(".items-start", {"-webkit-box-align": "start", "-ms-flex-align": "start", "align-items": "flex-start"})
    generator.add_rule(".items-center", {"-webkit-box-align": "center", "-ms-flex-align": "center", "align-items": "center"})
    generator.add_rule(".items-end", {"-webkit-box-align": "end", "-ms-flex-align": "end", "align-items": "flex-end"})
    generator.add_rule(".items-stretch", {"-webkit-box-align": "stretch", "-ms-flex-align": "stretch", "align-items": "stretch"})
    
    generator.add_rule(".justify-start", {"-webkit-box-pack": "start", "-ms-flex-pack": "start", "justify-content": "flex-start"})
    generator.add_rule(".justify-center", {"-webkit-box-pack": "center", "-ms-flex-pack": "center", "justify-content": "center"})
    generator.add_rule(".justify-end", {"-webkit-box-pack": "end", "-ms-flex-pack": "end", "justify-content": "flex-end"})
    generator.add_rule(".justify-between", {"-webkit-box-pack": "justify", "-ms-flex-pack": "justify", "justify-content": "space-between"})
    generator.add_rule(".justify-around", {"-ms-flex-pack": "distribute", "justify-content": "space-around"})
    
    generator.add_rule(".flex-1", {"flex": "1 1 0%"})
    generator.add_rule(".flex-auto", {"flex": "1 1 auto"})
    generator.add_rule(".flex-none", {"flex": "none"})

def generate_position(generator, spacing):
    """Generate position utilities"""
    generator.add_rule(".static", {"position": "static"})
    generator.add_rule(".relative", {"position": "relative"})
    generator.add_rule(".absolute", {"position": "absolute"})
    generator.add_rule(".fixed", {"position": "fixed"})
    generator.add_rule(".sticky", {"position": "-webkit-sticky", "position": "sticky"})
    
    for pos in ["0", "1", "2", "4", "8"]:
        val = spacing[pos]
        generator.add_rule(f".top-{pos}", {"top": val})
        generator.add_rule(f".right-{pos}", {"right": val})
        generator.add_rule(f".bottom-{pos}", {"bottom": val})
        generator.add_rule(f".left-{pos}", {"left": val})
    
    generator.add_rule(".inset-0", {"top": "0", "right": "0", "bottom": "0", "left": "0"})

def generate_typography(generator, font_sizes):
    """Generate typography utilities"""
    for name, size in font_sizes.items():
        generator.add_rule(f".text-{name}", {"font-size": size})
    
    generator.add_rule(".font-thin", {"font-weight": "100"})
    generator.add_rule(".font-light", {"font-weight": "300"})
    generator.add_rule(".font-normal", {"font-weight": "400"})
    generator.add_rule(".font-medium", {"font-weight": "500"})
    generator.add_rule(".font-semibold", {"font-weight": "600"})
    generator.add_rule(".font-bold", {"font-weight": "700"})
    generator.add_rule(".font-black", {"font-weight": "900"})
    
    generator.add_rule(".text-left", {"text-align": "left"})
    generator.add_rule(".text-center", {"text-align": "center"})
    generator.add_rule(".text-right", {"text-align": "right"})
    generator.add_rule(".text-justify", {"text-align": "justify"})
    
    generator.add_rule(".italic", {"font-style": "italic"})
    generator.add_rule(".not-italic", {"font-style": "normal"})
    generator.add_rule(".uppercase", {"text-transform": "uppercase"})
    generator.add_rule(".lowercase", {"text-transform": "lowercase"})
    generator.add_rule(".capitalize", {"text-transform": "capitalize"})
    
    generator.add_rule(".underline", {"text-decoration": "underline"})
    generator.add_rule(".line-through", {"text-decoration": "line-through"})
    generator.add_rule(".no-underline", {"text-decoration": "none"})
    
    generator.add_rule(".truncate", {"overflow": "hidden", "text-overflow": "ellipsis", "white-space": "nowrap"})
    generator.add_rule(".break-words", {"word-wrap": "break-word", "overflow-wrap": "break-word"})
    generator.add_rule(".break-all", {"word-break": "break-all"})

def generate_sizing(generator, widths):
    """Generate sizing utilities"""
    for name, val in widths.items():
        generator.add_rule(f".w-{name}", {"width": val})
        generator.add_rule(f".h-{name}", {"height": val})
    
    for i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64]:
        generator.add_rule(f".w-{i}", {"width": f"{i*4}px"})
        generator.add_rule(f".h-{i}", {"height": f"{i*4}px"})
    
    generator.add_rule(".min-w-0", {"min-width": "0"})
    generator.add_rule(".min-h-0", {"min-height": "0"})
    generator.add_rule(".max-w-full", {"max-width": "100%"})
    generator.add_rule(".max-h-full", {"max-height": "100%"})

def generate_borders(generator):
    """Generate border utilities"""
    generator.add_rule(".border", {"border-style": "solid", "border-width": "1px"})
    generator.add_rule(".border-0", {"border-width": "0"})
    generator.add_rule(".border-2", {"border-width": "2px"})
    generator.add_rule(".border-4", {"border-width": "4px"})
    generator.add_rule(".border-t", {"border-top-style": "solid", "border-top-width": "1px"})
    generator.add_rule(".border-r", {"border-right-style": "solid", "border-right-width": "1px"})
    generator.add_rule(".border-b", {"border-bottom-style": "solid", "border-bottom-width": "1px"})
    generator.add_rule(".border-l", {"border-left-style": "solid", "border-left-width": "1px"})
    
    generator.add_rule(".rounded-none", {"border-radius": "0"})
    generator.add_rule(".rounded-sm", {"border-radius": "2px"})
    generator.add_rule(".rounded", {"border-radius": "4px"})
    generator.add_rule(".rounded-md", {"border-radius": "6px"})
    generator.add_rule(".rounded-lg", {"border-radius": "8px"})
    generator.add_rule(".rounded-xl", {"border-radius": "12px"})
    generator.add_rule(".rounded-2xl", {"border-radius": "16px"})
    generator.add_rule(".rounded-full", {"border-radius": "9999px"})

def generate_overflow(generator):
    """Generate overflow utilities"""
    generator.add_rule(".overflow-auto", {"overflow": "auto"})
    generator.add_rule(".overflow-hidden", {"overflow": "hidden"})
    generator.add_rule(".overflow-visible", {"overflow": "visible"})
    generator.add_rule(".overflow-scroll", {"overflow": "scroll"})
    generator.add_rule(".overflow-x-auto", {"overflow-x": "auto"})
    generator.add_rule(".overflow-y-auto", {"overflow-y": "auto"})

def generate_zindex(generator):
    """Generate z-index utilities"""
    for z in [0, 10, 20, 30, 40, 50]:
        generator.add_rule(f".z-{z}", {"z-index": str(z)})
    generator.add_rule(".z-auto", {"z-index": "auto"})

def generate_opacity(generator):
    """Generate opacity utilities"""
    for i in range(0, 11):
        opacity = i / 10
        generator.add_rule(f".opacity-{i*10}", {"opacity": str(opacity)})

def generate_cursor(generator):
    """Generate cursor utilities"""
    generator.add_rule(".cursor-auto", {"cursor": "auto"})
    generator.add_rule(".cursor-pointer", {"cursor": "pointer"})
    generator.add_rule(".cursor-not-allowed", {"cursor": "not-allowed"})
    generator.add_rule(".cursor-move", {"cursor": "move"})
    generator.add_rule(".cursor-text", {"cursor": "text"})

def generate_user_select(generator):
    """Generate user-select utilities"""
    generator.add_rule(".select-none", {"user-select": "none"})
    generator.add_rule(".select-text", {"user-select": "text"})
    generator.add_rule(".select-all", {"user-select": "all"})
    generator.add_rule(".select-auto", {"user-select": "auto"})

def generate_pointer_events(generator):
    """Generate pointer-events utilities"""
    generator.add_rule(".pointer-events-none", {"pointer-events": "none"})
    generator.add_rule(".pointer-events-auto", {"pointer-events": "auto"})
