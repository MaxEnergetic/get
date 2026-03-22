import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

import RPi.GPIO as GPIO
import time


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