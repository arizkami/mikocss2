# MikoCSS - Complete Documentation

Welcome to MikoCSS, the ultimate CSS framework for legacy browser support with modern features.

## 📚 Documentation Index

1. [Getting Started](./getting-started.md) - Installation and basic usage
2. [Browser Support](./browser-support.md) - Compatibility information
3. [Color System](./color-system.md) - 524 color palette guide
4. [Layout System](./layout-system.md) - Grid, flexbox, and positioning
5. [Responsive Design](./responsive-design.md) - Breakpoints and utilities
6. [Animations](./animations.md) - Pulse, spin, bounce, and more
7. [Theme System](./theme-system.md) - Light/dark mode guide
8. [Components](./components.md) - Buttons, forms, tables, etc.
9. [Legacy Browser Fixes](./legacy-fixes.md) - IE6-11 hacks and polyfills
10. [Build System](./build-system.md) - Production build guide
11. [API Reference](./api-reference.md) - Complete class reference
12. [Examples](./examples.md) - Code examples and demos

## 🚀 Quick Start

```bash
# Generate CSS
python main.py cogeden.css

# Build for production
python build.py
```

```html
<!-- Basic usage -->
<link rel="stylesheet" href="cogeden.css">

<!-- With theme switcher -->
<link rel="stylesheet" href="dist/cogeden.min.css">
<script src="dist/cogeden-theme.js"></script>
```

## 🎯 Key Features

- **524 Colors** - Complete color palette with 64 hues × 8 shades
- **6 Breakpoints** - xs, sm, md, lg, xl, 2xl
- **12 Column Grid** - Flexible grid system with float fallbacks
- **Auto Theme** - Automatic light/dark mode detection
- **Animations** - Pulse, spin, bounce, fade, and more
- **Legacy Support** - IE6-11, Chrome 1+, Firefox 1+, Safari 3+
- **Production Ready** - Minified, gzipped, and optimized

## 📦 What's Included

```
mikocss/
├── core/                   # Core generators
│   ├── css_generator.py   # CSS rule generator
│   ├── color_engine.py    # Color palette generator
│   └── js_generator.py    # JavaScript utilities
├── layouts/               # Layout modules
│   ├── reset.py          # CSS reset
│   ├── utilities.py      # Layout utilities
│   ├── grid.py           # Grid system
│   ├── buttons.py        # Button styles
│   ├── forms.py          # Form utilities
│   ├── tables.py         # Table utilities
│   ├── images.py         # Image utilities
│   ├── lists.py          # List utilities
│   ├── animations.py     # Animation system
│   ├── color_scheme.py   # Theme system
│   ├── effects.py        # Shadows & transforms
│   ├── responsive.py     # Responsive utilities
│   ├── legacy.py         # Legacy browser fixes
│   └── chrome44_polyfill.py # Chrome 44 fixes
├── docs/                 # Documentation
├── test/                 # Test files
├── dist/                 # Production build
├── variable.json         # Configuration
├── main.py              # Main generator
└── build.py             # Build system
```

## 🌐 Browser Support

| Browser | Version | Support Level |
|---------|---------|---------------|
| Internet Explorer | 6-11 | Full |
| Chrome | 1+ | Full |
| Firefox | 1+ | Full |
| Safari | 3+ | Full |
| Opera | 9+ | Full |
| Servo | All | Full |

## 💡 Philosophy

MikoCSS is built on three principles:

1. **No Browser Left Behind** - Support for IE6-11 without compromising modern features
2. **Progressive Enhancement** - Modern browsers get enhanced features, old browsers get functional fallbacks
3. **Production Ready** - Optimized, minified, and ready for deployment

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

MIT License - See LICENSE file for details

## 🔗 Links

- [GitHub Repository](#)
- [Issue Tracker](#)
- [Changelog](./CHANGELOG.md)
- [Migration Guide](./migration.md)

---

**Version:** 1.0.0  
**Last Updated:** 2024  
**Maintained by:** Cogeden Team
