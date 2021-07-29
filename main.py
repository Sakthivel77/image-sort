from PIL import Image 
import random
import numpy as np
import colorsys     
import copy

r,c = 300,300
totalframes = 120

def hsv2rgb(l):
    return [[tuple(round(i * 255) for i in colorsys.hsv_to_rgb(i[0],i[1],i[2]))for i in j]for j in l] 

def saveimg(a,n = ''):
    converted = np.array(hsv2rgb(a))
    Image.fromarray(converted.astype('uint8')).save(f'images/random{n}.png')

hues = [random.random() for i in range(c)] # creates 300 random hues value

randomImage = [ random.sample([[hues[i],1,1] for i in range(c)],c) for j in range(r) ] #creates 300 row with the 300 pixels with hues values based on hues and shuffles each row

sortImage = copy.deepcopy(randomImage)
saveimg(randomImage)
def bubblesort(l,key= lambda x:x):
    l = [key(x) for x in l]
    swaps = []
    A = [i[0] for i in l]
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j] > A[j+1]:
                swaps.append([j,j+1])
                A[j],A[j+1] = A[j+1],A[j]
    return swaps

def pixel_swap(row,swap):
        randomImage[row][swap[0]], randomImage[row][swap[1]] = randomImage[row][swap[1]], randomImage[row][swap[0]] 
        
omegaswaps = [bubblesort(row) for row in sortImage] 

maxlen = len(max(omegaswaps,key= lambda x: len(x)))
print(maxlen)
frames = [int(i) for i in np.linspace(0,maxlen-1,totalframes)]

filenum = 0
for swap_pos in range(maxlen):
    for i in range(c):
        try:
            pixel_swap(i,omegaswaps[i][swap_pos])
        except:
            pass
    if swap_pos in frames:
        filenum+= 1
        
        saveimg(randomImage,str(filenum).zfill(5))
    