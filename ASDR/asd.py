import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt

samplerate, data = sio.wavfile.read('kick.wav')

times = np.arange(len(data))/float(samplerate)

print('sampling rate: ', samplerate)
print('time : ', times[-1])


plt.xlim(times[0], times[-1])
plt.plot(times, data)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.savefig('exam.png')
plt.show()
