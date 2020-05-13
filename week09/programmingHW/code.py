import numpy as npy
import matplotlib.pyplot as plt
import math

def transform(a, b):            #    returns a 3x3 matrix  
    returnval = npy.zeros(shape=(3, 3))
    returnval = [[1, 0, a], [0, 1, b], [0, 0, 1]]
    return returnval

def rotate(theta):
    theta = theta/360*math.pi*2
    returnval = npy.zeros(shape=(3, 3))
    returnval = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
    return returnval

x1 = float(input("Please insert xmin: "))
x2 = float(input("Please insert xmax: "))
y1 = float(input("Please insert ymin: "))
y2 = float(input("Please insert ymax: "))
x = npy.linspace(x1, x2, 30)
y = npy.linspace(y1, y2, 30)
max_ = 0

points = []            #    homogeneous coordinates array

for a in x:
    for b in y:
        plt.scatter(a, b, 20, 'r')
        if(abs(a) > max_):
            max_ = abs(a)
        if(abs(b) > max_):
            max_ = abs(b)
        points.append([a, b, 1])
plt.xlim(-max_*1.2, max_*1.2)        #    re-range the chart
plt.ylim(-max_*1.2, max_*1.2)        #    re-range the chart
plt.plot([0, 0], [-max_*1.2, max_*1.2])        #    draw the y-axis
plt.plot([-max_*1.2, max_*1.2], [0, 0])        #    draw the x-axis

plt.show()

############    Part 1 finished.    ############

theta = float(input("Please insert degree(s) to rotate: "))
deltax = float(input("Please insert the unit(s) of x-direction transform: "))
deltay = float(input("Please insert the unit(s) of y-direction transform: "))

transform_matrix = npy.eye(3)       #    Identity matrix 
transform_matrix = transform_matrix.dot(transform(deltax, deltay))       #    transform every points by x+0, y-5.
transform_matrix = transform_matrix.dot(rotate(theta))             #    rotate every points about (0, 0) for 45 degrees.

for a in x:
    for b in y:
        plt.scatter(a, b, 20, 'r')

for point in points:
    point = transform_matrix.dot(point)
    plt.scatter(point[0], point[1], 20, 'b')
    if(abs(point[0]) > max_):
        max_ = abs(point[0])
    if(abs(point[1]) > max_):
        max_ = abs(point[1])

plt.xlim(-max_*1.2, max_*1.2)        #    re-range the chart
plt.ylim(-max_*1.2, max_*1.2)        #    re-range the chart
plt.plot([0, 0], [-max_*1.2, max_*1.2])        #    draw the y-axis
plt.plot([-max_*1.2, max_*1.2], [0, 0])        #    draw the x-axis
plt.show()

############    Part 2 finished.    ############

print(transform_matrix)
