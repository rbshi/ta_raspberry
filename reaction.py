import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
GPIO.setup(led, GPIO.OUT)

left_button = 14
right_button = 15

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led, 0)
time.sleep(random.uniform(1,5))
GPIO.output(led, 1)

while True:
    if(GPIO.input(14)) == False:
        print('left player wins!')
        break
    if(GPIO.input(15)) == False:
        print('right player wins!')
        break
GPIO.cleanup()
