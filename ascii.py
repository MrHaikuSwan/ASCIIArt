from PIL import Image
import numpy as np

def render(arr):
    for y in range(len(arr)):
        print ''.join([i*2 for i in arr[y]])

convertstr = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

img = Image.open('flower.png')
img = img.convert('L')
img = img.resize((200,200))
imgarr = np.array(img)
asciiarr = np.zeros(imgarr.shape, dtype=str)

for y in range(len(imgarr)):
    for x in range(len(imgarr[y])):
        index = imgarr[y,x]*64/255
        char = convertstr[index]
        asciiarr[y,x] = char

render(asciiarr)

