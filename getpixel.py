from PIL import Image
import random

try:
    im = Image.open("cat.jpg")
except FileNotFoundError:
    print("file not found")
    exit(0)

print(im.format, im.size, im.mode)

width, height = im.size
blockSize = 30;

out = Image.new('RGB', (width, height), 'black')

for i in range(500):
    w = random.randrange(width)
    h = random.randrange(height)
    for i in range(blockSize):
    	for j in range(blockSize):
   			try:
   				out.putpixel((w+i,h+j), im.getpixel((w+i,h+j)))
   			except IndexError:
   				break

#im.show()
out.show()

out.save("catout.png")
