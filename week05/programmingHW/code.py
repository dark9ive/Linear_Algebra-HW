import numpy as npy
import sympy as spy
import sys
import random

def swap(a, b, matrix):
    matrix[a] += matrix[b]
    matrix[b] = matrix[a] - matrix[b]
    matrix[a] -= matrix[b]
    return matrix

def vectoradd(a, b, matrix):
    matrix[b] -= matrix[a]*matrix[b][a]/matrix[a][a]
    return matrix

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Wrong arguments!")
        exit()
    elif(sys.argv[1] == "1"):
        x = int(input("Please insert the row(s) of your matrix: "))
        y = int(input("Please insert the column(s) of your matrix: "))

        matrix = npy.zeros(shape=(max(x, y), max(x, y)))

        for a in range(x):
            for b in range(y):
                matrix[a][b] = input("Please insert the element in the position (%d, %d): "%(a+1, b+1))
    
        minusone = npy.zeros(shape=(0, 0))

        for a in range(max(x, y)):
            for b in range(a, max(x, y)):
                if(matrix[b][a] != 0):
                    if(b == a):
                        break
                    else:
                        matrix = swap(a, b, matrix)
            if(matrix[a][a] == 0):
                buf = npy.zeros(shape=(1, y))
                buf[0][a] = -1
                matrix = npy.insert(matrix, a, buf, axis=0)
                matrix = npy.delete(matrix, max(x, y), axis=0)
                minusone = npy.append(minusone, a)
            else:
                #matrix[a] /= matrix[a][a]
                for b in range(a+1, max(x, y)):
                    if(matrix[b][a] != 0):
                        vectoradd(a, b, matrix)

        print(matrix)

        sol = npy.zeros(shape=(1, max(x, y)))
        print("∀ ", end = '')
        for a in range(npy.size(minusone)):
            symb = spy.Symbol(chr(65+a))
            sol = sol + symb*matrix[:, int(minusone[a])]
            print(symb, end = '')
            if(a != npy.size(minusone)-1):
                print(", ", end = '')
            else:
                print(" ∈ ℝ , the Homogeneous solution of your input matrix is ", flush = True)

        print(sol)
        exit()
    elif(sys.argv[1] == "2"):
        x = int(input("Please insert the row(s) of your matrix: "))
        y = int(input("Please insert the column(s) of your matrix: "))

        matrix = npy.zeros(shape=(x, y))
        ans = npy.zeros(shape=(x, y))

        for a in range(x):
            for b in range(y):
                matrix[a][b] = input("Please insert the element in the position (%d, %d): "%(a+1, b+1))

        for a in range(x):
            for b in range(a, x):
                ans[b] += matrix[a]*random.randint(-3, 3)

        print(ans)
        exit()
    else:
        print("Wrong arguments!")
        exit()
