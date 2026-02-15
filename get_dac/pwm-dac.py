import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose


        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за диапазон (0 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0 В")
            voltage = 0.0
        number = int(voltage / self.dynamic_range * 255)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        dynamic_range = 3.183
        freq=5
        sampling_frequency=50
        while True:
            amp = sg.get_sin_wave_amplitude(freq, t)    
            voltage = amp * dynamic_range
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_freq)
            t += 1.0 / sampling_free
    finally:
        dac.deinit()