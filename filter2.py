import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('Kaus_1_NF.wav')
times = np.arange(len(data))/sampleRate

b, a = scipy.signal.butter(3, 20/(0.5*sampleRate), 'lowpass')
filteredLowPass = scipy.signal.filtfilt(b, a, data)
filteredLowPass = filteredLowPass.astype('float64')
filteredLowPass /= np.max(np.abs(filteredLowPass),axis=0)

plt.figure(1)
plt.plot(times, filteredLowPass)
plt.title("Filtered Kaus Heartbeat LowPass")
plt.margins(0, .05)
plt.tight_layout()
plt.savefig('lowpass.png')
write('filtered_LP_Kaus_1_NF.wav', sampleRate, filteredLowPass )






b, a = scipy.signal.butter(3, 150/(0.5*sampleRate), 'highpass')
filteredHighPass = scipy.signal.filtfilt(b, a, data)
filteredHighPass = filteredHighPass.astype('float64')
filteredHighPass /= np.max(np.abs(filteredHighPass),axis=0)
# abs_max = np.amax(np.abs(filteredHighPass))
# filteredHighPass /= filteredHighPass * (100.0 / abs_max)

plt.figure(2)
plt.plot(times, filteredHighPass)
plt.title("Filtered Kaus Heartbeat HighPass")
plt.margins(0, .05)
plt.tight_layout()
plt.savefig('highpass.png')
write('filtered_HP_Kaus_1_NF.wav', sampleRate, filteredHighPass )










b, a = scipy.signal.butter(3, [20/(0.5*sampleRate), 150/(0.5*sampleRate)], 'bandpass')
filteredBandPass = scipy.signal.lfilter (b, a, data)
filteredBandPass = filteredBandPass.astype('float64')
filteredBandPass /= np.max(np.abs(filteredBandPass),axis=0)


plt.figure(3)
plt.plot(times, filteredBandPass)
plt.title("Filtered Kaus Heartbeat Bandpass")
plt.margins(0, .05)
plt.tight_layout()
plt.savefig('bandpass.png')


write('filtered_BP_Kaus_1_NF.wav', sampleRate, filteredBandPass )