import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

f = 100
sig =np.sin(2*np.pi*f*t)

plt.figure(figsize=(10, 5))
plt.plot(t[:200], sig[:200])
plt.xlabel("time")
plt.ylabel("sine wave")
plt.grid()
plt.tight_layout()
plt.show()

# Why is t created with 1/fs as the step size?
# What does np.arange do differently from Python's range?
# Why do we plot only [:200] samples instead of all 1000?
# What would happen if you changed f = 50 to f = 200? Try it.

noise = np.random.randn(len(t)) * 0.5 #Gaussian noise
noisy_sig = sig + noise

plt.figure(figsize=(10,5))
plt.plot(t[:200], noisy_sig[:200])
plt.xlabel("time")
plt.ylabel("noisy signal")
plt.grid()
plt.tight_layout()
plt.show()

N = len(t)
fft = np.fft.fft(sig)
freqs = np.fft.fftfreq(N, 1/fs)

plt.figure(figsize=(10,4))
plt.plot(freqs, np.abs(fft))
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.title("FFT of clean signal")
plt.grid()
plt.tight_layout()
plt.show()

fft_n = np.fft.fft(noisy_sig)

plt.figure(figsize=(10,4))
plt.plot(freqs, np.abs(fft_n))
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.title("FFT of noisy signal")
plt.grid()
plt.tight_layout()
plt.show()

#frequesncy space = 1/fs ?
#abs(fft) ?
#negative frequency?
