from sample import sample as X
import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(threshold=np.nan)

max_blob = 0

Y = np.zeros(X.shape)
Y.fill(-1)

w, h = X.shape

blobs = np.zeros(h * w)
blob_index = 0

def clone():
    return np.zeros(X.shape)

def contiguous_left(x, y):
    return X[x][y] == X[x - 1][y]

def contiguous_right(x, y):
    return X[x][y] == X[x + 1][y]

def contiguous_up(x, y):
    return X[x][y] == X[x][y - 1]

def contiguous_down(x, y):
    return X[x][y] == X[x][y + 1]

def merge_shapes(x, y, i, V):
    if Y[x][y] != -1:
        Y[x][y] = i
        V[x][y] = 1.0

        if x < w - 1 and contiguous_right(x, y) and V[x + 1][y] != 1.0:
            merge_shapes(x + 1, y, i, V)

        if x > 0 and contiguous_left(x, y) and V[x - 1][y] != 1.0:
            merge_shapes(x - 1, y, i, V)

        if y < h - 1 and contiguous_down(x, y) and V[x][y + 1] != 1.0:
            merge_shapes(x, y + 1, i, V)

        if y > 0 and contiguous_up(x, y) and V[x][y - 1] != 1.0:
            merge_shapes(x, y - 1, i, V)

for x in range(w):
    for y in range(h):
        right = False
        down = False
        if Y[x][y] == -1:
            Y[x][y] = blob_index
            blobs[blob_index] += 1
            current_index = blob_index
        else:
            current_index = Y[x][y]

        # if x < w - 1 and contiguous_right(x,y):
        #     # if Y[x + 1][y] != -1:
        #     #     blobs[current_index] += blobs[Y[x + 1][y]]
        #     #     blobs[Y[x + 1][y]] = 0
        #     #     merge_shapes(x + 1, y, current_index)
        #     # else:
        #     blobs[current_index] += 1
        #     Y[x + 1][y] = current_index
        # else:
        #     blob_index += 1
        # if y < h - 1 and contiguous_down(x,y):
        #     # if Y[x][y + 1] != -1:
        #     #     blobs[current_index] += blobs[Y[x][y + 1]]
        #     #     blobs[Y[x][y + 1]] = 0
        #     #     merge_shapes(x, y + 1, current_index)
        #     # else:
        #     Y[x][y + 1] = current_index
        #     blobs[current_index] += 1
        # else:
        #     blob_index += 1

        # backwards.. this goes down
        if x < w - 1 and contiguous_right(x,y):
            if Y[x+1][y] != -1:
                blobs[current_index] += blobs[Y[x+1][y]]
                blobs[Y[x+1][y]] = 0
                merge_shapes(x+1,y,current_index, clone())
            else:
                Y[x+1][y] = current_index
                blobs[current_index] += 1
                right = True

        # backwards.. this goes right
        if y < h - 1 and contiguous_down(x,y):
            # there's already a shape!
            if Y[x][y+1] != -1:
                blobs[current_index] += blobs[Y[x][y+1]]
                blobs[Y[x][y+1]] = 0
                merge_shapes(x,y+1,current_index, clone())
            else:
                Y[x][y+1] = current_index
                blobs[current_index] += 1
                down = True
        else:
            blob_index += 1

        if blobs[current_index] > max_blob:
            max_blob = blobs[current_index]
            Z[x][y] = 1.0
            if right:
                Z[x+1][y] = 1.0
            if down:
                Z[x][y+1] = 1.0

print max_blob

plt.figure(1)
plt.subplot(221)
plt.imshow(X, interpolation="nearest")
plt.subplot(222)
plt.imshow(Y, interpolation="nearest")\
plt.show()
