import numpy as npy
import matplotlib.pyplot as plt
x = npy.linspace(0, 5, 10)      #   set x as a set with 10 elements, every elements has the same difference to the previous one.
y = 2**x        #   set y as a set with the same amount of elements of x, and each of them is 2 to the power of x.
plt.figure(1)       #   switch to graph 1.
plt.scatter(x, y)   #   draw only points on the x-y plane.
plt.figure(2)       #   switch to graph 2.
plt.plot(x, y)      #   link those points with lines.
with plt.xkcd():    #   comic style!
    plt.figure(3)   #   switch to graph 3.
    plt.scatter(x, y)   #   draw only points on the x-y plane.
    plt.figure(4)   #   switch to graph 4.
    plt.plot(x, y)  #   link those points with lines.
#   switch back to normal.
plt.figure(5)   #   switch to graph 5.
plt.plot(x, y)  #   link those points with lines.
