import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage import io


#ιστόγραμμα της εικόνας
img = io.imread("/home/katerina/Documents/python/image4.jpg")
h = np.histogram(img,bins=256)
cdf = np.zeros(256)
for x in range(256):
    cdf[x] += cdf[x-1] + h[0][x]
fig=plt.figure()
plt.plot(h[0])
plt.show()
plt.savefig("/home/katerina/Documents/python/image4_h.jpg")


