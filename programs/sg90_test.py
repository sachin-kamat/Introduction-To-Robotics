from machine import Pin,PWM
import time
sg90 = PWM(Pin(15, mode=Pin.OUT))
sg90.freq(50)

def set_servo_pulse(pulse_us):
  # Convert pulse width in microseconds to duty_u16 (0 - 65535 for a 20000us period)
  global sg90
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
    

  
while True:
    print("counter-clockwise")
    rotate_90_degrees(speed_us=1800, duration_ms=300)
    time.sleep(5)

    print("clockwise")
    rotate_90_degrees(speed_us=1200, duration_ms=300)
    time.sleep(5)
    
