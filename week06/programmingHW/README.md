# ProgrammingHW03

Linear Algebra Programming HW 03

## Intro

This code includes two parts of the homework.  
You can choose them by adding arguments while running.  
Running instructions are listed in [Usage](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week05/programmingHW#Usage).

## Usage

Please make sure you have [python3](https://wiki.python.org/moin/BeginnersGuide/Download), [numpy](https://www.scipy.org/install.html) and [sympy](https://github.com/sympy/sympy/releases) installed, and your terminal can show unicode characters.

```
python3 code.py (1 or 2)
```

## Explaination

### Part1

In the first part, the user can set a custom matrix with its rows less than its columns.  
  
If you don't, you will get this error:  
  
<img id="error1" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/screenshot_error1.png">
  
After you give me a matrix, I will show the given matrix again:
  
<img id="step1" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/step1.png">
  
Then I will make your matrix a RREF matrix by doing these:
 - If the n-th element in the n-th row equals to zero, swap the n-th row with a row which the n-th element isn't zero.
 - Divide the whole row by the value of the n-th element.
 - If the n-th element of any other row isn't zero, make it to zero by minus the whole row with the mutiple of the n-th row.
  
<img id="step2" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/step2.png">
  
...And do the minus 1 trick with the method below:
 - If there's no any row below the n-th row has value in the n-th elements, add a minus-one line in the n-th row, which means all the elements are zero, except the n-th element, which is -1.
  
<img id="step3" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/step3.png">
  
Last but not least, assign symbols with a for loop and sympy, which can show you the Homogeneous solution of your input matrix.  
  
<img id="success1" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/success1.png">
  
That's how my code briefly works.

### Part2

Mainly the reverse version of part1.  
Now it won't check whether your matrix is RREF or not.  
How it works is simply times every line with a random int from 1 to 3 and add rows randomly.  
  
For example:
  
<img id="success2" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/success2.png">
