from machine import Pin
import time
from neopixel import NeoPixel

np = NeoPixel(Pin(48), 1)

RED = (255,0,0)
YELLOW = (255, 128, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)


while True:
    np[0] = RED
    np.write()
    time.sleep(1)
    
    np[0] = YELLOW
    np.write()
    time.sleep(1)
    
    # Green light on
    np[0] = GREEN
    np.write()
    time.sleep(1)
    
    np[0] = OFF
    np.write()
    time.sleep(1)
    

