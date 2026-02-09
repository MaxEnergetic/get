import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led=26

gpio.setup(led, gpio.OUT)

state=0
period = 0.5
i=0

flag=True

while flag:
    state = not state 
    gpio.output(led,state)
    time.sleep(period)
    print(i)
    i+=0.5