import pwm_dac as pw
import signal_generator as sg
import time

t = 0
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 50
try:
    dac = PWM_DAC(12, 500, 3.183, True)
    freq = 5  
    sampling_frequency = 50  
    t = 0.0

    while True:
        amp = sg.triangle_signal(freq, t)    
        voltage = amp * dac.dynamic_range
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    dac.deinit()
