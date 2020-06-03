# ProgrammingHW08

Linear Algebra Programming HW 08

## usage

codes [here](https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week11/programmingHW/code.py).

```
python3 code.py
```

I recommend you to run these codes on a ___jupyter notebook___ or anything similar since terminal enviornments can't show the charts.  

## principle

This is basically the same copy of the HW06, except some input difference.

### Part 1

So this is how my codes works:  

First the user will insert deltaX and deltaY, both zero is not accepted.  

Ater that, user has to insert x0 and y0, and the code will draw 100 points on a chart, which ranged from (x - 10 * deltaX) to (x + 10 * deltaX), (y - 10 * deltaY) to (y + 10 * deltaY).  

The chart is ranged from x=(-1.2\*max, 1.2\*max), y=(-1.2\*max, 1.2\*max) for max=max(eachX, eachY).

This is all of Part 1.  

### Part 2

In part 2, the user is asked to insert a R2 matrix, and the x-direction and y-direction transform.

The transform matrix is calcucate as follows:

1. First make a 3x3 identity matrix.
2. Ask user to fill in the [0][0], [0][1], [1][0], and[1][1].
3. Multiply(npy.dot) the matrix with transform-matrix, which is [[1, 0, deltaX], [0, 1, deltaY], [0, 0, 1]]

then multiply every points with the 3x3 transform matrix and draw them on a new chart.

Finally, my code prints out the transform matrix for the user to verify.

## Example
<img src=https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week11/programmingHW/pics/example.png >.
