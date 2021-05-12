# import pyaudio
# p = pyaudio.PyAudio()
# for ii in range(p.get_device_count()):
#     print(p.get_device_info_by_index(ii).get('name'))


import pyaudio
import wave
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import scipy.io.wavfile
import scipy.signal
from scipy.io.wavfile import write

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 48000 # 44.1kHz sampling rate
chunk = 2048 # 2^12 samples for buffer
record_secs = 10 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'rahul_lung_unfiltered.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk,False)
    frames.append(data)
time.sleep(0.5)

print("finished recording 1")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

time.sleep(2)

# data = np.array(frames, dtype = int16)
_, data = read('rahul_lung_unfiltered.wav')

duration = len(data)/samp_rate
time = np.arange(0,duration,1/samp_rate) #time vector

plt.figure(1)
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('rahul_lung_unfiltered.wav')
plt.savefig('rahul_lung_unfiltered.png')



sampleRate, data = scipy.io.wavfile.read('rahul_lung_unfiltered.wav')
times = np.arange(len(data))/sampleRate

b, a = scipy.signal.butter(3, [60/(0.5*sampleRate), 600/(0.5*sampleRate)], 'bandpass')
filteredBandPass = scipy.signal.lfilter (b, a, data)
filteredBandPass = filteredBandPass.astype('float64')
filteredBandPass /= np.max(np.abs(filteredBandPass),axis=0)


plt.figure(2)
plt.plot(times, filteredBandPass)
plt.title("Filtered Rahul Lung Bandpass")
plt.margins(0, .05)
plt.tight_layout()
plt.savefig('Filtered Rahul Lung Bandpass.png')


write('rahul_lung_filtered.wav', sampleRate, filteredBandPass )