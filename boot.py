import time
from neopixel import NeoPixel
from machine import Pin

PIXEL_COUNT = 16
LIGHT_MINUTES = 3
PIXEL_PIN = Pin(0)
MOTION_DETECTION_PIN = 1

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
motion = Pin(MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

WHITE = (255, 255, 255)
OFF = (0, 0, 0)
SHINE_TIME = 60 * LIGHT_MINUTES

pixels.fill(OFF)
pixels.write()

while True:
    if motion.value():
        pixels.fill(WHITE)
        pixels.write()
        time.sleep(SHINE_TIME)
        pixels.fill(OFF)
        pixels.write()
    time.sleep(1)
