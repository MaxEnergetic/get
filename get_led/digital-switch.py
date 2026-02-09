import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
b=13
gpio.setup(b, gpio.IN)

status = 0
led = 26
flag=True
i=0
gpio.setup(led,gpio.OUT)
gpio.output(led, status )
while flag:
    if gpio.input(b):
        status = not status
        gpio.output(led,status)
        time.sleep(0.2)
        i+=1

        print(i)