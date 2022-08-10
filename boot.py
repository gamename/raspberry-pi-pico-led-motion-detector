import time
from neopixel import NeoPixel
from machine import Pin

PIXEL_COUNT = 55
LIGHT_MINUTES = 3

pixels = NeoPixel(Pin(0), PIXEL_COUNT)
pir = Pin(1, Pin.IN, Pin.PULL_DOWN)

WHITE = (255, 255, 255)
OFF = (0, 0, 0)
SLEEP_TIME = 60 * LIGHT_MINUTES

pixels.fill(OFF)
pixels.write()

while True:
    if pir.value():
        pixels.fill(WHITE)
        pixels.write()
        time.sleep(SLEEP_TIME)
        pixels.fill(OFF)
        pixels.write()
    time.sleep(1)
