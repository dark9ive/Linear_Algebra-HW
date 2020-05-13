# ProgrammingHW06

Linear Algebra Programming HW 06

## usage

codes [here](https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week09/programmingHW/code.py).

```
python3 code.py
```

I recommend you to run these codes on a ___jupyter notebook___ or anything similar since terminal enviornments can't show the charts.  

## principle

### Part 1

So this is how my codes works:  

First the user will insert a range for a rectangle, then I will fill the region with 30x30 points separated.

After that, the code will draw each points on a chart, which ranged from x=(-1.2\*max, 1.2\*max), y=(-1.2\*max, 1.2\*max) for max=max(eachX, eachY).

This is all of Part 1.  

### Part 2

In part 2, the user is asked to insert the degree(s) to rotate, and the x-direction and y-direction transform.

The transform matrix is calcucate as follows:

1. First make a 3x3 identity matrix.
2. Multiply(npy.dot) the matrix with rotate-matrix, which is [[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]]
3. Multiply(npy.dot) the matrix with transform-matrix, which is [[1, 0, deltaX], [0, 1, deltaY], [0, 0, 1]]

then multiply every points with the 3x3 transform matrix and draw them on a new chart.


## Example
<img src=https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week09/programmingHW/pics/Myexample.png >.
