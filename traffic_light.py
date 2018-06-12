import  RPi.GPIO    as  GPIO
import  time
import RPi.GPIO as GPIO
import time

red_led =   3
green_led   =   4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led,   GPIO.OUT)
#   Define  a   function    to  control the traffic light
def light_state(red_state,  green_state):
    GPIO.output(red_led,    red_state)
    GPIO.output(green_led,  green_state)
print("Traffic    Light   Simulation")

#   Main    loop
try:
    while   True:
        #   starts  at  Green   light
        light_state(0,  1)

        time.sleep(5)
        #   blink   the Green   light
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        #   change  to  Red light
        light_state(1,  0)
        time.sleep(5)
except  KeyboardInterrupt:
    print("Ctrl+C pressed.    Terminating...")
finally:
    GPIO.cleanup()
    print("GPIO   pins    cleaned up  successfully.")
