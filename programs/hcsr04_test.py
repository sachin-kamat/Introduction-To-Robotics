from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

while True:
    distance_cm = sensor.distance_cm()
    distance_mm = sensor.distance_mm()
    print(f"{distance_cm=} , {distance_mm=}")
    sleep(1)
