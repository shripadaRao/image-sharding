from email.mime import image
from PIL import Image
from numpy import asarray
import os


# load the image and convert into
# numpy array
img = Image.open('file.jpeg')
numpydata = asarray(img)

#user input to number of shred

no_tiles = int(input("No of sharding:"))
#implement sharding to other nos also not just power of 2.


M = numpydata.shape[0]//no_tiles
N = numpydata.shape[1]//no_tiles
tiles = [numpydata[x:x+M,y:y+N] for x in range(0,numpydata.shape[0],M) for y in range(0,numpydata.shape[1],N)]

def getImage(num):
    return Image.fromarray(num)

#function for saving
def save_in_dir(num):
    image_path = "photos/{}".format(num)
    #os.mkdir(image_path)
    image.save(f'{img_path}file{num}.jpeg')

img_path = "photos/"
for x in range(0,no_tiles*2):
    tile = tiles[x]
    image = getImage(tile)
    save_in_dir(x)

