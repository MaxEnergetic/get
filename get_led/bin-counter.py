import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

up = 1
down = 2
gpio.setup([up, down], gpio.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if gpio.input(up):
        if num < 255:
            num += 1
        print(num, dec2bin(num))
        gpio.output(leds, dec2bin(num))
        time.sleep(sleep_time)

    if gpio.input(down):
        if num > 0:
            num -= 1
        print(num, dec2bin(num))
        gpio.output(leds, dec2bin(num))
        time.sleep(sleep_time)
