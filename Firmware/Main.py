import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledData
from kmk.modules.encoder import RotaryTracker
from kmk.modules.mouse_keys import MouseKeys
keyboard = KMKKeyboard()
 #keyboard matrix

 keyboard. row_pins = (board.D8, board.D9, board.D10)
 keyboard. col_pins = (board.D5, board.D6, board.D7)
 keyboard.diode_orientation = DiodeOrientation.COL2ROW
 #oled screen

 i2c_bus = busio.I2C(board.D3, board.D2)
 def  custom_oled_text():
     lines = [
     "   HACKPAD V1  ",
     "---------------",
     f"layer: {keyboard.active_layers[0]}",
     "status: active"
     ]
     return lines
 oled_ext = Oled(
     OledData(image_train=['kmk/extensions/peg_oled_display/kmk.bmp']),
     to_display=OledDisplayMode.TXT,
     flip=False,
     entries_toast=custom_oled_text,
     )
oled_ext.i2c = i2c_bus
keyboard.extensions.append(oled_ext)
#rotary encoder stuffs

encoder_tracker = RotaryTracker()
keyboard.modules.append(encoder_tracker)
encoder_tracker.pins = ((board.D13, board.D11, board.D12),)
#keymap stuffs

keyboard.keymap = [
     [
     KC.LGUI(KC.LSFT(KC.S)),  KC.PRSC,  KC.ESC,

     KC.LSFT,             KC.LALT(KC.F4),   KC.MB_BTN4,

     KC.Q,                    KC.E,        KC.L,
    ]
    ]
#encoder actions

encoder_tracker.map = [ ((KC.VOLD, KC.VOLU, KC.MUTE),) ]
#START KEYBOARD

if __name__ == '__main__' :
    keyboard.go()










