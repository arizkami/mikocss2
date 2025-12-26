"""
Production Build System
Generates minified CSS, JS utilities, and production-ready files
"""
import sys
import os
import json
import gzip
import shutil
from pathlib import Path

# Import generators
from main import load_config, generate_css
from core.js_generator import JSGenerator


def minify_css(css_content):
    """Minify CSS content"""
    # Remove comments
    css_content = remove_comments(css_content)
    
    # Remove extra whitespace
    css_content = ' '.join(css_content.split())
    
    # Remove spaces around special characters
    css_content = css_content.replace(' {', '{')
    css_content = css_content.replace('{ ', '{')
    css_content = css_content.replace(' }', '}')
    css_content = css_content.replace('; ', ';')
    css_content = css_content.replace(': ', ':')
    css_content = css_content.replace(' >', '>')
    css_content = css_content.replace('> ', '>')
    
    return css_content


def remove_comments(content):
    """Remove CSS comments"""
    import re
    # Remove /* */ comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    return content


def gzip_file(input_file, output_file):
    """Create gzipped version of file"""
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def get_file_size(file_path):
    """Get file size in KB"""
    size = os.path.getsize(file_path)
    return round(size / 1024, 2)


def build_production(output_dir="dist"):
    """Build production-ready files"""
    print("=" * 60)
    print("  MikoCSS - Production Build")
    print("=" * 60)
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Load config
    config = load_config("variable.json")
    
    # 1. Generate full CSS
    print("\n📦 Step 1: Generating full CSS...")
    full_css_path = f"{output_dir}/cogeden.css"
    generate_css(config, full_css_path)
    full_size = get_file_size(full_css_path)
    print(f"   ✓ Full CSS: {full_size} KB")
    
    # 2. Generate minified CSS
    print("\n📦 Step 2: Minifying CSS...")
    with open(full_css_path, 'r') as f:
        css_content = f.read()
    
    minified_css = minify_css(css_content)
    min_css_path = f"{output_dir}/cogeden.min.css"
    
    with open(min_css_path, 'w') as f:
        f.write(minified_css)
    
    min_size = get_file_size(min_css_path)
    reduction = round((1 - min_size / full_size) * 100, 1)
    print(f"   ✓ Minified CSS: {min_size} KB ({reduction}% smaller)")
    
    # 3. Generate gzipped version
    print("\n📦 Step 3: Creating gzipped version...")
    gzip_path = f"{output_dir}/cogeden.min.css.gz"
    gzip_file(min_css_path, gzip_path)
    gzip_size = get_file_size(gzip_path)
    gzip_reduction = round((1 - gzip_size / full_size) * 100, 1)
    print(f"   ✓ Gzipped CSS: {gzip_size} KB ({gzip_reduction}% smaller)")
    
    # 4. Generate JavaScript utilities
    print("\n📦 Step 4: Generating JavaScript utilities...")
    js_gen = JSGenerator()
    
    # Utility functions
    utils_js = js_gen.generate_utility_functions()
    utils_path = f"{output_dir}/cogeden-utils.js"
    with open(utils_path, 'w') as f:
        f.write(utils_js)
    utils_size = get_file_size(utils_path)
    print(f"   ✓ Utility JS: {utils_size} KB")
    
    # Theme switcher
    from layouts.color_scheme import generate_theme_switcher_js
    theme_js = generate_theme_switcher_js()
    theme_path = f"{output_dir}/cogeden-theme.js"
    with open(theme_path, 'w', encoding='utf-8') as f:
        f.write(theme_js)
    theme_size = get_file_size(theme_path)
    print(f"   ✓ Theme Switcher: {theme_size} KB")
    
    # CSS Loader
    loader_js = js_gen.generate_minified_loader("cogeden.min.css")
    loader_path = f"{output_dir}/cogeden-loader.min.js"
    with open(loader_path, 'w') as f:
        f.write(loader_js)
    loader_size = get_file_size(loader_path)
    print(f"   ✓ CSS Loader: {loader_size} KB")
    
    # 5. Generate package.json
    print("\n📦 Step 5: Generating package.json...")
    package_json = js_gen.generate_build_config()
    package_path = f"{output_dir}/package.json"
    with open(package_path, 'w') as f:
        f.write(package_json)
    print(f"   ✓ Package config created")
    
    # 6. Generate build manifest
    print("\n📦 Step 6: Creating build manifest...")
    manifest = {
        "build_date": js_gen._get_timestamp(),
        "version": "1.0.0",
        "files": {
            "full": {
                "path": "cogeden.css",
                "size_kb": full_size
            },
            "minified": {
                "path": "cogeden.min.css",
                "size_kb": min_size,
                "reduction": f"{reduction}%"
            },
            "gzipped": {
                "path": "cogeden.min.css.gz",
                "size_kb": gzip_size,
                "reduction": f"{gzip_reduction}%"
            },
            "utilities": {
                "path": "cogeden-utils.js",
                "size_kb": utils_size
            },
            "theme": {
                "path": "cogeden-theme.js",
                "size_kb": theme_size
            },
            "loader": {
                "path": "cogeden-loader.min.js",
                "size_kb": loader_size
            }
        },
        "features": {
            "colors": 524,
            "breakpoints": 6,
            "browser_support": "IE6-11, Servo, Chrome 1+, Firefox 1+, Safari 3+"
        }
    }
    
    manifest_path = f"{output_dir}/build-manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"   ✓ Build manifest created")
    
    # 7. Generate README
    print("\n📦 Step 7: Generating README...")
    readme = f"""# MikoCSS - Production Build

## Files

- **cogeden.css** ({full_size} KB) - Full unminified CSS
- **cogeden.min.css** ({min_size} KB) - Minified CSS ({reduction}% smaller)
- **cogeden.min.css.gz** ({gzip_size} KB) - Gzipped CSS ({gzip_reduction}% smaller)
- **cogeden-utils.js** ({utils_size} KB) - JavaScript utilities for legacy browsers
- **cogeden-theme.js** ({theme_size} KB) - Automatic light/dark theme switcher
- **cogeden-loader.min.js** ({loader_size} KB) - Minified CSS loader

## Usage

### Basic Usage (HTML)
```html
<link rel="stylesheet" href="cogeden.min.css">
```

### With Theme Switcher
```html
<link rel="stylesheet" href="cogeden.min.css">
<script src="cogeden-theme.js"></script>
<script>
  // Theme is automatically initialized
  
  // Create toggle button
  CogedenTheme.createToggleButton('#theme-container');
  
  // Or manually toggle
  CogedenTheme.toggleTheme();
  
  // Listen for theme changes
  document.addEventListener('themechange', function(e) {{
    console.log('Theme changed to:', e.detail.theme);
  }});
</script>
```

### With Utilities
```html
<link rel="stylesheet" href="cogeden.min.css">
<script src="cogeden-utils.js"></script>
<script>
  // Use utility functions
  var element = CogedenUtils.query('.my-element');
  CogedenUtils.addClass(element, 'active');
</script>
```

## Color Scheme System

Automatic light/dark mode support:

```html
<!-- Automatic based on system preference -->
<div class="bg-scheme-primary text-scheme-primary">
  Content adapts to light/dark mode
</div>

<!-- Manual control -->
<body class="dark-mode">
  <div class="bg-scheme-primary">Dark mode content</div>
</body>
```

## Animations

Pulse, spin, bounce, fade, and more:

```html
<div class="animate-pulse">Pulsing element</div>
<div class="animate-spin">Spinning element</div>
<div class="animate-bounce">Bouncing element</div>
<div class="hover:animate-shake">Shake on hover</div>
```

## Browser Support

- Internet Explorer 6-11
- Chrome 1+
- Firefox 1+
- Safari 3+
- Opera 9+
- Servo (all versions)

## Features

- 524 color palette
- 6 responsive breakpoints (xs, sm, md, lg, xl, 2xl)
- Complete grid system (12 columns)
- Automatic light/dark mode
- Advanced animations (pulse, spin, bounce, fade, etc.)
- Form utilities
- Button styles
- Table utilities
- Image utilities
- List utilities
- Legacy browser hacks and polyfills

## Build Info

- Build Date: {js_gen._get_timestamp()}
- Version: 1.0.0
- Total CSS Lines: 20,000+

## License

MIT License
"""
    
    readme_path = f"{output_dir}/README.md"
    with open(readme_path, 'w') as f:
        f.write(readme)
    print(f"   ✓ README created")
    
    # Summary
    print("\n" + "=" * 60)
    print("✨ Production build complete!")
    print("=" * 60)
    print(f"\n📁 Output directory: {output_dir}/")
    print(f"\n📊 Size comparison:")
    print(f"   Full:     {full_size} KB (100%)")
    print(f"   Minified: {min_size} KB ({reduction}% reduction)")
    print(f"   Gzipped:  {gzip_size} KB ({gzip_reduction}% reduction)")
    print(f"\n🚀 Ready for production deployment!")
    print("=" * 60)


if __name__ == "__main__":
    # Parse arguments
    output_dir = "dist"
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("MikoCSS Production Build")
            print("\nUsage:")
            print("  python build.py [output_dir]")
            print("\nOptions:")
            print("  --help          Show this help message")
            print("  --minify        Build minified version only")
            print("  --production    Full production build (default)")
            print("\nExamples:")
            print("  python build.py")
            print("  python build.py dist")
            print("  python build.py output --production")
            sys.exit(0)
        elif sys.argv[1] not in ["--minify", "--production"]:
            output_dir = sys.argv[1]
    
    # Run build
    build_production(output_dir)
