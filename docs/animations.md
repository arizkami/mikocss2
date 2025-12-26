# Animations

MikoCSS includes a comprehensive animation system with full legacy browser support.

## Available Animations

### Pulse Animations

```html
<!-- Standard pulse -->
<div class="animate-pulse">Pulsing element</div>

<!-- Heartbeat -->
<div class="animate-heartbeat">Heartbeat effect</div>

<!-- Ping (scale pulse) -->
<div class="animate-ping">Ping effect</div>
```

### Rotation Animations

```html
<!-- Continuous spin -->
<div class="animate-spin">Spinning element</div>

<!-- Wiggle -->
<div class="animate-wiggle">Wiggling element</div>

<!-- Static rotation -->
<div class="rotate-45">Rotated 45°</div>
<div class="rotate-90">Rotated 90°</div>
<div class="rotate-180">Rotated 180°</div>
<div class="-rotate-45">Rotated -45°</div>
```

### Movement Animations

```html
<!-- Bounce -->
<div class="animate-bounce">Bouncing element</div>

<!-- Shake -->
<div class="animate-shake">Shaking element</div>

<!-- Slide in from left -->
<div class="animate-slide-in-left">Slides from left</div>

<!-- Slide in from right -->
<div class="animate-slide-in-right">Slides from right</div>
```

### Fade Animations

```html
<!-- Fade in -->
<div class="animate-fade-in">Fades in</div>

<!-- Fade out -->
<div class="animate-fade-out">Fades out</div>
```

## Animation Controls

### Duration

```html
<div class="animate-pulse animate-duration-75">75ms</div>
<div class="animate-pulse animate-duration-100">100ms</div>
<div class="animate-pulse animate-duration-150">150ms</div>
<div class="animate-pulse animate-duration-200">200ms</div>
<div class="animate-pulse animate-duration-300">300ms</div>
<div class="animate-pulse animate-duration-500">500ms</div>
<div class="animate-pulse animate-duration-700">700ms</div>
<div class="animate-pulse animate-duration-1000">1000ms</div>
```

### Delay

```html
<div class="animate-bounce animate-delay-100">Delayed 100ms</div>
<div class="animate-bounce animate-delay-200">Delayed 200ms</div>
<div class="animate-bounce animate-delay-500">Delayed 500ms</div>
<div class="animate-bounce animate-delay-1000">Delayed 1000ms</div>
```

### Iteration Count

```html
<!-- Play once -->
<div class="animate-bounce animate-once">Plays once</div>

<!-- Play twice -->
<div class="animate-bounce animate-twice">Plays twice</div>

<!-- Play infinitely -->
<div class="animate-bounce animate-infinite">Plays forever</div>
```

### Direction

```html
<!-- Normal direction -->
<div class="animate-bounce animate-normal">Normal</div>

<!-- Reverse direction -->
<div class="animate-bounce animate-reverse">Reverse</div>

<!-- Alternate direction -->
<div class="animate-bounce animate-alternate">Alternate</div>
```

### Fill Mode

```html
<div class="animate-fade-in animate-fill-forwards">Stays visible</div>
<div class="animate-fade-in animate-fill-backwards">Starts from first frame</div>
<div class="animate-fade-in animate-fill-both">Both</div>
```

### Play State

```html
<!-- Paused -->
<div class="animate-spin animate-paused">Paused</div>

<!-- Running -->
<div class="animate-spin animate-running">Running</div>
```

## Hover Animations

```html
<!-- Pulse on hover -->
<div class="hover:animate-pulse">Hover to pulse</div>

<!-- Bounce on hover -->
<div class="hover:animate-bounce">Hover to bounce</div>

<!-- Shake on hover -->
<div class="hover:animate-shake">Hover to shake</div>
```

## Combining Animations

