# Week 01

Class review of NCCU-CS Linear Algebra week 1.

## Intro

This is 108703015's Linear Algebra homework. Seperated into two parts:

 - [Homework](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week01#homework)
 - [Introspection](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week01#introspection)

### Working environments

 - Operating System: Ubuntu 18.04
 - Python version: 3.6.9

## Homework

[Here's](https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week01/homework01.py) the source code of this week's homework.  
Due to my lack in creativity, I don't know how to draw something fancy. Instead, I'll try my best on making a class review.

### Before we started...

If you want to tryout my code, make sure you have [python3](https://wiki.python.org/moin/BeginnersGuide/Download), [numpy](https://www.scipy.org/install.html), [matplotlib](https://matplotlib.org/users/installing.html), and [xkcd](https://xkcd.com/1654/) installed on your system. If you have no idea what they are, please click them for installing guides.

### Import library(s)

In the first two line, you will see:

```python
import numpy as npy
import matplotlib.pyplot as plt
```

Their functions are importing **numpy** and **matplotlib** into my codes.  

### Assign variables

Next, I assigned two sets of variables:

```python
x = npy.linspace(0, 5, 10)
y = 2**x 
```

In the first line, I assigned **x** with `numpy.linespace(a, b, c)`, which means assign an array with `c` isometric numbers ranged from `a` to `b`. In the second line, I assigned **y** as an array with each element equals to 2<sup>x</sup>.  

### Draw graphs

The next function I use is `plt.figure()`.  
This fuction is used to switch different graphs. The only parameter needed is the index of the graph, which starts from 1.  
  
The function `plt.scatter(x, y)` can draw the graph with all the points seprated:  

<img id="figure01" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week01/pics/figure01.png" width="400" height="300">

The function `plt.plot(x, y)` can draw the graph with all the points linked by straight lines:  

<img id="figure02" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week01/pics/figure02.png" width="400" height="300">

The function `plt.xkcd()` can draw your graphs in comic style:  

<img id="figure03" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week01/pics/figure03.png" width="400" height="300"><img id="figure04" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week01/pics/figure04.png" width="400" height="300">

The comic style looks cool, ***however......***  
  
Many students found that this action cannot be undo, which means their graphs kept being comic style. I've found a solution for that:

```python
with plt.xkcd():
    blah.....
    blah....
    some actions....
return to normal style here. 
```

Using `with plt.xkcd():`, your results can be displayed in comic style without affecting other parts.  

## Introspection

In this week's course, Mr.Tsai has taught us how to build the environment which will be used in this course. Also, Mr.Tsai has explained the goal of this course. I'm happy that Mr.Tsai focus on waht a CS student need instead of just teaching math. This makes me willing 
to spend more time on this course(including writing this README.md file). Hope I can keep the quality of homework until the end of this semester.
