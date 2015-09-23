import numpy as np

def new_sample():
    np.set_printoptions(threshold=np.nan)
    X = np.random.choice([1,0,0.5,0.25,0.75],(100,100))
    print X

new_sample()
