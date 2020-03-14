# Week 02

Class review of NCCU-CS Linear Algebra week 2.

## Intro

This is 108703015's Linear Algebra homework. Seperated into two parts:

 - [Homework](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week02#homework)
 - [Introspection](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week02#introspection)

### Working environments

 - Operating System: Ubuntu 18.04
 - Python version: 3.6.9

## Homework

[Here's](https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week02/homework02.py) the source code of this week's homework.  
Trying my best on making a class review.

### Before we started...

If you want to tryout my code, make sure you have [python3](https://wiki.python.org/moin/BeginnersGuide/Download), [numpy](https://www.scipy.org/install.html), [matplotlib](https://matplotlib.org/users/installing.html), and [xkcd](https://xkcd.com/1654/) installed on your system. If you have no idea what they are, please click them for installing guides.

### Import library(s)

Just like what we do in the last week, you can import numpy by using the following line:

```python
import numpy as npy
```

### Assign variable(s)

In the next two lines, I assigned ***x*** and ***y*** as a 2×3 and 3×2 matrix.

```python
x = npy.array([[1, 2, 3], [1, 2, 3]])
y = npy.array([[1, 2], [1, 2], [1, 2]])
```

### Matrix multiplication

Accroding to what we have learned about matrix, we can do the ***matrix multiplication*** on x and y. In python, we can use the 'numpy.dot()' function to done that.

```python
ans = npy.dot(x, y)
print(ans)
```

The result of xy is printed on the screen, which is `[6, 12], [6, 12]`.  
The next operation I have done is to calculate the ***dot product*** of two vectors.  

### Dot product

So now I assigned x and y as two vectors with 3 elements each.

```python
x = npy.array([3, 2, 1])
y = npy.array([1, 2, 3])
```

Then I calculate the dot product of these two vectors using the `numpy.dot()` function.

```python
ans = npy.dot(x, y)
print(ans)
```

The result should be printed on the screen: `10`

### error(s)

I've tried to assign the matrices with different sizes which both of them cannot multiply the other. and the dot operation returned the following error:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 6, in dot
ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
```

## Introspection

&nbsp;&nbsp;&nbsp;&nbsp;During this week's course, Mr.Tsai has taught us some basics about the linear system and matrix in math. Although I've learned them in senior high school courses, I didn't realize that they have so much to do with the computer science. In addition, numpy provides a convenient environment for us to finish those related calculations, including matrix add/subtract/multiplication, discriminate solution(s) of a linear system...etc. This part is way more different from the senior high school course. In senior high, the main goal is to learn how to do such operations, which is really boring. In Mr.Tsai's class, we use techniques to complete those tasks, and put our attention on discussing math problems, which is more useful.  
  
&nbsp;&nbsp;&nbsp;&nbsp;If you ask me: *"Why do you want to finish your homework in this form? It spent much more time than the normal ways!"*  
I will give you the answer: *"Because I think this is cool, and I think this course is worthwhile to spent time on. That's it."*
