import time
from neopixel import Neopixel
from machine import Pin

PIXEL_COUNT = 30
LIGHT_MINUTES = 3

pixels = Neopixel(PIXEL_COUNT, 0, 0, "GRB")
pir = Pin(1, Pin.IN, Pin.PULL_DOWN)

WHITE = (255, 255, 255)
OFF = (0, 0, 0)
SLEEP_TIME = 60 * LIGHT_MINUTES

pixels.brightness(100)
pixels.fill(OFF)
pixels.show()

while True:
    if pir.value():
        pixels.fill(WHITE)
        pixels.show()
        time.sleep(SLEEP_TIME)
        pixels.fill(OFF)
        pixels.show()
    time.sleep(1)
