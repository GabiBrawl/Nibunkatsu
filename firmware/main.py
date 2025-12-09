import board
import busio
import os
import digitalio

from kb import NibunkatsuOne
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData

# Initialize the keyboard from our kb.py class
keyboard = NibunkatsuOne()

# --- 1. Determine Side from GPIO10 ---
# If GPIO10 is connected to GND, it's the left side; otherwise, right side
side_pin = digitalio.DigitalInOut(board.IO10)
side_pin.direction = digitalio.Direction.INPUT
side_pin.pull = digitalio.Pull.UP
is_left = not side_pin.value  # Low if connected to GND (left), high otherwise (right)

keyboard.split.split_side = SplitSide.LEFT if is_left else SplitSide.RIGHT

# --- 2. Modules & Extensions ---
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# --- 3. RGB Setup (Under the keys) ---
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=28,
    val_limit=150,     # Limit brightness (max 255) to save power
    hue_default=160,   # Cyan/Blue-ish
    sat_default=255,
    val_default=120,
    animation_speed=1,
)
keyboard.extensions.append(rgb)

# --- 4. OLED Setup (Vertical Display with Custom Graphics) ---
def render_oled(display, keyboard):
    """Custom OLED render function for vertical display"""
    # Clear display
    display.fill(0)
    
    # Get current layer name
    layer_names = ["BASE", "NUM", "NAV"]
    current_layer = layer_names[keyboard.active_layers[0]] if keyboard.active_layers else "BASE"
    
    # Display layout for vertical OLED (64x128)
    display.text("LAYER", 0, 0, 1)
    display.text(current_layer, 0, 12, 1)
    
    # Add some visual separator
    display.hline(0, 24, 64, 1)
    
    # Show keyboard info at bottom
    display.text("Nibunkatsu", 0, 100, 1)
    display.text("One", 0, 112, 1)
    
    # Optional: Show keypress indicator or other status
    # This could be expanded with more features
    
    display.show()

oled_ext = Oled(
    toDisplay=OledDisplayMode.GFX,
    oled_render=render_oled,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# --- 5. Keymap ---
# Define your layers here. 
# 4 Rows x 6 Cols = 24 keys per half -> 48 keys total
# KMK maps them: [L1..L24, R1..R24]

keyboard.keymap = [
    # LAYER 0: Base (QWERTY-ish)
    [
        # --- LEFT HAND ---
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        KC.NO,   KC.NO,   KC.LGUI, KC.LALT, KC.MO(1), KC.SPC,

        # --- RIGHT HAND ---
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
        KC.SPC,  KC.MO(2),KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, 
    ],
    
    # LAYER 1: Numbers (Momentary)
    [
        # Left
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # Right
        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    ],

    # LAYER 2: Navigation / Media
    [
        # Left
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # Right
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.NO,   KC.NO,
        KC.MUTE, KC.VOLD, KC.VOLU, KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    ]
]

if __name__ == '__main__':
    keyboard.go()