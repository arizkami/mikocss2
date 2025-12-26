"""
Image Utilities for Legacy Browsers
"""

def generate_image_utilities(generator):
    """Generate comprehensive image utilities"""
    
    # Image display
    generator.add_rule(".img-responsive", {
        "max-width": "100%",
        "height": "auto",
        "display": "block",
        "-ms-interpolation-mode": "bicubic"  # IE7-8 smooth scaling
    })
    
    generator.add_rule(".img-fluid", {
        "max-width": "100%",
        "height": "auto",
        "-ms-interpolation-mode": "bicubic"
    })
    
    # Image shapes
    generator.add_rule(".img-rounded", {"border-radius": "6px"})
    generator.add_rule(".img-circle", {"border-radius": "50%"})
    generator.add_rule(".img-thumbnail", {
        "padding": "4px",
        "background-color": "#fff",
        "border": "1px solid #ddd",
        "border-radius": "4px",
        "max-width": "100%",
        "height": "auto"
    })
    
    # Image sizing
    generator.add_rule(".img-cover", {
        "object-fit": "cover",
        "width": "100%",
        "height": "100%"
    })
    generator.add_rule(".img-contain", {
        "object-fit": "contain",
        "width": "100%",
        "height": "100%"
    })
    
    # Image alignment
    generator.add_rule(".img-left", {"float": "left", "margin-right": "16px", "margin-bottom": "8px"})
    generator.add_rule(".img-right", {"float": "right", "margin-left": "16px", "margin-bottom": "8px"})
    generator.add_rule(".img-center", {"display": "block", "margin-left": "auto", "margin-right": "auto"})
    
    # Image filters (with IE fallbacks)
    generator.add_rule(".img-grayscale", {
        "filter": "grayscale(100%)",
        "-webkit-filter": "grayscale(100%)",
        "-moz-filter": "grayscale(100%)",
        "-ms-filter": "grayscale(100%)"
    })
    
    generator.add_rule(".img-sepia", {
        "filter": "sepia(100%)",
        "-webkit-filter": "sepia(100%)",
        "-moz-filter": "sepia(100%)"
    })
    
    generator.add_rule(".img-blur", {
        "filter": "blur(5px)",
        "-webkit-filter": "blur(5px)",
        "-moz-filter": "blur(5px)"
    })
    
    # Image aspect ratios
    generator.add_rule(".aspect-square", {"aspect-ratio": "1 / 1"})
    generator.add_rule(".aspect-video", {"aspect-ratio": "16 / 9"})
    generator.add_rule(".aspect-4-3", {"aspect-ratio": "4 / 3"})
    
    # Legacy aspect ratio (for old browsers)
    generator.add_rule(".aspect-ratio-box", {
        "position": "relative",
        "width": "100%",
        "height": "0",
        "overflow": "hidden"
    })
    generator.add_rule(".aspect-ratio-box-16-9", {"padding-bottom": "56.25%"})
    generator.add_rule(".aspect-ratio-box-4-3", {"padding-bottom": "75%"})
    generator.add_rule(".aspect-ratio-box-1-1", {"padding-bottom": "100%"})
    generator.add_rule(".aspect-ratio-box > img", {
        "position": "absolute",
        "top": "0",
        "left": "0",
        "width": "100%",
        "height": "100%"
    })
