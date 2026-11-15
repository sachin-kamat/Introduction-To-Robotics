from hcsr04 import HCSR04
from machine import Pin,PWM
from time import sleep
import time

sg90 = PWM(Pin(15, mode=Pin.OUT))
sg90.freq(50)
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

def set_servo_angle(angle):
  # Convert 0-180 degrees to pulse width (in microseconds)
  # 0 deg = ~500 us (0.5ms), 180 deg = ~2500 us (2.5ms)
  # 90 deg = ~1500 us (1.5ms)
  min_us = 500
  max_us = 2500
  pulse_us = min_us + (angle / 180.0) * (max_us - min_us)

  # Convert microseconds to duty_u16 (0 to 65535 for a 20000 us period at 50Hz)
  duty_u16 = int((pulse_us / 20000.0) * 65535)
  sg90.duty_u16(duty_u16)

def set_servo_us(us):
    # 20000 us is the 50Hz period (1/50s = 20ms)
    #duty = int((us / 20000) * 65535)
    sg90.duty(us)

def set_servo_pulse(pulse_us):
  # Convert pulse width in microseconds to duty_u16 (0 - 65535 for a 20000us period)
  duty = int((pulse_us / 20000) * 65535)
  sg90.duty_u16(duty)
  
def rotate_90_degrees(speed_us=1700, duration_ms=250):
    """
    speed_us: pulse width for movement (e.g., 1700 us for one direction, 1300 us for other)
    duration_ms: time in milliseconds needed to travel roughly 90 degrees
    """
    # 1. Start moving
    set_servo_pulse(speed_us)
    
    # 2. Wait for the estimated time to cover 90 degrees
    time.sleep_ms(duration_ms)
    
    # 3. Stop the servo (neutral pulse width ~1500 us)
    set_servo_pulse(1500)

sg90.duty(0)
#while True:
#    try:
#        distance = sensor.distance_mm()
#        print('Distance: ', distance, 'mm')
#        if (distance < 50):
#            print("distance less than 100 clockwise")
#            rotate_90_degrees(speed_us=1700, duration_ms=250)
#            time.sleep(3)
#        else:
#            print("counter clock-wise")
#            rotate_90_degrees(speed_us=1200, duration_ms=250)
#            time.sleep(1)
            
#        sleep(1)
#    except OSError as e:
#        print("Error")
        
        
gate = 0 # 0 == closed , 1 == open

def is_car_detected():
    print(f"{sensor.distance_mm()=}")
    if sensor.distance_mm() < 5:
        return True
    return False

def open_gate():
    # open
    global gate
    gate = 1
    print("counter clock-wise")
    rotate_90_degrees(speed_us=1200, duration_ms=250)
    time.sleep(5)
    
    
def close_gate():
    # close
    global gate
    gate = 0
    print("clock-wise")
    rotate_90_degrees(speed_us=1700, duration_ms=250)
    time.sleep(5)
    
    
while True:
    try:
        print(f"car detected {is_car_detected()} and {gate=}")
        car_detected = is_car_detected()
        #if car_detected and gate == 0:
        #    open_gate()
        
        #if not car_detected and gate == 1:
        #    close_gate()
        time.sleep(5)
    except OSError as e:
        print(f"Error detected {e}")


        
        
        
        
