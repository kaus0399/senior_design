from gpiozero import LED, Button
from scipy.signal import butter, lfilter
from scipy.io.wavfile import write
import time
import RPi.GPIO as GPIO
import sounddevice as sd


class Microphone(object):
    def __init__(self, name: str, time: int, lc: int, hc: int, fs: int, order: int, pin: int, status=False):
        self.time = time
        self.pin = pin
        self.status = status
        self.name = name

    # rate at which analog converts to digital

    def butter_bandpass(self, lc: int, hc: int, fs: int, order: int):
        # lc, hc, fs, order=5
        nyq = 0.5 * self.fs
        low = self.lc / nyq
        high = self.hc / nyq
        b, a = butter(self.order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self):
        # data, lc, hc, fs, order=5
        b, a = self.butter_bandpass(self.lc, self.hc, self.fs, order=self.order)
        y = lfilter(b, a, data)
        return y

    def record(self, button):
        GPIO.setwarnings(False) # Set Warnings to False
        GPIO.setmode(GPIO.BCM) # Set Pin-Mode
        micro_pin = GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set Pin for microphone
        myrecording = sd.rec(int(self.time * self.fs), samplerate=self.fs, channels=2) #Recording
        sd.wait()
        write(self.name, self.fs, myrecording)  # Save as WAV file 


    def filter(self)
        
            #     # b, a = signal.butter(4, 100, 'low', analog=True)
            #     # w, h = signal.freqs(b, a)
            #     #scipy.io.wavfile.write(self.time.wav, )

            #     # Process output and then save Audio to SD card as date_time_self.name.wav
            # else:
            #     raise Exception('Audio not recording' + str(self.name))


    # T = 0.05
    # nsamples = T * fs
    # t = np.linspace(0, T, nsamples, endpoint=False)
    # a = 0.02
    # f0 = 600.0
    # x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    # x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    # x += a * np.cos(2 * np.pi * f0 * t + .11)
    # x += 0.03 * np.cos(2 * np.pi * 2000 * t)
    # plt.figure(2)
    # plt.clf()
    # plt.plot(t, x, label='Noisy signal')
    #
    # y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)

    # def print_time(self):
    #     print(self.time)
    #     print(self.status)

# class Button(object):
#     def __init__(self, status):
#         self.time = time
#         self.status = False


# #Object : Microphone
# Time
# Frequency (lc,hc)
# Measurement
# Processsing
# Status: False
# if TImer == 0 .. set True


# #Button Object
# Boolean (Button) True or False
# Track status of boolean


# While at least one microphone False:
#     Keep going

# If all microphones True:
#     terminate
