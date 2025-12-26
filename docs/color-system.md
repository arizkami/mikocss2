# Color System

MikoCSS includes a comprehensive 524-color palette designed for maximum flexibility.

## Color Palette Structure

### Neutrals (12 colors)

- `black` - #000000
- `white` - #ffffff
- `gray-100` to `gray-1000` - 10 shades of gray

```html
<div class="bg-black text-white">Black background</div>
<div class="bg-white text-black">White background</div>
<div class="bg-gray-500 text-white">Gray background</div>
```

### Color Wheel (512 colors)

64 hues × 8 shades = 512 colors

Format: `c{hue}-{shade}`
- Hue: 1-64
- Shade: 100, 200, 300, 400, 500, 600, 700, 800

```html
<!-- Red spectrum -->
<div class="bg-c1-100">Lightest red</div>
<div class="bg-c1-400">Medium red</div>
<div class="bg-c1-800">Darkest red</div>

<!-- Blue spectrum -->
<div class="bg-c16-400">Blue</div>

<!-- Green spectrum -->
<div class="bg-c32-400">Green</div>

<!-- Yellow spectrum -->
<div class="bg-c48-400">Yellow</div>
```

## Color Utilities

### Background Colors

```html
<div class="bg-{color}">Background color</div>

<!-- Examples -->
<div class="bg-c16-400">Blue background</div>
<div class="bg-gray-200">Light gray background</div>
<div class="bg-white">White background</div>
```

### Text Colors

```html
<div class="text-{color}">Text color</div>

<!-- Examples -->
<p class="text-c1-600">Red text</p>
<p class="text-gray-700">Dark gray text</p>
<p class="text-black">Black text</p>
```

### Border Colors

```html
<div class="border border-{color}">Border color</div>

<!-- Examples -->
<div class="border border-c32-400">Green border</div>
<div class="border border-gray-300">Gray border</div>
```

## Theme-Aware Colors

Colors that automatically adapt to light/dark mode:

```html
<!-- Background colors -->
<div class="bg-scheme-primary">Primary background</div>
<div class="bg-scheme-secondary">Secondary background</div>
<div class="bg-scheme-tertiary">Tertiary background</div>

<!-- Text colors -->
<p class="text-scheme-primary">Primary text</p>
<p class="text-scheme-secondary">Secondary text</p>
<p class="text-scheme-tertiary">Tertiary text</p>

<!-- Border colors -->
<div class="border border-scheme">Theme-aware border</div>

<!-- Link colors -->
<a href="#" class="link-scheme">Theme-aware link</a>
```

## Color Combinations

### High Contrast

```html
<div class="bg-black text-white">High contrast</div>
<div class="bg-c1-700 text-white">Dark red with white text</div>
```

### Subtle Contrast

```html
<div class="bg-gray-100 text-gray-800">Subtle contrast</div>
<div class="bg-c16-100 text-c16-800">Light blue with dark blue text</div>
```

### Complementary Colors

```html
<!-- Blue and orange -->
<div class="bg-c16-400 text-white">Blue</div>
<div class="bg-c48-400 text-white">Orange</div>

<!-- Red and green -->
<div class="bg-c1-400 text-white">Red</div>
<div class="bg-c32-400 text-white">Green</div>
```

## Color Picker Guide

### Finding the Right Hue

| Hue Range | Color Family |
|-----------|--------------|
| c1-c8 | Red to Pink |
| c9-c16 | Pink to Purple |
| c17-c24 | Purple to Blue |
| c25-c32 | Blue to Cyan |
| c33-c40 | Cyan to Green |
| c41-c48 | Green to Yellow |
| c49-c56 | Yellow to Orange |
| c57-c64 | Orange to Red |

### Choosing Shade Levels

| Shade | Use Case |
|-------|----------|
| 100 | Very light backgrounds, subtle highlights |
| 200 | Light backgrounds, hover states |
| 300 | Borders, dividers |
| 400 | Default UI elements |
| 500 | Primary actions, emphasis |
| 600 | Hover states for primary actions |
| 700 | Active states, dark backgrounds |
| 800 | Very dark backgrounds, high contrast |

## Accessibility

### WCAG Contrast Guidelines

```html
<!-- Good contrast (WCAG AA) -->
<div class="bg-c16-700 text-white">Accessible</div>
<div class="bg-white text-gray-900">Accessible</div>

<!-- Poor contrast (avoid) -->
<div class="bg-c16-200 text-c16-300">Hard to read</div>
```

### Recommended Combinations

```html
<!-- Light backgrounds -->
<div class="bg-white text-gray-900">Excellent contrast</div>
<div class="bg-gray-100 text-gray-800">Good contrast</div>

<!-- Dark backgrounds -->
<div class="bg-gray-900 text-white">Excellent contrast</div>
<div class="bg-c1-700 text-white">Good contrast</div>

<!-- Colored backgrounds -->
<div class="bg-c16-500 text-white">Good contrast</div>
<div class="bg-c32-600 text-white">Good contrast</div>
```

## Custom Color Configuration

Edit `variable.json` to customize the color generation:

```json
{
  "colors": {
    "palette": {
      "total_hues": 64,
      "shades_per_hue": 8,
      "lightness_start": 0.92,
      "lightness_step": 0.085,
      "saturation_high": 0.95,
      "saturation_low": 0.75
    }
  }
}
```

Then regenerate:

```bash
python main.py cogeden.css
```

## Examples

### Color Palette Display

```html
<div class="flex flex-wrap">
    <div class="bg-c1-400 text-white p-4 m-2">c1-400</div>
    <div class="bg-c16-400 text-white p-4 m-2">c16-400</div>
    <div class="bg-c32-400 text-white p-4 m-2">c32-400</div>
    <div class="bg-c48-400 text-white p-4 m-2">c48-400</div>
</div>
```

### Gradient Effect (using multiple shades)

```html
<div class="flex">
    <div class="bg-c16-100 p-4 flex-1">100</div>
    <div class="bg-c16-200 p-4 flex-1">200</div>
    <div class="bg-c16-300 p-4 flex-1">300</div>
    <div class="bg-c16-400 p-4 flex-1 text-white">400</div>
    <div class="bg-c16-500 p-4 flex-1 text-white">500</div>
    <div class="bg-c16-600 p-4 flex-1 text-white">600</div>
    <div class="bg-c16-700 p-4 flex-1 text-white">700</div>
    <div class="bg-c16-800 p-4 flex-1 text-white">800</div>
</div>
```

### Status Colors

```html
<!-- Success -->
<div class="bg-c32-500 text-white p-4">Success message</div>

<!-- Warning -->
<div class="bg-c48-400 text-white p-4">Warning message</div>

<!-- Error -->
<div class="bg-c1-500 text-white p-4">Error message</div>

<!-- Info -->
<div class="bg-c16-500 text-white p-4">Info message</div>
```

## Browser Support

All color utilities work in:
- IE6+ (with fallbacks)
- Chrome 1+
- Firefox 1+
- Safari 3+
- All modern browsers

## Next Steps

- [Learn about theme system](./theme-system.md)
- [Explore responsive colors](./responsive-design.md)
- [View component examples](./components.md)
