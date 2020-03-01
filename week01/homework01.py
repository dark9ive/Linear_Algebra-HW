import numpy as npy
import matplotlib.pyplot as plot
%matplotlib inline

x = npy.linspace(0, 5, 1000)
y = 2**x
plot.plot(x, y)
