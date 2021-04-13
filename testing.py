# Connect GPIO18 to positive on the IoT relay, connect ground from Pi to ground on relay.

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print("CTRL+C to stop testing")

while 1 == 1:
    GPIO.output(18,GPIO.HIGH) # Toggle relay on.
    time.sleep(5)
    GPIO.output(18,GPIO.LOW) # Toggle relay off.
    time.sleep(5)
