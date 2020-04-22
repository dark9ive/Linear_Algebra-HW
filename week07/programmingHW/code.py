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
        while(x > y):
            print("The rows cannot be more than the columns!")
            x = int(input("Please insert the row(s) of your matrix: "))
            y = int(input("Please insert the column(s) of your matrix: "))

        matrix = npy.zeros(shape=(max(x, y), max(x, y)))

        for a in range(x):
            for b in range(y):
                matrix[a][b] = input("Please insert the element in the position (%d, %d): "%(a+1, b+1))
        print("\n\nThis is your input matrix:")
        for a in range(x):
            print(matrix[a])
    
        minusone = npy.zeros(shape=(0, 0))

        for a in range(max(x, y)):
            for b in range(a, max(x, y)):
                if(matrix[b][a] != 0):
                    if(b == a):
                        break
                    else:
                        matrix = swap(a, b, matrix)
                        break
            if(matrix[a][a] == 0):
                buf = npy.zeros(shape=(1, y))
                buf[0][a] = -1
                matrix = npy.insert(matrix, a, buf, axis=0)
                matrix = npy.delete(matrix, max(x, y), axis=0)
                minusone = npy.append(minusone, a)
                continue
            else:
                matrix[a] /= matrix[a][a]
                for b in range(y):
                    if(b == a):
                        continue
                    if(matrix[b][a] != 0):
                        vectoradd(a, b, matrix)
        for a in range(x):
            for b in range(y):
                if(matrix[a][b] == 0):
                    matrix[a][b] = 0
        print("\n\nRREF of your input matrix is:")
        for a in range(y):
            lock = 1;
            for b in minusone:
                if(a == b):
                    lock = 0
                    break
            if(lock):
                print(matrix[a])
        print("\n\nYour RREF marix after adding minus one(s) is:")
        print(matrix)

        sol = npy.zeros(shape=(1, max(x, y)))
        print("\n\n∀ ", end = '')
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
        while(x > y):
            print("The rows cannot be more than the columns!")
            x = int(input("Please insert the row(s) of your matrix: "))
            y = int(input("Please insert the column(s) of your matrix: "))

        matrix = npy.zeros(shape=(x, y))
        ans = npy.zeros(shape=(x, y))

        for a in range(x):
            for b in range(y):
                matrix[a][b] = input("Please insert the element in the position (%d, %d): "%(a+1, b+1))

        #for a in range(x):

        for a in range(x):
            for b in range(a, x):
                ans[b] += matrix[a]*random.randint(1, 3)

        print(ans)
        exit()
    else:
        print("Wrong arguments!")
        exit()
