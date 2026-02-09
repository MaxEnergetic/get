import RPi.GPIO as gpio
import time
import random as r


gpio.setmode(gpio.BCM)

leds = [24, 22, 23, 27, 17, 25, 5, 16]

gpio.setup(leds, gpio.OUT)

state=0
period = 0.5
i=0
led=0
flag=True

gpio.output(leds,0)

while flag:

    for led in leds:
        print(led)
        gpio.output(led,1)
        time.sleep(period)
        gpio.output(led,0)

    for led in reversed(leds):
        print(led)
        gpio.output(led,1)
        time.sleep(period)
        gpio.output(led,0)
