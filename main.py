"""CircuitPython Essentials Digital In Out example"""
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

mode = 0

pixel_pin = board.A0
num_pixels = 24
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, 
                           auto_write=False, pixel_order=(1, 0, 2, 3))

RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)
PINK = (255, 102, 178)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3, 0)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3, 0)
 
 
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)
 
 
def rainbow_cycle(wait):
    # for j in range(255):
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels)
        pixels[i] = wheel(rc_index & 255)
    pixels.show()
    time.sleep(wait)

def switchdetect(mode):
    if switch.value:
        led.value = False
    else:
        led.value = True
        mode = (mode + 1)
        time.sleep(0.5)
    return mode
    

while True:

    if mode >= 8:
        mode = 0
    mode = switchdetect(mode)
    if mode == 0: 
        pixels.fill(RED)
        pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    if mode == 1: 
        pixels.fill(YELLOW)
        pixels.show()
    if mode == 2:
        pixels.fill(GREEN)
        pixels.show()
    if mode == 3: 
        pixels.fill(CYAN)
        pixels.show()
    if mode == 4: 
        pixels.fill(BLUE)
        pixels.show()
    if mode == 5: 
        pixels.fill(PURPLE)
        pixels.show()
    if mode == 6: 
        pixels.fill(PINK)
        pixels.show()
    if mode == 7: 
        rainbow_cycle(0.01)  # Increase the number to slow down the rainbow
 