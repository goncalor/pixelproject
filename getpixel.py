from PIL import Image
import random

blockSize = 30; 
blockAmmount = 500;

try:
        im = Image.open("cat.jpg")
except FileNotFoundError:
        print("file not found")
        exit(0)

print(im.format, im.size, im.mode)
width, height = im.size
out = Image.new('RGB', (width, height), 'black')

def upSample(x, y, blockSize):
    h = x*blockSize
    w = y*blockSize
    return h,w

def Mark(x,y, dsMatrix): # down sampled matrix
    if dsMatrix[x][y] == 1:
        return False
    else:
        dsMatrix[x][y] = 1
        return True

dsHeight = height/blockSize
dsWidth = width/blockSize
dsMatrix = [[0]*dsHeight*dsWidth for x in xrange(dsHeight*dsWidth)]

for k in range(blockAmmount):
    x = random.randrange(dsHeight)
    y = random.randrange(dsWidth)
    if Mark(x, y, dsMatrix):
        h,w = upSample(x, y, blockSize)
        for i in range(blockSize):
            for j in range(blockSize):
                try:
                    out.putpixel((w+i,h+j), im.getpixel((w+i,h+j)))
                except IndexError:
                    print "inneficient :("
                    break

#im.show()
out.show()

out.save("catout.png")
