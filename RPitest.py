import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
while(True):
    GPIO.output(27,1)
    print("LED turns on...")
    sleep(1)
    GPIO.output(27,0)
    print("LED turns off...")
    sleep(1)
