"""
Color Utilities Generator
"""

def generate_color_utilities(generator, colors_map):
    """Generate background, text, and border color utilities"""
    for name, hex_code in colors_map.items():
        generator.add_rule(f".bg-{name}", {"background-color": hex_code})
        generator.add_rule(f".text-{name}", {"color": hex_code})
        generator.add_rule(f".border-{name}", {"border-color": hex_code})
