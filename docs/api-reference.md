# API Reference

Complete reference of all MikoCSS classes and utilities.

## Layout

### Display

```
.block              display: block
.inline             display: inline
.inline-block       display: inline-block
.hidden             display: none
.invisible          visibility: hidden
.visible            visibility: visible
```

### Flexbox

```
.flex               display: flex
.inline-flex        display: inline-flex
.flex-row           flex-direction: row
.flex-col           flex-direction: column
.flex-wrap          flex-wrap: wrap
.flex-nowrap        flex-wrap: nowrap

.items-start        align-items: flex-start
.items-center       align-items: center
.items-end          align-items: flex-end
.items-stretch      align-items: stretch

.justify-start      justify-content: flex-start
.justify-center     justify-content: center
.justify-end        justify-content: flex-end
.justify-between    justify-content: space-between
.justify-around     justify-content: space-around

.flex-1             flex: 1 1 0%
.flex-auto          flex: 1 1 auto
.flex-none          flex: none
```

### Float & Clear

```
.float-left         float: left
.float-right        float: right
.float-none         float: none
.clear-both         clear: both
.clear-left         clear: left
.clear-right        clear: right
.clearfix           clearfix hack
```

### Position

```
.static             position: static
.relative           position: relative
.absolute           position: absolute
.fixed              position: fixed
.sticky             position: sticky

.top-{0-8}          top: {value}
.right-{0-8}        right: {value}
.bottom-{0-8}       bottom: {value}
.left-{0-8}         left: {value}
.inset-0            top/right/bottom/left: 0
```

## Spacing

### Margin

```
.m-{0-48}           margin: {value}
.mt-{0-48}          margin-top: {value}
.mb-{0-48}          margin-bottom: {value}
.ml-{0-48}          margin-left: {value}
.mr-{0-48}          margin-right: {value}
.mx-{0-48}          margin-left/right: {value}
.my-{0-48}          margin-top/bottom: {value}
```

### Padding

```
.p-{0-48}           padding: {value}
.pt-{0-48}          padding-top: {value}
.pb-{0-48}          padding-bottom: {value}
.pl-{0-48}          padding-left: {value}
.pr-{0-48}          padding-right: {value}
.px-{0-48}          padding-left/right: {value}
.py-{0-48}          padding-top/bottom: {value}
```

## Typography

### Font Size

```
.text-xs            font-size: 10px
.text-sm            font-size: 12px
.text-base          font-size: 16px
.text-lg            font-size: 20px
.text-xl            font-size: 24px
.text-2xl           font-size: 32px
.text-3xl           font-size: 48px
.text-4xl           font-size: 64px
.text-5xl           font-size: 80px
```

### Font Weight

```
.font-thin          font-weight: 100
.font-light         font-weight: 300
.font-normal        font-weight: 400
.font-medium        font-weight: 500
.font-semibold      font-weight: 600
.font-bold          font-weight: 700
.font-black         font-weight: 900
```

### Text Alignment

```
.text-left          text-align: left
.text-center        text-align: center
.text-right         text-align: right
.text-justify       text-align: justify
```

### Text Transform

```
.uppercase          text-transform: uppercase
.lowercase          text-transform: lowercase
.capitalize         text-transform: capitalize
```

### Text Decoration

```
.underline          text-decoration: underline
.line-through       text-decoration: line-through
.no-underline       text-decoration: none
```

### Text Style

```
.italic             font-style: italic
.not-italic         font-style: normal
```

### Text Overflow

```
.truncate           overflow: hidden; text-overflow: ellipsis
.break-words        word-wrap: break-word
.break-all          word-break: break-all
```

## Sizing

### Width

```
.w-full             width: 100%
.w-half             width: 50%
.w-third            width: 33.333%
.w-quarter          width: 25%
.w-screen           width: 100vw
.w-auto             width: auto
.w-{1-64}           width: {n*4}px

.min-w-0            min-width: 0
.max-w-full         max-width: 100%
```

### Height

```
.h-full             height: 100%
.h-half             height: 50%
.h-screen           height: 100vh
.h-auto             height: auto
.h-{1-64}           height: {n*4}px

.min-h-0            min-height: 0
.max-h-full         max-height: 100%
```

## Borders

### Border Width

```
.border             border-width: 1px
.border-0           border-width: 0
.border-2           border-width: 2px
.border-4           border-width: 4px
.border-t           border-top-width: 1px
.border-r           border-right-width: 1px
.border-b           border-bottom-width: 1px
.border-l           border-left-width: 1px
```

### Border Radius

```
.rounded-none       border-radius: 0
.rounded-sm         border-radius: 2px
.rounded            border-radius: 4px
.rounded-md         border-radius: 6px
.rounded-lg         border-radius: 8px
.rounded-xl         border-radius: 12px
.rounded-2xl        border-radius: 16px
.rounded-full       border-radius: 9999px
```

## Colors

### Background

```
.bg-{color}         background-color: {color}
.bg-black           background-color: #000000
.bg-white           background-color: #ffffff
.bg-gray-{100-1000} background-color: {gray}
.bg-c{1-64}-{100-800} background-color: {color}
```

### Text

```
.text-{color}       color: {color}
```

### Border

```
.border-{color}     border-color: {color}
```

### Theme-Aware

```
.bg-scheme-primary
.bg-scheme-secondary
.bg-scheme-tertiary
.text-scheme-primary
.text-scheme-secondary
.text-scheme-tertiary
.border-scheme
.link-scheme
```

## Effects

### Shadow

