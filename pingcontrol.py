import platform
import subprocess
import time
import RPi.GPIO as GPIO


# Input the actual IP you want to monitor here:
ip = "1.2.3.4"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


def ping_ip(ip):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', ip), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:
        return False


while 1 == 1:
    if ping_ip(ip):
        GPIO.output(18,GPIO.HIGH)
    else:
        # Wait 10 seconds and ping again to check for false negative.
        time.sleep(10)
        if ping_ip(ip):
            pass
        else:
            GPIO.output(18,GPIO.LOW)
    # Number of seconds you want program to halt before next check.
    time.sleep(10)
