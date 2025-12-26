"""
Color Utilities Generator
"""

def generate_color_utilities(generator, colors_map):
    """Generate background, text, and border color utilities"""
    for name, hex_code in colors_map.items():
        generator.add_rule(f".bg-{name}", {"background-color": hex_code})
        generator.add_rule(f".text-{name}", {"color": hex_code})
        generator.add_rule(f".border-{name}", {"border-color": hex_code})
    
    # Add dark mode color overrides for common colors
    # These work with both auto (prefers-color-scheme) and manual (.dark-mode class)
    
    # Black becomes white in dark mode
    generator.add_rule(".dark\\:bg-white", {"background-color": "#ffffff"}, "(prefers-color-scheme: dark)")
    generator.add_rule(".dark-mode .dark\\:bg-white", {"background-color": "#ffffff"})
    
    generator.add_rule(".dark\\:bg-black", {"background-color": "#000000"}, "(prefers-color-scheme: dark)")
    generator.add_rule(".dark-mode .dark\\:bg-black", {"background-color": "#000000"})
    
    generator.add_rule(".dark\\:text-white", {"color": "#ffffff"}, "(prefers-color-scheme: dark)")
    generator.add_rule(".dark-mode .dark\\:text-white", {"color": "#ffffff"})
    
    generator.add_rule(".dark\\:text-black", {"color": "#000000"}, "(prefers-color-scheme: dark)")
    generator.add_rule(".dark-mode .dark\\:text-black", {"color": "#000000"})
    
    # Light mode overrides
    generator.add_rule(".light\\:bg-white", {"background-color": "#ffffff"}, "(prefers-color-scheme: light)")
    generator.add_rule(".light-mode .light\\:bg-white", {"background-color": "#ffffff"})
    
    generator.add_rule(".light\\:bg-black", {"background-color": "#000000"}, "(prefers-color-scheme: light)")
    generator.add_rule(".light-mode .light\\:bg-black", {"background-color": "#000000"})
    
    generator.add_rule(".light\\:text-white", {"color": "#ffffff"}, "(prefers-color-scheme: light)")
    generator.add_rule(".light-mode .light\\:text-white", {"color": "#ffffff"})
    
    generator.add_rule(".light\\:text-black", {"color": "#000000"}, "(prefers-color-scheme: light)")
    generator.add_rule(".light-mode .light\\:text-black", {"color": "#000000"})
