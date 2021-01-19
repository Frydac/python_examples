#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

sample_rate = 48000.0

# impulse on position 0
impulse = np.zeros(512)
impulse[0] = 0.7
fft_impulse = np.fft.fft(impulse)
fft_size = len(fft_impulse)
half = fft_size // 2
scale = 2.0 / fft_size
freq = np.fft.fftfreq(len(impulse), 1/sample_rate)[:half]
fig, ax = plt.subplots(3, 2)
ax[0, 0].plot(impulse)
ax[0, 0].set_title('time impulse at pos 0')
ax[1, 0].plot(freq, scale * np.abs(fft_impulse)[:half])
ax[1, 0].set_title('freq impulse at pos 0')
ax[2, 0].plot(freq, np.angle(fft_impulse)[:half])
ax[2, 0].set_title('phase impulse at pos 0')


#impulse on position 32
impulse = np.zeros(512)
impulse[32] = 0.7
fft_impulse = np.fft.fft(impulse)
freq = np.fft.fftfreq(len(impulse), 1/sample_rate)[:half]
ax[0, 1].plot(impulse)
ax[0, 1].set_title('time impulse at pos 32')
ax[1, 1].plot(freq, scale * np.abs(fft_impulse)[:half])
ax[1, 1].set_title('freq impulse at pos 32')
ax[2, 1].plot(freq, np.angle(fft_impulse)[:half])
ax[2, 1].set_title('phase impulse at pos 32')

plt.show()



