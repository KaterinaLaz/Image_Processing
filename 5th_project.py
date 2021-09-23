
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 =Image.open("/home/katerina/Documents/python/image5.png")
a = np.array(im1)
a = a / 255

sob_x = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sob_y = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
plt.imshow(a, cmap='gray', vmin=0, vmax=1)

def convolution(a,b):
    c = np.ones((a.shape[0]+2,a.shape[1]+2))
    d = np.zeros(a.shape)
    c[1:-1,1:-1] = a
    for x in range(1,c.shape[0]-1):
        for y in range(1,c.shape[1]-1):
            d[x-1,y-1] = np.sum(c[x-1:x+2,y-1:y+2]*b)
    return d.astype(np.uint8)

#για χ
im_sob_x = convolution(a,sob_x)
plt.imshow(im_sob_x, cmap='gray', vmin=0, vmax=1)
#για y
im_sob_y = convolution(a,sob_y)
plt.imshow(im_sob_y, cmap='gray', vmin=0, vmax=1)
#και τα δύο
im_sob_all = im_sob_x + im_sob_y
plt.imshow(im_sob_all, cmap='gray', vmin=0, vmax=1)