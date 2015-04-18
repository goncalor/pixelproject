from PIL import Image
import random

try:
    im = Image.open("cat.jpg")
except FileNotFoundError:
    print("file not found")
    exit(0)

print(im.format, im.size, im.mode)

width, height = im.size

out = Image.new('RGB', (width, height), 'black')

for i in range(1000000):
    w = random.randrange(width)
    h = random.randrange(height)
    out.putpixel((w,h), im.getpixel((w,h)))

#im.show()
out.show()

out.save("catout.png")
