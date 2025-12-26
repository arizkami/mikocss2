# Theme System (Light/Dark Mode)

MikoCSS includes an automatic light/dark theme system with full legacy browser support.

## Quick Start

```html
<!-- Include CSS -->
<link rel="stylesheet" href="cogeden.css">

<!-- Include theme switcher -->
<script src="cogeden-theme.js"></script>

<!-- Theme is automatically initialized -->
```

## Automatic Theme Detection

The system automatically detects the user's preferred color scheme:

```html
<!-- This adapts automatically -->
<div class="bg-scheme-primary text-scheme-primary">
    Content adapts to light/dark mode
</div>
```

## Theme-Aware Classes

### Background Colors

```html
<div class="bg-scheme-primary">Primary background</div>
<div class="bg-scheme-secondary">Secondary background</div>
<div class="bg-scheme-tertiary">Tertiary background</div>
```

**Light Mode:**
- primary: #ffffff (white)
- secondary: #f8f9fa (light gray)
- tertiary: #e9ecef (lighter gray)

**Dark Mode:**
- primary: #1a1a1a (dark)
- secondary: #2d2d2d (medium dark)
- tertiary: #3a3a3a (lighter dark)

### Text Colors

```html
<p class="text-scheme-primary">Primary text</p>
<p class="text-scheme-secondary">Secondary text</p>
<p class="text-scheme-tertiary">Tertiary text</p>
```

### Border & Shadow

```html
<div class="border border-scheme">Theme-aware border</div>
<div class="shadow-scheme">Theme-aware shadow</div>
```

### Links

```html
<a href="#" class="link-scheme">Theme-aware link</a>
```

## Manual Theme Control

### JavaScript API

```javascript
// Get current theme
var theme = CogedenTheme.getTheme(); // 'light' or 'dark'

// Set theme
CogedenTheme.setTheme('dark');
CogedenTheme.setTheme('light');

// Toggle theme
CogedenTheme.toggleTheme();

// Initialize (called automatically)
CogedenTheme.init();
```

### Create Toggle Button

```javascript
// Create button in container
CogedenTheme.createToggleButton('#theme-container');

// With custom options
CogedenTheme.createToggleButton('#theme-container', {
    className: 'btn btn-secondary',
    lightIcon: '☀️ Light',
    darkIcon: '🌙 Dark'
});
```

### Listen for Theme Changes

```javascript
document.addEventListener('themechange', function(e) {
    console.log('Theme changed to:', e.detail.theme);
    
    // Update UI based on theme
    if (e.detail.theme === 'dark') {
        // Dark mode specific code
    } else {
        // Light mode specific code
    }
});
```

## Manual Theme Classes

Force a specific theme regardless of system preference:

```html
<!-- Force dark mode -->
<body class="dark-mode">
    <div class="bg-scheme-primary">Always dark</div>
</body>

<!-- Force light mode -->
<body class="light-mode">
    <div class="bg-scheme-primary">Always light</div>
</body>
```

## Media Query Support

For browsers that support `prefers-color-scheme`:

```html
<!-- Auto dark mode -->
<div class="auto-dark:bg-dark">Dark in dark mode</div>
<div class="auto-dark:text-light">Light text in dark mode</div>

<!-- Auto light mode -->
<div class="auto-light:bg-light">Light in light mode</div>
<div class="auto-light:text-dark">Dark text in light mode</div>
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Theme Example</title>
    <link rel="stylesheet" href="cogeden.css">
</head>
<body class="bg-scheme-primary text-scheme-primary">
    
    <!-- Header with theme toggle -->
    <header class="bg-scheme-secondary p-4 border-b border-scheme">
        <div class="container flex items-center justify-between">
            <h1 class="text-2xl font-bold">My App</h1>
            <div id="theme-toggle"></div>
        </div>
    </header>
    
    <!-- Main content -->
    <main class="container py-8">
        <div class="bg-scheme-secondary rounded-lg shadow-scheme p-6">
            <h2 class="text-xl font-bold mb-4">Theme-Aware Card</h2>
            <p class="text-scheme-secondary mb-4">
                This card adapts to light/dark mode automatically.
            </p>
            <a href="#" class="link-scheme">Theme-aware link</a>
        </div>
    </main>
    
    <!-- Theme switcher -->
    <script src="cogeden-theme.js"></script>
    <script>
        // Create toggle button
        CogedenTheme.createToggleButton('#theme-toggle', {
            className: 'btn btn-secondary',
            lightIcon: '☀️',
            darkIcon: '🌙'
        });
        
        // Listen for changes
        document.addEventListener('themechange', function(e) {
            console.log('Theme:', e.detail.theme);
        });
    </script>
</body>
</html>
```

## Browser Support

### Modern Browsers (Full Support)
- Chrome 76+ (prefers-color-scheme support)
- Firefox 67+
- Safari 12.1+
- Edge 79+

### Legacy Browsers (Manual Control)
- Chrome 44-75 (manual theme switching works)
- Firefox 1-66 (manual theme switching works)
- IE 11 (manual theme switching with polyfills)
- IE 9-10 (basic support with fallbacks)
- IE 6-8 (graceful degradation)

## Customization

### Custom Theme Colors

Edit `layouts/color_scheme.py`:

```python
# Modify CSS variables
:root {
  --bg-primary: #your-color;
  --text-primary: #your-color;
  /* ... */
}
```

### Custom Theme Logic

```javascript
// Override theme detection
CogedenTheme.getTheme = function() {
    // Your custom logic
    return 'dark';
};
```

## Best Practices

1. **Use theme-aware classes** for main UI elements
2. **Provide manual toggle** for user preference
3. **Test in both modes** during development
4. **Consider contrast** in both themes
5. **Save user preference** (done automatically)

## Common Patterns

### Card Component

```html
<div class="bg-scheme-secondary rounded-lg shadow-scheme p-6 border border-scheme">
    <h3 class="text-scheme-primary font-bold mb-2">Card Title</h3>
    <p class="text-scheme-secondary">Card content</p>
</div>
```

### Navigation Bar

```html
<nav class="bg-scheme-secondary border-b border-scheme">
    <div class="container flex items-center justify-between p-4">
        <div class="text-scheme-primary font-bold">Logo</div>
        <div class="flex">
            <a href="#" class="link-scheme mx-2">Home</a>
            <a href="#" class="link-scheme mx-2">About</a>
        </div>
    </div>
</nav>
```

### Form

```html
<form class="bg-scheme-secondary p-6 rounded-lg shadow-scheme">
    <div class="form-group">
        <label class="form-label text-scheme-primary">Email</label>
        <input type="email" class="form-control bg-scheme-primary text-scheme-primary border-scheme">
    </div>
    <button class="btn btn-primary">Submit</button>
</form>
```

## Troubleshooting

### Theme not switching?

1. Check that `cogeden-theme.js` is loaded
2. Verify localStorage is available
3. Check browser console for errors

### Colors not changing?

1. Use `bg-scheme-*` classes, not regular color classes
2. Ensure CSS variables are supported (or fallbacks work)
3. Check that theme class is on `<html>` element

### Old browser issues?

1. Include Chrome 44 polyfill
2. Use fallback colors in CSS
3. Test with `cogeden-utils.js`

## Next Steps

- [Learn about color system](./color-system.md)
- [Explore animations](./animations.md)
- [View complete examples](./examples.md)
