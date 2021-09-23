from PIL import Image
import numpy as np
from skimage import io
from skimage import data
import matplotlib
import matplotlib.pyplot as plt


a = io.imread("/home/katerina/Documents/python/image4.jpg")
plt.imshow(a , cmap='gray', vmin=0, vmax=255)
h = np.histogram(a,bins=256)
cdf_a = np.zeros(256)
for i in range(256):
    cdf_a[i] = cdf_a[i-1] + h[0][i]
fig1 = plt.figure()
plt.plot(h[0]) 
plt.show()

fig2 = plt.figure()
plt.plot(cdf_a)
plt.show()
b = np.zeros(a.shape , dtype = np.uint8)
t = 255/(a.shape[0]*a.shape[1])
for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        b[x][y] = cdf_a[a[x][y]] * t
fig3 = plt.figure()
plt.imshow(b, cmap='gray', vmin=0, vmax=255)

h_b = np.histogram(b,bins=256)
fig4 = plt.figure()
plt.plot(h_b[0])
plt.show()
