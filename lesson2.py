import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sp

fs = 1000
t = np.arange(0, 1, 1/fs)

f = 50
sig = np.sin(2*np.pi*f*t)
noise = np.random.randn(len(t)) * 0.5

noisy = sig + noise

numtaps = 11
cutoff = 100

filter = sp.firwin(numtaps, cutoff, fs=fs)
# sp.firwin(): designs a Finite Impulse Response (FIR) low-pass filter
# numtaps: how many coefficients (taps) the filter has
# cutoff: the frequency in Hz where the filter starts cutting
# fs=fs: tells the function what your sampling rate is so it can scale correctly
# returns h: an array of filter coefficients

filtered = sp.lfilter(filter, 1, noisy)
#sp.lfilter(): applies a digital filter to a signal
# h: the filter coefficients we just designed (numerator)
# 1.0: denominator — for FIR filters this is always 1.0
# noisy: the input signal we want to filter
# returns: the filtered output signal

plt.figure(figsize=(10,4))
plt.plot(t[:200], sig[:200], label = "clean")
plt.plot(t[:200], noisy[:200], label = "noisy")
plt.plot(t[:200], filtered[:200], label = "filtered")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("clean, noisy and filtered signal")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

fft = np.fft.fft(sig)
fft_n = np.fft.fft(noisy)
fft_filtered = np.fft.fft(filtered)

freq = np.fft.fftfreq(len(t), 1/fs)

plt.figure(figsize=(10,4))
plt.plot(freq, np.abs(fft), label ="clean")
plt.plot(freq, np.abs(fft_n), label="noisy")
plt.plot(freq, np.abs(fft_filtered), label = "filtered")
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()


#numtaps
#order?
#filter characteritics


#plt.xticks(100, 200, 300, 400, 500, 600) 
