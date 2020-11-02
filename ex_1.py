import sys

import numpy as np
import scipy.io.wavfile

sample, centroids = sys.argv[1], sys.argv[2]
fs, y = scipy.io.wavfile.read(sample)
x = np.array(y.copy())
centroids = np.loadtxt(centroids)

new_values = ""

scipy.io.wavfile.write("compressed.wav", fs, np.array(new_values, dtype=np.int16))
