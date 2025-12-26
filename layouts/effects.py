"""
Effects Utilities (Shadows, Transforms, Transitions)
"""

def generate_shadows(generator):
    """Generate box-shadow utilities"""
    generator.add_rule(".shadow-sm", {"box-shadow": "0 1px 2px 0 rgba(0, 0, 0, 0.05)"})
    generator.add_rule(".shadow", {"box-shadow": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)"})
    generator.add_rule(".shadow-md", {"box-shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"})
    generator.add_rule(".shadow-lg", {"box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"})
    generator.add_rule(".shadow-xl", {"box-shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"})
    generator.add_rule(".shadow-none", {"box-shadow": "none"})

def generate_transitions(generator):
    """Generate transition utilities"""
    generator.add_rule(".transition-none", {"transition": "none"})
    generator.add_rule(".transition-all", {"transition": "all 0.3s ease"})
    generator.add_rule(".transition-colors", {"transition": "color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease"})
    generator.add_rule(".transition-opacity", {"transition": "opacity 0.3s ease"})
    generator.add_rule(".transition-transform", {"transition": "transform 0.3s ease"})

def generate_transforms(generator):
    """Generate transform utilities"""
    # Scale
    generator.add_rule(".scale-0", {"transform": "scale(0)"})
    generator.add_rule(".scale-50", {"transform": "scale(0.5)"})
    generator.add_rule(".scale-75", {"transform": "scale(0.75)"})
    generator.add_rule(".scale-90", {"transform": "scale(0.9)"})
    generator.add_rule(".scale-95", {"transform": "scale(0.95)"})
    generator.add_rule(".scale-100", {"transform": "scale(1)"})
    generator.add_rule(".scale-105", {"transform": "scale(1.05)"})
    generator.add_rule(".scale-110", {"transform": "scale(1.1)"})
    generator.add_rule(".scale-125", {"transform": "scale(1.25)"})
    generator.add_rule(".scale-150", {"transform": "scale(1.5)"})
    
    # Rotate
    generator.add_rule(".rotate-0", {"transform": "rotate(0deg)"})
    generator.add_rule(".rotate-45", {"transform": "rotate(45deg)"})
    generator.add_rule(".rotate-90", {"transform": "rotate(90deg)"})
    generator.add_rule(".rotate-180", {"transform": "rotate(180deg)"})
    generator.add_rule(".-rotate-45", {"transform": "rotate(-45deg)"})
    generator.add_rule(".-rotate-90", {"transform": "rotate(-90deg)"})
    generator.add_rule(".-rotate-180", {"transform": "rotate(-180deg)"})
