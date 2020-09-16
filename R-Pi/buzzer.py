import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.IN)


GPIO.output(3,GPIO.HIGH)
time.sleep(.5)
GPIO.output(3,GPIO.LOW)
time.sleep(.5)
   


