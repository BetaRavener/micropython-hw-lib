"""
Temperature Monitoring using MAX6675 with ESP32  
Author: Er-Rajas  
Description:  
This script continuously reads temperature from the MAX6675 thermocouple sensor  
and prints the values over serial. Designed for MicroPython on ESP32.  

Adjust the delay on line 24 as needed: `time.sleep([desired_delay])`
  
"""

from max6675 import MAX6675
from machine import Pin
import time

so = Pin(12, Pin.IN)
sck = Pin(2, Pin.OUT)
cs = Pin(14, Pin.OUT)
sensor = MAX6675(sck, cs, so)
try:
    while True:
        temperature = sensor.read()
        print("Temperature: {:.2f} °C".format(temperature))
        time.sleep(1)  # adjust delay (in seconds) as needed

except KeyboardInterrupt:
    print("\nStopped by user.")