"""
Color Generation Engine
Generates 524 colors: neutrals + color wheel
"""
import colorsys

class ColorEngine:
    def __init__(self, config=None):
        self.colors_map = {}
        self.config = config or {
            "total_hues": 64,
            "shades_per_hue": 8,
            "lightness_start": 0.92,
            "lightness_step": 0.085,
            "saturation_high": 0.95,
            "saturation_low": 0.75
        }
    
    def _hls_to_hex(self, h, l, s):
        """Convert HLS to hex color"""
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return '#{:02x}{:02x}{:02x}'.format(
            int(max(0, min(1, r)) * 255),
            int(max(0, min(1, g)) * 255),
            int(max(0, min(1, b)) * 255)
        )
    
    def generate_palette(self):
        """Generate complete color palette"""
        print("🎨 Generating 524 colors...")
        
        # 1. Neutrals (Black, White, 10 Grays)
        self.colors_map['black'] = '#000000'
        self.colors_map['white'] = '#ffffff'
        for i in range(1, 11):
            l = 1.0 - (i * 0.085)
            self.colors_map[f'gray-{i}00'] = self._hls_to_hex(0, l, 0)

        # 2. Color Wheel (64 Hues * 8 Shades)
        total_hues = self.config["total_hues"]
        shades_per_hue = self.config["shades_per_hue"]
        
        for h in range(total_hues):
            hue_val = h / total_hues
            base_name = f"c{h+1}"
            
            for s in range(shades_per_hue):
                lightness = self.config["lightness_start"] - (s * self.config["lightness_step"])
                saturation = self.config["saturation_high"] if (0.3 < lightness < 0.8) else self.config["saturation_low"]
                
                hex_code = self._hls_to_hex(hue_val, lightness, saturation)
                shade_level = (s + 1) * 100
                self.colors_map[f"{base_name}-{shade_level}"] = hex_code
        
        return self.colors_map
    
    def get_colors(self):
        """Return generated colors"""
        return self.colors_map
