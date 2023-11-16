# Neo Trinkandle: 2023 Glenn Jones

"""
bundle library:Ladafruit-circuitpython-bundle-8.x-mpy-20231115.zip
firmware: adafruit-circuitpython-neopixel_trinkey_m0-en_GB-8.2.7.uf2

Realistic NeoPixel candle effect on your Adafruit Neo Trinkey

Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy

Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
import random
import touchio
from rainbowio import colorwheel

num_pixels = 4

#pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.3, auto_write=False)
pixels.brightness += 0.1


RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
PINK = (248, 144, 231)

VPURPLE = (164, 83, 245)
VBLUE = (143, 140, 243)
VGREEN = (102, 184, 193)
VPINK = (251, 108, 255)
VORANGE = (225, 123, 25)

color = 0

RANDOMCOL = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# num1 = random.randint(0, 255)

# touch_A1 = touchio.TouchIn(board.TOUCH1)  # Not a touch pin on Trinket M0!
# touch_A2 = touchio.TouchIn(board.TOUCH2)  # Not a touch pin on Trinket M0!

def rainbow(color_index):
    for pixel in range(4):
        pixel_index = (pixel * 256 // 4) + color_index
        pixels[pixel] = colorwheel(pixel_index & 255)
    pixels.show()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)



def candle_effect1():
    while True:
        flicker = random.randint(1, 50)  # Random flicker value

        # Set NeoPixel color with some random flicker
        pixels.fill((255 - flicker, 150 - flicker, 20 - flicker))
        pixels.show()

        time.sleep(0.1)  # Adjust the sleep duration to control the flicker speed
def fade_color(color, step):
    return tuple(max(0, value - step) for value in color)

def candle_effect2():
    while True:
        flicker = random.randint(5, 20)  # Random flicker value

        # Set NeoPixel color with fading effect
        for i in range(255, 0, -flicker):
            pixels.fill(fade_color((255, 150, 20), i))
            pixels.show()
            time.sleep(0.02)

        time.sleep(random.uniform(0.1, 0.5))  # Adjust the sleep duration to control the flicker speed

def fade_color(color, step):
    return tuple(max(0, value - step) for value in color)

def candle_effect3():
    while True:
        flicker = random.randint(5, 20)  # Random flicker value

        # Fading effect
        for i in range(255, 0, -flicker):
            pixels.fill(fade_color((255, 150, 20), i))
            pixels.show()
            time.sleep(0.02)

        # Random flickering
        flicker = random.randint(1, 10)
        for _ in range(flicker):
            pixels.fill((255, 150, 20))
            pixels.show()
            time.sleep(random.uniform(0.01, 0.1))

        time.sleep(random.uniform(0.1, 0.5))  # Adjust the sleep duration to control the flicker speed

def candle_effect4():
    while True:
        flicker = random.randint(5, 20)  # Random flicker value

        # Fading effect with pixel index variation
        for i in range(num_pixels):
            intensity = random.randint(0, 255)
            pixels[i % num_pixels] = fade_color((255, 150, 20), intensity)
            pixels.show()
            time.sleep(0.02)

        # Random flickering
        flicker = random.randint(1, 10)
        for _ in range(flicker):
            pixels.fill((255, 150, 20))
            pixels.show()
            time.sleep(random.uniform(0.01, 0.1))

        time.sleep(random.uniform(0.1, 0.5))  # Adjust the sleep duration to control the flicker speed

while True:
    candle_effect4()
    #time.sleep(random.randint(0, 5))
    #candle_effect2()
    #time.sleep(random.randint(0, 5))
    """
    num1 = random.randint(0, 255)
    num2 = random.randint(0, 255)
    num3 = random.randint(0, 255)
    
    pixels.brightness = 0.1
    color = color + 1
    if color > 255:
        color = 0
    rainbow(color)
    time.sleep(random.randint(0, 2))
    #rainbow_cycle(0.1)
    #time.sleep(1)
    pixels.fill((num1, num2, num3))
    time.sleep(random.randint(0, 2))
    pixels.fill((0, 0, 0))
    time.sleep(random.randint(0, 1))
    """
