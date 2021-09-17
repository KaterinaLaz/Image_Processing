from PIL import Image

#Με το μέσο όρο των τριών χρωματικών συνιστωσών
img = Image.open("/home/katerina/Documents/python/image1.jpg")
imgG = img.convert('L')
for x in range(img.size[0]):
    for y in range(img.size[1]):
        imgG.putpixel((x,y),int(sum(img.getpixel((x,y)))/3))
imgG.save("/home/katerina/Documents/python/image1_g_a.jpg")
       
#Με την ελάχιστη τιμή των τριών χρωματικών συνιστωσών
imgG_min= Image.new('L',(img.size[0],img.size[1]))
for x in range(img.size[0]):
    for y in range(img.size[1]):
        imgG_min.putpixel((x,y),int(min(img.getpixel((x,y)))))
imgG_min.save("/home/katerina/Documents/python/image1_g_b.jpg")

#Με τη μέγιστη τιμή των τριών χρωματικών συνιστωσών
imgG_max= Image.new('L',(img.size[0],img.size[1]))
for x in range(img.size[0]):
    for y in range(img.size[1]):
        imgG_max.putpixel((x,y),int(max(img.getpixel((x,y)))))
imgG_max.save("/home/katerina/Documents/python/image1_g_c.jpg")

imgG_max.show()
imgG_min.show()
imgG.show()