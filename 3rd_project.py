import numpy as np
from PIL import Image

img = Image.open("/home/katerina/Documents/python/image3.jpg")

for i in range(img.size[0]):
	for j in range(img.size[1]):
		ngtv = img.getpixel((i,j))
		img.putpixel((i,j),255 - ngtv)

img.show()
img.save("/home/katerina/Documents/python/image3_n.png")