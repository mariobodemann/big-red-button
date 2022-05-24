import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

big_button = digitalio.DigitalInOut(board.A0)
big_button.direction = digitalio.Direction.INPUT
big_button.pull = digitalio.Pull.DOWN

big_lights = digitalio.DigitalInOut(board.A1)
big_lights.direction = digitalio.Direction.OUTPUT
big_lights.value = False

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def blink():
    for i in range(0, 25):
        big_lights.value = (i % 2 == 0)
        time.sleep(0.05)

print("Waiting for button ...")

blink()

while True:
    if big_button.value:
        print("PRESSED")
        keyboard.press(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
        keyboard.release_all()
        keyboard.press(Keycode.COMMAND, Keycode.SHIFT, Keycode.M)
        keyboard.release_all()
        blink()

    big_lights.value = False
    time.sleep(0.1)
