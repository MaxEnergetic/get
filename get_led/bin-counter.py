import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
leds = [24, 22, 23, 27, 17, 25, 5, 16]
gpio.setup(leds, gpio.OUT)
num = 0
up=1
down=2
gpio.setup([up,down], gpio.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if gpio.input(up)>0:
        if num +1 <= 7:
            num+=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        GPIO.output(leds, dec2bin(num))

    if gpio.input(down)>0:
        if num +1 >= 0:
            num-=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        GPIO.output(leds, dec2bin(num))
