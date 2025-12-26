"""
Core CSS Generator with Legacy Browser Support
IE6-11, Servo, Chrome 1+, Firefox 1+ Compatible
"""
import re

class CSSGenerator:
    def __init__(self):
        self.css_content = []
    
    def add_rule(self, selector, properties, media_query=None):
        """
        Generates a CSS rule and automatically injects:
        - IE6/7 hacks (*zoom, *display, _property)
        - IE8/9 hacks (filter alpha, -ms-filter)
        - Vendor prefixes (-webkit-, -moz-, -ms-, -o-)
        - Legacy browser fallbacks
        """
        lines = []
        
        if media_query:
            lines.append(f"@media {media_query} {{")
            lines.append(f"{selector} {{")
            indent = "    "
        else:
            lines.append(f"{selector} {{")
            indent = "  "
        
        for prop, val in properties.items():
            # Handle transform properties
            if prop == "transform":
                lines.append(f"{indent}-webkit-transform: {val};")
                lines.append(f"{indent}-moz-transform: {val};")
                lines.append(f"{indent}-ms-transform: {val};")
                lines.append(f"{indent}-o-transform: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Handle transition properties
            if prop == "transition":
                lines.append(f"{indent}-webkit-transition: {val};")
                lines.append(f"{indent}-moz-transition: {val};")
                lines.append(f"{indent}-ms-transition: {val};")
                lines.append(f"{indent}-o-transition: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Handle animation properties
            if prop == "animation":
                lines.append(f"{indent}-webkit-animation: {val};")
                lines.append(f"{indent}-moz-animation: {val};")
                lines.append(f"{indent}-ms-animation: {val};")
                lines.append(f"{indent}-o-animation: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Handle box-shadow
            if prop == "box-shadow":
                lines.append(f"{indent}-webkit-box-shadow: {val};")
                lines.append(f"{indent}-moz-box-shadow: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Handle text-shadow
            if prop == "text-shadow":
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Handle linear-gradient
            if "linear-gradient" in str(val):
                lines.append(f"{indent}background: {self._legacy_gradient(val)};")
                lines.append(f"{indent}background: -webkit-{val};")
                lines.append(f"{indent}background: -moz-{val};")
                lines.append(f"{indent}background: -o-{val};")
                lines.append(f"{indent}background: {val};")
                continue
            
            # Border Radius Prefixes
            if "border-radius" in prop:
                lines.append(f"{indent}-webkit-{prop}: {val};")
                lines.append(f"{indent}-moz-{prop}: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue

            # Flexbox Polyfills
            if prop == "display" and val == "flex":
                lines.append(f"{indent}display: -webkit-box;")
                lines.append(f"{indent}display: -moz-box;")
                lines.append(f"{indent}display: -ms-flexbox;")
                lines.append(f"{indent}display: -webkit-flex;")
                lines.append(f"{indent}display: flex;")
                continue

            # Inline-Block Hack for IE 6/7
            if prop == "display" and val == "inline-block":
                lines.append(f"{indent}{prop}: {val};")
                lines.append(f"{indent}*display: inline;")
                lines.append(f"{indent}*zoom: 1;")
                continue

            # Opacity Polyfill for IE 8/9
            if prop == "opacity":
                try:
                    opacity_val = int(float(val) * 100)
                    lines.append(f"{indent}{prop}: {val};")
                    lines.append(f"{indent}-ms-filter: \"progid:DXImageTransform.Microsoft.Alpha(Opacity={opacity_val})\";")
                    lines.append(f"{indent}filter: alpha(opacity={opacity_val});")
                    lines.append(f"{indent}zoom: 1;")
                except ValueError:
                    lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Box Sizing
            if prop == "box-sizing":
                lines.append(f"{indent}-webkit-box-sizing: {val};")
                lines.append(f"{indent}-moz-box-sizing: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # User Select
            if prop == "user-select":
                lines.append(f"{indent}-webkit-user-select: {val};")
                lines.append(f"{indent}-moz-user-select: {val};")
                lines.append(f"{indent}-ms-user-select: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Appearance
            if prop == "appearance":
                lines.append(f"{indent}-webkit-appearance: {val};")
                lines.append(f"{indent}-moz-appearance: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Column properties
            if prop in ["column-count", "column-gap", "column-rule"]:
                lines.append(f"{indent}-webkit-{prop}: {val};")
                lines.append(f"{indent}-moz-{prop}: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Flex properties for old syntax
            if prop == "flex":
                lines.append(f"{indent}-webkit-box-flex: {val};")
                lines.append(f"{indent}-moz-box-flex: {val};")
                lines.append(f"{indent}-webkit-flex: {val};")
                lines.append(f"{indent}-ms-flex: {val};")
                lines.append(f"{indent}{prop}: {val};")
                continue
            
            # Standard property
            lines.append(f"{indent}{prop}: {val};")

        if media_query:
            lines.append("  }")
            lines.append("}")
        else:
            lines.append("}")
        
        self.css_content.append("\n".join(lines))
    
    def _legacy_gradient(self, gradient_str):
        """Generate IE9 fallback color for gradients"""
        match = re.search(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}|rgba?\([^)]+\)', str(gradient_str))
        return match.group(0) if match else "#cccccc"
    
    def get_css(self):
        """Return generated CSS content"""
        return "\n".join(self.css_content)
    
    def clear(self):
        """Clear CSS content"""
        self.css_content = []
