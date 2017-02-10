# Demonstation of HCSR04
# Following code periodicaly measures the distance using HCSR04 sensor
# and trigers LED if an object was measured closer than specified
# distance threshold.

from hcsr04 import HCSR04
import time
from machine import Pin

# Parameters
trig_pin_no = 14
echo_pin_no = 13
led_pin_no = 4
max_dist = 2  # Maximum distance that will triger LED (in meters)
led_time = 1  # Time for which the LED stays lit (in seconds)

# Initialization
led = Pin(led_pin_no, Pin.OUT)
s = HCSR04(trig_pin_no, echo_pin_no)
start = None

# Infinite loop, kill with Ctrl-C
while True:
    # Measure the distance
    d = s.distance()
    
    # If the sensor itself is reporting something in range and its closer
    # than max_dist, triger the LED
    if d is not None and d < max_dist:
        led.high()  # Lit up LED
        start = time.ticks_ms()  # Save trigger time 
        print(d)  # Prints the distance that trigerred LED

    # Check if the LED is still lit and if so, check the timeout
    if start is not None and time.ticks_diff(time.ticks_ms(), start) > led_time * 1000:
        led.low()  # Turn off LED
        start = None  # Null the triger time => LED is off

    # Optional sleep to make terminal easier to read and prevent 
    # buffer congestion.
    time.sleep(0.1)
