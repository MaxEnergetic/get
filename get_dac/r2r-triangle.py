import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


class R2R_DAC:

    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        if not (0 <= number <= 255):
            print("Число выходит за диапазон (0-255). Устанавливаем 0.")
            number = 0
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]

        if self.verbose:
            print(f"Number: {number} -> Bits: {bits}")

        GPIO.output(self.gpio_bits, bits)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за диапазон (0 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0 В")
            voltage = 0.0
        number = int(voltage / self.dynamic_range * 255)
try:
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    dynamic_range = 3.183
    freq=5
    sampling_frequency=50
    t=0
    while True:
        amp = sg.triangle_signal(freq, t)    
        voltage = amp * dynamic_range
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_freq)
        t += 1.0 / sampling_freq
finally:
    dac.deinit()
    print("DAC deinitialized")