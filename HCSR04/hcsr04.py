"""
Micropython module for HC-SR04 ultrasonic ranging module.
Compatible with ESP8266.
Based on work of Euter2:
https://github.com/Euter2/MicroPython/blob/master/ultrasonic.py
"""
from machine import Pin, time_pulse_us
from time import sleep_us


class HCSR04:
    """HC-SR04 ultrasonic ranging module class."""

    def __init__(self, trig_Pin, echo_Pin):
        """Initialize Input(echo) and Output(trig) Pins."""
        self._trig = Pin(trig_Pin, Pin.OUT)
        self._echo = Pin(echo_Pin, Pin.IN)
        self._sound_speed = 340  # m/s

    def _pulse(self):
        """Trigger ultrasonic module with 10us pulse."""
        self._trig.high()
        sleep_us(10)
        self._trig.low()

    def distance(self):
        """Measure pulse length and return calculated distance [m]."""
        self._pulse()
        try:
            pulse_width_s = time_pulse_us(self._echo, Pin.high, 30000) / 1000000
        except OSError:
            # Measurement timed out
            return None

        dist_m = (pulse_width_s / 2) * self._sound_speed
        return dist_m

    def calibration(self, known_dist_m):
        """Calibrate speed of sound."""
        self._sound_speed = known_dist_m / self.distance() * self._sound_speed
        print("Speed of sound was successfully calibrated! \n" +
              "Current value: " + str(self._sound_speed) + " m/s")
