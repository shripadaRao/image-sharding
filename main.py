# Import the necessary libraries
from PIL import Image
from numpy import asarray


# load the image and convert into
# numpy array
img = Image.open('result_16:31:21.jpg')
numpydata = asarray(img)

part1 = numpydata[:455,:512,:]
part2 = numpydata[455:,:512,:]
part3 = numpydata[:455,512:,:]
part4 = numpydata[455:,512:,:]
# data
#print(numpydata)(910, 1024, 3)

print(numpydata.shape)

#getting img from matrix
#pilImage = Image.fromarray(part1)
pilImage = Image.fromarray(part4)
pilImage.save('file4.jpeg')



#func for getting img from matrix
def getImage(num):
    return Image.fromarray(num)

#function for saving
def save(num):
    pilImage.save('file{}.jpg'.format(num))


#user input to number of shred
no_shred = 2
no_shred = input("No of file shreding. Power of 2")

def no_shred(no):
    no = input("Number of file shreds")
    if no%2 != 0:
        print("Select in powers of 2")

#func to shard img
M = numpydata.shape[0]//no_shred
N = numpydata.shape[1]//no_shred
tiles = [numpydata[x:x+M,y:y+N] for x in range(0,numpydata.shape[0],M) for y in range(0,numpydata.shape[1],N)]
