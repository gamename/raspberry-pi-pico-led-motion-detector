'''
This is a simple example of how to light a strip of ws2812b pixels with the Raspberry Pi Pico using
a motion detector
'''
import time
from neopixel import NeoPixel
from machine import Pin

# How many pixels do we have?
PIXEL_COUNT = 16

# How long should we keep the light on?
LIGHT_MINUTES = 3

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Which pin controls the motion detector?
MOTION_DETECTION_PIN = 1

# Define the color we want to use for the light strip
WHITE = (255, 255, 255)

# Define how we want to turn off the light strip
OFF = (0, 0, 0)

# How long should we stay on after detecting motion?
SHINE_TIME = 60 * LIGHT_MINUTES


def set_color(strip, color):
    '''
    Set the color of the pixel strip
    Args:
        strip (): The pixel strip name
        color (): The color to set

    Returns:
        Nothing
    '''
    strip.fill(color)
    strip.write()


pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
motion = Pin(MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

set_color(pixels, OFF)

while True:
    if motion.value():
        set_color(pixels, WHITE)
        time.sleep(SHINE_TIME)
        set_color(pixels, OFF)
