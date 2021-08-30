from operator import xor
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


x = np.arange(1,10,0.1)
y = np.sin(np.power(x,1/3))
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()
