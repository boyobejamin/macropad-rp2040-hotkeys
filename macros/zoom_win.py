# Zoom Hotkeys (Win)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Zoom (Win)', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio', [Keycode.CONTROL, Keycode.SHIFT, Keycode.W]),
        (0x000754, 'Chat', [Keycode.CONTROL, Keycode.SHIFT, Keycode.R]),
        (0x04541B, 'Video', [Keycode.CONTROL, Keycode.SHIFT, Keycode.V]),
        # 2nd row ----------
        (0x002000, 'Share', [Keycode.CONTROL, Keycode.SHIFT, Keycode.S]),
        (0x000754, 'People', [Keycode.CONTROL, Keycode.SHIFT, Keycode.R]),
        (0x000754, 'Leave', [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
        # 3rd row ----------
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (0x000754, 'Participants', [Keycode.CONTROL, Keycode.SHIFT, Keycode.U]),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        # 4th row ----------
        (0x200000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}
