"""
MikoCSS System Generator - Main Entry Point
IE6-11, Servo, Chrome 1+, Firefox 1+ Compatible
"""
import json
import sys
from pathlib import Path

# Import core modules
from core.css_generator import CSSGenerator
from core.color_engine import ColorEngine

# Import layout modules
from layouts.reset import generate_reset
from layouts import utilities, effects, responsive, colors
from layouts import forms, buttons, lists, images, tables, legacy, grid
from layouts import color_scheme, animations, chrome44_polyfill


def load_config(config_path="variable.json"):
    """Load configuration from JSON file"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Config file '{config_path}' not found!")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in config file: {e}")
        sys.exit(1)


def generate_css(config, output_file="cogeden.css"):
    """Generate complete CSS system"""
    print("=" * 60)
    print("  Cogeden Full CSS System Generator")
    print("  IE6-11, Servo, Chrome 1+, Firefox 1+ Compatible")
    print("=" * 60)
    
    # Initialize generators
    generator = CSSGenerator()
    color_engine = ColorEngine(config.get("colors", {}).get("palette"))
    
    # Generate color palette
    colors_map = color_engine.generate_palette()
    
    # Build CSS content
    print("\n📝 Generating CSS utilities...")
    
    # 1. Reset
    generator.css_content.append(generate_reset())
    
    # 2. Layout utilities
    utilities.generate_spacing(generator, config["spacing"])
    utilities.generate_display(generator)
    utilities.generate_float(generator)
    utilities.generate_flexbox(generator)
    utilities.generate_position(generator, config["spacing"])
    utilities.generate_typography(generator, config["font_sizes"])
    utilities.generate_sizing(generator, config["widths"])
    utilities.generate_borders(generator)
    utilities.generate_overflow(generator)
    utilities.generate_zindex(generator)
    utilities.generate_opacity(generator)
    utilities.generate_cursor(generator)
    utilities.generate_user_select(generator)
    utilities.generate_pointer_events(generator)
    
    # 2b. Grid system
    grid.generate_grid_utilities(generator)
    
    # 2c. Component utilities
    buttons.generate_button_utilities(generator)
    forms.generate_form_utilities(generator)
    lists.generate_list_utilities(generator)
    images.generate_image_utilities(generator)
    tables.generate_table_utilities(generator)
    
    # 2d. Legacy browser utilities
    legacy.generate_legacy_utilities(generator)
    
    # 3. Effects
    effects.generate_shadows(generator)
    effects.generate_transitions(generator)
    effects.generate_transforms(generator)
    
    # 3b. Animations
    animations.generate_keyframes(generator)
    animations.generate_animation_utilities(generator)
    
    # 3c. Color scheme system
    color_scheme.generate_color_scheme_system(generator)
    
    # 3d. Chrome 44 and old browser fixes
    chrome44_polyfill.generate_chrome44_fixes(generator)
    
    # 4. Responsive
    responsive.generate_responsive(
        generator, 
        config["breakpoints"],
        config["spacing"],
        config["font_sizes"],
        config["widths"]
    )
    
    # 5. Colors
    colors.generate_color_utilities(generator, colors_map)
    
    # Save CSS file
    print("\n💾 Saving CSS file...")
    with open(output_file, "w") as f:
        f.write(generator.get_css())
    
    # Statistics
    css_content = generator.get_css()
    total_lines = len(css_content.splitlines())
    
    print(f"✅ Created {output_file} successfully.")
    print(f"   - Total Colors: {len(colors_map)}")
    print(f"   - Total CSS Lines: {total_lines}")
    
    print("\n" + "=" * 60)
    print("✨ Generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    # Load configuration
    config = load_config("variable.json")
    
    # Generate CSS
    output_file = sys.argv[1] if len(sys.argv) > 1 else "cogeden.css"
    generate_css(config, output_file)
