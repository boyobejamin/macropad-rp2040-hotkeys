# Discord

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Discord (Win)', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'Mute', [Keycode.CONTROL, Keycode.OPTION, Keycode.M]),
        (keyconfig.LED_BLANK, 'Reply', ['r']),
        (keyconfig.LED_BLANK, 'SS', [Keycode.CONTROL, Keycode.SHIFT, Keycode.V]),
        # 2nd row ----------
        (keyconfig.LED_BLANK, 'VAD', [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
        (keyconfig.LED_BLANK, 'Upld', [Keycode.CONTROL, Keycode.SHIFT, 'm']),
        (0x04541B, 'PTT', ['d']),
        # 3rd row ----------
        (keyconfig.LED_BLANK, 'Def', [Keycode.CONTROL, Keycode.SHIFT, 'd']),
        (keyconfig.LED_BLANK, 'Acc', [Keycode.CONTROL, Keycode.ENTER]),
        (keyconfig.LED_BLANK, 'Dec', [Keycode.ESCAPE]),
        # 4th row ----------
        (0x000754, 'Emoji', [Keycode.CONTROL, 'e']),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}
