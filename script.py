import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('1st_String_E_64Kb.wav')
fft_out = fft(data)
plt.plot(data, np.abs(fft_out))
plt.show()