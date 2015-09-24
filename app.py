import matplotlib.pyplot  as plot
import matplotlib.colors as colors

import numpy              as np

from random import randint

from sample import sample as X
import numpy as np


sampleArray = X

width = X.shape[0]
height = X.shape[1]

#Color

screenValuesColor = np.zeros((width,height, 3), order="F")

for x in range(width):
	for y in range(height):
		value = sampleArray[x][y]
		screenValuesColor[x][y] = np.array([1.0-value,2.0*value-1.0,value*2.0-1.0])


#Calculate blob size
visitedPixels = np.zeros((width,height), order="F",dtype=bool)


def calculateBlobSize(x, y,blobSize):

	#Set the pixel I am checking to visited 
	visitedPixels[x][y]=True

	#check left
	nextX=x-1
	nextY=y
	if x-1 != -1 and sampleArray[x][y] == sampleArray[nextX][nextY] and visitedPixels[nextX,nextY] != True:
		blobSize=calculateBlobSize(nextX,nextY,blobSize)

	#check right
	nextX=x+1
	nextY=y
	if x+1 != width and sampleArray[x][y] == sampleArray[nextX][nextY] and visitedPixels[x+1,y] != True:
		blobSize=calculateBlobSize(nextX,nextY,blobSize)

	#check down
	nextX=x
	nextY=y-1
	if y-1 != -1 and sampleArray[x][y] == sampleArray[nextX][nextY] and visitedPixels[x,y-1] != True:
		blobSize=calculateBlobSize(nextX,nextY,blobSize)

	#check up
	nextX=x
	nextY=y+1
	if y+1 != height and sampleArray[x][y] == sampleArray[nextX][nextY] and visitedPixels[x,y+1] != True:
		blobSize=calculateBlobSize(nextX,nextY,blobSize)



	return blobSize+1



blobSizes= np.zeros((width,height), order="F")


for x in range(width):
	for y in range(height):
		#Reset the array of visited pixels every time we check a pixel
		visitedPixels = np.zeros((width,height), order="F",dtype=bool)
		blobSizes[x][y] = calculateBlobSize(x,y,0)

#BlobSize

screenValuesBlobSize= np.zeros((width,height, 3), order="F")

maxValue =-1
maxX =0
maxY=0

for x in range(width):
	for y in range(height):
		if blobSizes[x][y] > maxValue:
			maxValue=blobSizes[x][y]
			maxX=x
			maxY=y
		# value = (1.0-blobSizes[x][y])*20
		value=0.0
		screenValuesBlobSize[x][y] = np.array([value,value,value])

for x in range(width):
	for y in range(height):
		if blobSizes[x][y]==maxValue:
			value=1.0
			screenValuesBlobSize[x][y] = np.array([value,value,value])

print "Biggest blob size: " + str(maxValue)

#Plot it

plot.figure(1)

plot.subplot(121)
plot.imshow(screenValuesColor,interpolation="nearest")


plot.subplot(122)
plot.imshow(screenValuesBlobSize, interpolation="nearest")

plot.show()
