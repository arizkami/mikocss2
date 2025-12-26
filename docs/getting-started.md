# Getting Started with MikoCSS

## Installation

### Method 1: Generate from Source

```bash
# Clone or download the repository
cd mikocss

# Generate CSS file
python main.py cogeden.css

# Use in your HTML
<link rel="stylesheet" href="cogeden.css">
```

### Method 2: Production Build

```bash
# Build optimized files
python build.py

# Files will be in dist/ folder
# - cogeden.css (full)
# - cogeden.min.css (minified)
# - cogeden.min.css.gz (gzipped)
# - cogeden-utils.js (utilities)
# - cogeden-theme.js (theme switcher)
```

### Method 3: CDN (Coming Soon)

```html
<link rel="stylesheet" href="https://cdn.cogeden.css/1.0.0/cogeden.min.css">
```

## Basic Usage

### HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="cogeden.css">
</head>
<body>
    <div class="container">
        <h1 class="text-3xl font-bold text-center">Hello World</h1>
        <p class="text-base text-gray-700">Welcome to MikoCSS!</p>
    </div>
</body>
</html>
```

## First Examples

### 1. Simple Layout

```html
<div class="container py-8">
    <div class="row">
        <div class="col-6">
            <div class="bg-c16-400 text-white p-6 rounded">
                Column 1
            </div>
        </div>
        <div class="col-6">
            <div class="bg-c32-400 text-white p-6 rounded">
                Column 2
            </div>
        </div>
    </div>
</div>
```

### 2. Button Styles

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
```

### 3. Responsive Design

```html
<div class="hidden md:block">
    Visible on medium screens and up
</div>

<div class="text-sm md:text-lg lg:text-2xl">
    Responsive text size
</div>
```

### 4. Animations

```html
<div class="animate-pulse">Pulsing element</div>
<div class="animate-spin">Spinning element</div>
<div class="hover:animate-bounce">Bounce on hover</div>
```

### 5. Theme System

```html
<!-- Auto-adapting colors -->
<div class="bg-scheme-primary text-scheme-primary">
    Adapts to light/dark mode
</div>

<!-- With theme switcher -->
<script src="cogeden-theme.js"></script>
<script>
    // Create toggle button
    CogedenTheme.createToggleButton('#theme-container');
</script>
```

## Configuration

### Customize Colors

Edit `variable.json`:

```json
{
  "spacing": {
    "0": "0px",
    "1": "4px",
    "2": "8px"
  },
  "font_sizes": {
    "xs": "10px",
    "sm": "12px",
    "base": "16px"
  },
  "breakpoints": {
    "xs": "480px",
    "sm": "640px",
    "md": "768px"
  }
}
```

### Regenerate CSS

```bash
python main.py custom-output.css
```

## Common Patterns

### Card Component

```html
<div class="bg-white rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-4">Card Title</h2>
    <p class="text-gray-700 mb-4">Card content goes here.</p>
    <button class="btn btn-primary">Action</button>
</div>
```

### Navigation Bar

```html
<nav class="bg-c1-700 text-white p-4">
    <div class="container flex items-center justify-between">
        <div class="text-xl font-bold">Logo</div>
        <div class="flex">
            <a href="#" class="mx-2 p-2">Home</a>
            <a href="#" class="mx-2 p-2">About</a>
            <a href="#" class="mx-2 p-2">Contact</a>
        </div>
    </div>
</nav>
```

### Form Layout

```html
<form class="bg-white p-6 rounded shadow">
    <div class="form-group">
        <label class="form-label">Email</label>
        <input type="email" class="form-control" placeholder="Enter email">
    </div>
    <div class="form-group">
        <label class="form-label">Password</label>
        <input type="password" class="form-control" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## Next Steps

- [Learn about the color system](./color-system.md)
- [Explore responsive design](./responsive-design.md)
- [Master animations](./animations.md)
- [Set up theme switching](./theme-system.md)
- [View complete examples](./examples.md)

## Troubleshooting

### CSS not loading?

1. Check file path is correct
2. Verify file was generated successfully
3. Check browser console for errors

### Styles not working in old browsers?

1. Ensure you're using the full `cogeden.css` (not minified)
2. Check that legacy polyfills are included
3. Test with `cogeden-utils.js` for JavaScript features

### Need help?

- Check [API Reference](./api-reference.md)
- See [Examples](./examples.md)
- Review [Legacy Browser Fixes](./legacy-fixes.md)
