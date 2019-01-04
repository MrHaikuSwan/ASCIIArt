from PIL import Image
import numpy as np
import os

def render(arr):
    for y in range(len(arr)):
        print ''.join([i*2 for i in arr[y]])

convertstr = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

inputimg = [i for i in os.listdir('InputImage/') if '.' in i][0]
img = Image.open('InputImage/' + inputimg)
img = img.convert('L')
dims = img.size
factor = 200.0/img.size[1]
new_dims = tuple([int(i*factor) for i in dims])
img = img.resize(new_dims)
imgarr = np.array(img)
asciiarr = np.zeros(imgarr.shape, dtype=str)

for y in range(len(imgarr)):
    for x in range(len(imgarr[y])):
        index = imgarr[y,x]*64/255
        char = convertstr[index]
        asciiarr[y,x] = char

render(asciiarr)

