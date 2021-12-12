import numpy as np

def rectangle(size,color, transparent = 0x000000):
    return np.full(size,color)

def rectangle_outline(size,color,thickness, transparent = 0x000000):
    t = thickness #lazy
    (x,y) = size
    a = np.full(size,color)
    a[t:(a.shape[0] - t),t:(a.shape[1] - t)] = transparent