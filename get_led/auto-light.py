import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
led=26
gpio.setup(led, gpio.OUT)

state=1
period = 0.5
i=0
flag=True

light_detector = 6
gpio.setup(light_detector, gpio.IN)
gpio.output(led,0)

while flag:
    if gpio.input(light_detector):
        gpio.output(led,not gpio.input(light_detector))