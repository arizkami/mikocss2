"""
Animation Utilities with Legacy Browser Support
Includes keyframes, pulse, spin, bounce, fade, etc.
"""

def generate_keyframes(generator):
    """Generate CSS keyframes with vendor prefixes"""
    
    # Pulse animation
    generator.css_content.append("""
@-webkit-keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
@-moz-keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
@-o-keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}""")
    
    # Spin animation
    generator.css_content.append("""
@-webkit-keyframes spin {
  from { -webkit-transform: rotate(0deg); }
  to { -webkit-transform: rotate(360deg); }
}
@-moz-keyframes spin {
  from { -moz-transform: rotate(0deg); }
  to { -moz-transform: rotate(360deg); }
}
@-o-keyframes spin {
  from { -o-transform: rotate(0deg); }
  to { -o-transform: rotate(360deg); }
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}""")
    
    # Bounce animation
    generator.css_content.append("""
@-webkit-keyframes bounce {
  0%, 100% { -webkit-transform: translateY(0); }
  50% { -webkit-transform: translateY(-20px); }
}
@-moz-keyframes bounce {
  0%, 100% { -moz-transform: translateY(0); }
  50% { -moz-transform: translateY(-20px); }
}
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}""")
    
    # Fade in animation
    generator.css_content.append("""
@-webkit-keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@-moz-keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}""")
    
    # Fade out animation
    generator.css_content.append("""
@-webkit-keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
@-moz-keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}""")
    
    # Slide in from left
    generator.css_content.append("""
@-webkit-keyframes slideInLeft {
  from { -webkit-transform: translateX(-100%); }
  to { -webkit-transform: translateX(0); }
}
@-moz-keyframes slideInLeft {
  from { -moz-transform: translateX(-100%); }
  to { -moz-transform: translateX(0); }
}
@keyframes slideInLeft {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}""")
    
    # Slide in from right
    generator.css_content.append("""
@-webkit-keyframes slideInRight {
  from { -webkit-transform: translateX(100%); }
  to { -webkit-transform: translateX(0); }
}
@-moz-keyframes slideInRight {
  from { -moz-transform: translateX(100%); }
  to { -moz-transform: translateX(0); }
}
@keyframes slideInRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}""")
    
    # Shake animation
    generator.css_content.append("""
@-webkit-keyframes shake {
  0%, 100% { -webkit-transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { -webkit-transform: translateX(-10px); }
  20%, 40%, 60%, 80% { -webkit-transform: translateX(10px); }
}
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
  20%, 40%, 60%, 80% { transform: translateX(10px); }
}""")
    
    # Ping animation (scale pulse)
    generator.css_content.append("""
@-webkit-keyframes ping {
  0% { -webkit-transform: scale(1); opacity: 1; }
  75%, 100% { -webkit-transform: scale(2); opacity: 0; }
}
@keyframes ping {
  0% { transform: scale(1); opacity: 1; }
  75%, 100% { transform: scale(2); opacity: 0; }
}""")
    
    # Wiggle animation
    generator.css_content.append("""
@-webkit-keyframes wiggle {
  0%, 100% { -webkit-transform: rotate(0deg); }
  25% { -webkit-transform: rotate(-5deg); }
  75% { -webkit-transform: rotate(5deg); }
}
@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-5deg); }
  75% { transform: rotate(5deg); }
}""")
    
    # Heartbeat animation
    generator.css_content.append("""
@-webkit-keyframes heartbeat {
  0%, 100% { -webkit-transform: scale(1); }
  10%, 30% { -webkit-transform: scale(1.1); }
  20%, 40% { -webkit-transform: scale(1); }
}
@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  10%, 30% { transform: scale(1.1); }
  20%, 40% { transform: scale(1); }
}""")


