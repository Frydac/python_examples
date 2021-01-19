#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

# To get an idea of what these coefficients represent.

# example
#  coeffs.b0: -0.119712
#  coeffs.b1: 0
#  coeffs.b2: 0.119712
#  coeffs.a1: -2.21673
#  coeffs.a2: 1.23942

b = [-0.119712, 0, 0.119712]
a = [1, -2.21673, 1.23942]
sample_rate = 44100

# docs: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html
w, h = signal.freqz(b, a)
print("█ h:")
print(h)

# w is in radians in [0, pi]
w_freq = w / math.pi * sample_rate/2

fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w_freq, 20 * np.log10(abs(h)), 'b')
ax1.set_xlabel('Frequency with sample rate {}'.format(sample_rate))
ax1.set_ylabel('Amplitude [dB]', color='b')

# originally plotter with radians
#  ax1.plot(w, 20 * np.log10(abs(h)), 'b')
#  ax1.set_xlabel('Frequency [radians/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w_freq, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')

# logscale on x axis
plt.semilogx()

plt.show()