```
.shadow-sm          box-shadow: small
.shadow             box-shadow: default
.shadow-md          box-shadow: medium
.shadow-lg          box-shadow: large
.shadow-xl          box-shadow: extra large
.shadow-none        box-shadow: none
.shadow-scheme      theme-aware shadow
```

### Opacity

```
.opacity-0          opacity: 0
.opacity-10         opacity: 0.1
.opacity-20         opacity: 0.2
...
.opacity-100        opacity: 1
```

### Transform

```
.scale-0            transform: scale(0)
.scale-50           transform: scale(0.5)
.scale-75           transform: scale(0.75)
.scale-90           transform: scale(0.9)
.scale-95           transform: scale(0.95)
.scale-100          transform: scale(1)
.scale-105          transform: scale(1.05)
.scale-110          transform: scale(1.1)
.scale-125          transform: scale(1.25)
.scale-150          transform: scale(1.5)

.rotate-0           transform: rotate(0deg)
.rotate-45          transform: rotate(45deg)
.rotate-90          transform: rotate(90deg)
.rotate-180         transform: rotate(180deg)
.-rotate-45         transform: rotate(-45deg)
.-rotate-90         transform: rotate(-90deg)
.-rotate-180        transform: rotate(-180deg)
```

### Transition

```
.transition-none    transition: none
.transition-all     transition: all 0.3s ease
.transition-colors  transition: color, bg, border
.transition-opacity transition: opacity 0.3s ease
.transition-transform transition: transform 0.3s ease
```

## Animations

### Animation Classes

```
.animate-pulse
.animate-spin
.animate-bounce
.animate-ping
.animate-fade-in
.animate-fade-out
.animate-slide-in-left
.animate-slide-in-right
.animate-shake
.animate-wiggle
.animate-heartbeat
```

### Animation Controls

```
.animate-duration-{75-1000}
.animate-delay-{75-1000}
.animate-once
.animate-twice
.animate-infinite
.animate-normal
.animate-reverse
.animate-alternate
.animate-fill-forwards
.animate-fill-backwards
.animate-fill-both
.animate-paused
.animate-running
```

## Grid System

### Container

```
.container          centered container
.container-fluid    full-width container
```

### Row

```
.row                flex row
.row-legacy         float-based row
```

### Columns

```
.col-{1-12}         column width
.col-auto           auto width
.col-legacy-{1-12}  float-based column
.offset-{1-11}      column offset
.order-{1-12}       flex order
.order-first
.order-last
```

### Grid Alignment

```
.align-items-start
.align-items-center
.align-items-end
.justify-content-start
.justify-content-center
.justify-content-end
.justify-content-between
.justify-content-around
```

## Components

### Buttons

```
.btn                base button
.btn-primary
.btn-secondary
.btn-success
.btn-danger
.btn-warning
.btn-info
.btn-light
.btn-dark
.btn-outline-primary
.btn-sm
.btn-lg
.btn-block
.btn-link
```

### Forms

```
.form-group
.form-control
.form-control-sm
.form-control-lg
.form-label
.form-check
.form-check-input
.form-check-label
.form-select
.form-textarea
.is-valid
.is-invalid
.valid-feedback
.invalid-feedback
```

### Lists

```
.list-none
.list-disc
.list-decimal
.list-inline
.list-unstyled
.list-group
.list-group-item
```

### Tables

```
.table
.table-auto
.table-fixed
.table-bordered
.table-striped
.table-hover
.table-responsive
.table-compact
.table-spacious
```

### Images

```
.img-responsive
.img-fluid
.img-rounded
.img-circle
.img-thumbnail
.img-cover
.img-contain
```

## Responsive

All utilities support responsive prefixes:

```
.{breakpoint}:{utility}

xs:     min-width: 480px
sm:     min-width: 640px
md:     min-width: 768px
lg:     min-width: 1024px
xl:     min-width: 1280px
2xl:    min-width: 1536px
```

Examples:
```
.md:flex
.lg:text-2xl
.xl:w-half
.sm:hidden
```

## Utilities

### Overflow

```
.overflow-auto
.overflow-hidden
.overflow-visible
.overflow-scroll
.overflow-x-auto
.overflow-y-auto
```

### Z-Index

```
.z-0
.z-10
.z-20
.z-30
.z-40
.z-50
.z-auto
```

### Cursor

```
.cursor-auto
.cursor-pointer
.cursor-not-allowed
.cursor-move
.cursor-text
```

### User Select

```
.select-none
.select-text
.select-all
.select-auto
```

### Pointer Events

```
.pointer-events-none
.pointer-events-auto
```

## Legacy Browser Utilities

```
.haslayout          IE6/7 hasLayout trigger
.cf                 clearfix
.inline-block-legacy IE6/7 inline-block
.scrollbar-custom   custom scrollbar
.no-select          disable text selection
```

## JavaScript API

### Theme System

```javascript
CogedenTheme.getTheme()
CogedenTheme.setTheme(theme)
CogedenTheme.toggleTheme()
CogedenTheme.init()
CogedenTheme.createToggleButton(container, options)
```

### Utilities

```javascript
CogedenUtils.addClass(element, className)
CogedenUtils.removeClass(element, className)
CogedenUtils.toggleClass(element, className)
CogedenUtils.hasClass(element, className)
CogedenUtils.query(selector)
CogedenUtils.queryAll(selector)
CogedenUtils.on(element, event, handler)
CogedenUtils.off(element, event, handler)
CogedenUtils.getStyle(element, property)
CogedenUtils.detectIE()
CogedenUtils.isLegacyBrowser()
```

## Next Steps

- [View examples](./examples.md)
- [Learn about customization](./customization.md)
- [Read migration guide](./migration.md)
