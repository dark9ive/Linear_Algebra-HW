# ProgrammingHW03

Linear Algebra Programming HW 03

## Intro

This code includes two parts of the homework.  
You can choose them by adding arguments while running.  
Running instructions are listed in [Usage](https://github.com/dark9ive/Linear_Algebra-HW/tree/master/week05/programmingHW#Usage).

## Usage

Please make sure you have [python3](https://wiki.python.org/moin/BeginnersGuide/Download) and [numpy](https://www.scipy.org/install.html) installed, and your terminal can show unicode characters.

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

  
<img id="success" src="https://github.com/dark9ive/Linear_Algebra-HW/blob/master/week05/programmingHW/pics/screenshot.png">
