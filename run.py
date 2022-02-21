from email.mime import image
from PIL import Image
from numpy import asarray


# load the image and convert into
# numpy array
img = Image.open('result_16:31:21.jpg')
numpydata = asarray(img)

#user input to number of shred
#no_shred = input("Number of file shreds") 
no_shred = 2 #power of 2

M = numpydata.shape[0]//no_shred
N = numpydata.shape[1]//no_shred
tiles = [numpydata[x:x+M,y:y+N] for x in range(0,numpydata.shape[0],M) for y in range(0,numpydata.shape[1],N)]

def getImage(num):
    return Image.fromarray(num)

#function for saving
def saveAs(num):
    image.save('file{}.jpeg'.format(num))


for x in range(0,4):
    tile = tiles[x]
    image = getImage(tile)
    saveAs('tile_{}'.format(x+1)) #x+1 for simplicity

