import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage import filters
from skimage import io

img = Image.open("/home/katerina/Documents/python/image2_g.png")

#Threshold
def conv_binary1(img,t):
    img_b = Image.new('L',(img.size[0],img.size[1]))
    
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x,y)) > t:
                img_b.putpixel((x,y),255)
            else :
                img_b.putpixel((x,y),0)
    return img_b

im2 = conv_binary1(img ,140)
im2.show()
im2.save("/home/katerina/Documents/python/image2_g_a.jpg")

#Otsu
im = io.imread("/home/katerina/Documents/python/image2_g.png")
k= filters.threshold_otsu(im)
plt.imshow(im < k , cmap='binary', interpolation='nearest')
plt.axis('off')
plt.show()

