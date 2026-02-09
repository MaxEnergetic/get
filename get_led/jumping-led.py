import RPi.GPIO as gpio
import time
import random as r


gpio.setmode(gpio.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

gpio.setup(leds, gpio.OUT)

state=0
period = 0.5
i=0
led=0
flag=True

while flag:
    state = not state 
    led =r.randint(0,7)
    gpio.output(leds[led],state)
    time.sleep(period)
    print(led)
    state = not state
    gpio.output(leds[led],state)