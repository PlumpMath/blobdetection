import matplotlib.pyplot  as plot

import numpy              as np

from sample import sample as X

sampleArray = np.array(X)

screenValues = np.zeros((len(X),len(X[0]), 3), order="F")

for x in range(width["view"]):
  for y in range(height):
    value = sampleArray[x][y]
    screenValues[x][y] = np.array([value,value,value])
    # screenInt[x][y] *= 126

plot.imshow(X,interpolation="nearest")
plot.show()