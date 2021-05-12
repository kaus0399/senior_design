from scipy.signal import butter, lfilter
import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write

# # read ECG data from the WAV file
# sampleRate, data = scipy.io.wavfile.read('Kaus_1_NF.wav')
# times = np.arange(len(data))/sampleRate

# # apply a 3-pole lowpass filter at 0.1x Nyquist frequency
# b, a = scipy.signal.butter(3, 0.1)
# filtered = scipy.signal.filtfilt(b, a, data)

# for order in [3, 6, 9]:
#         b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#         w, h = freqz(b, a, worN=2000)







def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    # fs = 44100.0
    lowcut = 20.0
    highcut = 200.0

    # Plot the frequency response for a few different orders.
    # plt.figure(1)
    # plt.clf()
    # for order in [3, 6, 9]:
    #     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    #     w, h = freqz(b, a, worN=2000)
    #     plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    # plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
    #          '--', label='sqrt(0.5)')
    # plt.xlabel('Frequency (Hz)')
    # plt.ylabel('Gain')
    # plt.grid(True)
    # plt.legend(loc='best')

    # Filter a noisy signal.
    # T = 0.05
    # nsamples = int(T * fs)
    # a = 0.02
    # f0 = 600.0
    # x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    # x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    # x += a * np.cos(2 * np.pi * f0 * t + .11)
    # x += 0.03 * np.cos(2 * np.pi * 2000 * t)


    fs, x = read('Kaus_1_NF.wav')
    duration = len(x)/fs
    t = np.arange(0,duration,1/fs)
    plt.figure(2)
    plt.clf()
    plt.plot(t, x, label='Noisy signal')
    plt.savefig('noise.png')




    y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
    plt.plot(t, y, label='Filtered signal') #(%g Hz)')
    plt.xlabel('time (seconds)')
    plt.savefig('filtered.png')
    # plt.hlines([-a, a], 0, T, linestyles='--')
    # plt.grid(True)
    # plt.axis('tight')
    # plt.legend(loc='upper left')



run()