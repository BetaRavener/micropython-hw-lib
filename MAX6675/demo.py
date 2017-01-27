from max6675 import MAX6675
from machine import Pin
import time

so = Pin(12, Pin.IN)
sck = Pin(14, Pin.OUT)
cs = Pin(16, Pin.OUT)

max = MAX6675(sck, cs , so)

for _ in range(10):
    print(max.read())
    time.sleep(1)