# Discord

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Discord (MacOS)', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'Mute', [Keycode.COMMAND, Keycode.SHIFT, Keycode.M]),
        (keyconfig.LED_BLANK, 'Reply', ['r']),
        (keyconfig.LED_BLANK, 'CC', [Keycode.COMMAND, Keycode.SHIFT, Keycode.OPTION, Keycode.V]),
        # 2nd row ----------
        (keyconfig.LED_BLANK, 'VAD', [Keycode.COMMAND, Keycode.SHIFT, Keycode.OPTION, Keycode.W]),
        (keyconfig.LED_BLANK, 'Upld', [Keycode.COMMAND, Keycode.SHIFT, 'u']),
        (0x04541B, 'PTT', [Keycode.F4]),
        # 3rd row ----------
        (keyconfig.LED_BLANK, 'Def', [Keycode.COMMAND, Keycode.SHIFT, 'd']),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        # 4th row ----------
        (0x000754, 'Emoji', [Keycode.COMMAND, 'e']),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}
