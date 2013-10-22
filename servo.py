#!/usr/bin/env python
#
# Example for Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
# 
# This needs more work. The code for the Humans appears to have gotten a higher priorty.
#

from RPIO import PWM
import time
import RPi.GPIO as GPIO

Servo2Pin=18
SleepTime=1

class Servo:

  def __init__(self):
    self.servo = PWM.Servo()

  def servo_CW(self, angleUS):
    # Set servo on Servo1Pin to 1200us (1.2ms)
    # This rotates the servo CW.
    self.servo.set_servo(Servo2Pin, angleUS)
    time.sleep(SleepTime)
    self.servo.stop_servo(Servo2Pin)
    time.sleep(.25)

  def servo_CCW(self, angleUS):
    # Set servo on Servo1Pin to 2000s (2.0ms)
    # This rotates the servo CounterCW
    self.servo.set_servo(Servo2Pin, angleUS)
    time.sleep(SleepTime)
    # Clear servo on Servo1Pin
    self.servo.stop_servo(Servo2Pin)
    time.sleep(.25)