```html
<!-- Fast pulse with delay -->
<div class="animate-pulse animate-duration-300 animate-delay-200">
    Fast pulse with delay
</div>

<!-- Bounce twice then stop -->
<div class="animate-bounce animate-twice animate-fill-forwards">
    Bounce twice
</div>

<!-- Slow spin -->
<div class="animate-spin animate-duration-1000">
    Slow spin
</div>
```

## Loading Indicators

### Spinner

```html
<div class="inline-block w-12 h-12 border-4 border-c16-400 border-t-transparent rounded-full animate-spin"></div>
```

### Pulse Loader

```html
<div class="inline-block w-12 h-12 bg-c24-400 rounded-full animate-pulse"></div>
```

### Ping Loader

```html
<div class="inline-block w-12 h-12 bg-c32-400 rounded-full animate-ping"></div>
```

### Bounce Loader

```html
<div class="flex">
    <div class="w-3 h-3 bg-c16-400 rounded-full animate-bounce mr-2"></div>
    <div class="w-3 h-3 bg-c16-400 rounded-full animate-bounce animate-delay-100 mr-2"></div>
    <div class="w-3 h-3 bg-c16-400 rounded-full animate-bounce animate-delay-200"></div>
</div>
```

## Button Animations

```html
<!-- Scale on hover -->
<button class="btn btn-primary transition-all hover:scale-110">
    Hover me
</button>

<!-- Shake on hover -->
<button class="btn btn-danger hover:animate-shake">
    Shake button
</button>

<!-- Pulsing button -->
<button class="btn btn-success animate-pulse">
    Pulsing button
</button>
```

## Card Animations

```html
<!-- Fade in card -->
<div class="bg-white rounded shadow-lg p-6 animate-fade-in">
    <h3>Card Title</h3>
    <p>Card content</p>
</div>

<!-- Slide in card -->
<div class="bg-white rounded shadow-lg p-6 animate-slide-in-left">
    <h3>Card Title</h3>
    <p>Card content</p>
</div>

<!-- Hover scale card -->
<div class="bg-white rounded shadow-lg p-6 transition-all hover:scale-105">
    <h3>Card Title</h3>
    <p>Card content</p>
</div>
```

## Notification Animations

```html
<!-- Success notification -->
<div class="bg-c32-500 text-white p-4 rounded animate-slide-in-right">
    ✓ Success! Your changes have been saved.
</div>

<!-- Error notification -->
<div class="bg-c1-500 text-white p-4 rounded animate-shake">
    ✗ Error! Something went wrong.
</div>

<!-- Info notification -->
<div class="bg-c16-500 text-white p-4 rounded animate-fade-in">
    ℹ Info: New update available.
</div>
```

## Browser Support

### Modern Browsers
All animations work perfectly in:
- Chrome 44+
- Firefox 16+
- Safari 9+
- Edge (all versions)

### Legacy Browsers
Animations work with vendor prefixes in:
- Chrome 1-43 (with -webkit- prefix)
- Firefox 5-15 (with -moz- prefix)
- Safari 4-8 (with -webkit- prefix)
- IE 10-11 (with -ms- prefix)

### Very Old Browsers
- IE 6-9: Animations gracefully degrade (no animation, but content visible)
- Chrome 1-3: Limited animation support

## Performance Tips

1. **Use transform over position** - Better performance
2. **Limit simultaneous animations** - Don't animate too many elements at once
3. **Use will-change sparingly** - Only for critical animations
4. **Prefer CSS over JavaScript** - CSS animations are hardware accelerated

## Custom Animations

You can create custom animations by editing `layouts/animations.py`:

```python
# Add to generate_keyframes()
generator.css_content.append("""
@keyframes myCustomAnimation {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}
""")

# Add utility class
generator.add_rule(".animate-custom", {
    "animation": "myCustomAnimation 1s ease-in-out infinite"
})
```

Then regenerate:

```bash
python main.py cogeden.css
```

## Examples

See [demo-animations-theme.html](../demo-animations-theme.html) for live examples.

## Next Steps

- [Learn about transitions](./effects.md)
- [Explore theme system](./theme-system.md)
- [View component examples](./components.md)
