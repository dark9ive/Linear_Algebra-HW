import numpy as npy             #   import numpy
x = npy.array([1, 2, 3])        #   assign x as a 1×3 array
y = npy.array([[1], [2], [3]])  #   assign y as a 3×1 array
ans = npy.dot(x, y)             #   dot operation
print(ans)                      #   print the answer of "ans"
y = npy.array([1, 2, 3])        #   assign y as a 1×3 array
ans = npy.dot(x, y)             #   dot operation
print(ans)                      #   print the answer of "ans"
exit()                          #   exit