def generate_animation_utilities(generator):
    """Generate animation utility classes"""
    
    # Animation classes
    generator.add_rule(".animate-pulse", {
        "animation": "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite"
    })
    
    generator.add_rule(".animate-spin", {
        "animation": "spin 1s linear infinite"
    })
    
    generator.add_rule(".animate-bounce", {
        "animation": "bounce 1s infinite"
    })
    
    generator.add_rule(".animate-ping", {
        "animation": "ping 1s cubic-bezier(0, 0, 0.2, 1) infinite"
    })
    
    generator.add_rule(".animate-fade-in", {
        "animation": "fadeIn 0.5s ease-in"
    })
    
    generator.add_rule(".animate-fade-out", {
        "animation": "fadeOut 0.5s ease-out"
    })
    
    generator.add_rule(".animate-slide-in-left", {
        "animation": "slideInLeft 0.5s ease-out"
    })
    
    generator.add_rule(".animate-slide-in-right", {
        "animation": "slideInRight 0.5s ease-out"
    })
    
    generator.add_rule(".animate-shake", {
        "animation": "shake 0.5s ease-in-out"
    })
    
    generator.add_rule(".animate-wiggle", {
        "animation": "wiggle 1s ease-in-out infinite"
    })
    
    generator.add_rule(".animate-heartbeat", {
        "animation": "heartbeat 1.5s ease-in-out infinite"
    })
    
    # Animation duration
    generator.add_rule(".animate-duration-75", {"animation-duration": "75ms"})
    generator.add_rule(".animate-duration-100", {"animation-duration": "100ms"})
    generator.add_rule(".animate-duration-150", {"animation-duration": "150ms"})
    generator.add_rule(".animate-duration-200", {"animation-duration": "200ms"})
    generator.add_rule(".animate-duration-300", {"animation-duration": "300ms"})
    generator.add_rule(".animate-duration-500", {"animation-duration": "500ms"})
    generator.add_rule(".animate-duration-700", {"animation-duration": "700ms"})
    generator.add_rule(".animate-duration-1000", {"animation-duration": "1000ms"})
    
    # Animation delay
    generator.add_rule(".animate-delay-75", {"animation-delay": "75ms"})
    generator.add_rule(".animate-delay-100", {"animation-delay": "100ms"})
    generator.add_rule(".animate-delay-150", {"animation-delay": "150ms"})
    generator.add_rule(".animate-delay-200", {"animation-delay": "200ms"})
    generator.add_rule(".animate-delay-300", {"animation-delay": "300ms"})
    generator.add_rule(".animate-delay-500", {"animation-delay": "500ms"})
    generator.add_rule(".animate-delay-700", {"animation-delay": "700ms"})
    generator.add_rule(".animate-delay-1000", {"animation-delay": "1000ms"})
    
    # Animation iteration
    generator.add_rule(".animate-once", {"animation-iteration-count": "1"})
    generator.add_rule(".animate-twice", {"animation-iteration-count": "2"})
    generator.add_rule(".animate-infinite", {"animation-iteration-count": "infinite"})
    
    # Animation direction
    generator.add_rule(".animate-normal", {"animation-direction": "normal"})
    generator.add_rule(".animate-reverse", {"animation-direction": "reverse"})
    generator.add_rule(".animate-alternate", {"animation-direction": "alternate"})
    
    # Animation fill mode
    generator.add_rule(".animate-fill-none", {"animation-fill-mode": "none"})
    generator.add_rule(".animate-fill-forwards", {"animation-fill-mode": "forwards"})
    generator.add_rule(".animate-fill-backwards", {"animation-fill-mode": "backwards"})
    generator.add_rule(".animate-fill-both", {"animation-fill-mode": "both"})
    
    # Animation play state
    generator.add_rule(".animate-paused", {"animation-play-state": "paused"})
    generator.add_rule(".animate-running", {"animation-play-state": "running"})
    
    # Hover animations
    generator.add_rule(".hover\\:animate-pulse:hover", {
        "animation": "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite"
    })
    
    generator.add_rule(".hover\\:animate-bounce:hover", {
        "animation": "bounce 1s infinite"
    })
    
    generator.add_rule(".hover\\:animate-shake:hover", {
        "animation": "shake 0.5s ease-in-out"
    })
