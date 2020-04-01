import numpy as npy                     #   import numpy
x = npy.array([[1, 2, 3], [1, 2, 3]])   #   assign x as a 2×3 array
y = npy.array([[1, 2], [1, 2], [1, 2]]) #   assign y as a 3×2 array
ans = npy.dot(x, y)                     #   dot operation
print(ans)                              #   print the answer of "ans"
x = npy.array([3, 2, 1])                #   assign y as a 1×3 vector
y = npy.array([1, 2, 3])                #   assign y as a 1×3 vector
ans = npy.dot(x, y)                     #   dot operation
print(ans)                              #   print the answer of "ans"
exit()                                  #   exit
