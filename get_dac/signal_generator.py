import numpy as np
import time
def get_sin_wave_amplitude(freq, t):

    value = np.sin(2 * np.pi * freq * t)
    shifted = value + 1
    normalized = shifted / 2
    return normalized

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)

import numpy as np

def triangle_signal(freq, t):

    value= 2 * np.abs(2 * (freq * t - np.floor(freq * t + 0.5))) - 1
    shifted = value + 1
    normalized = shifted / 2
    return normalized