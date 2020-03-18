import numpy as npy

quantity = npy.zeros(shape=(2, 2))
price = npy.empty(2)
for a in range(2):
    for b in range(2):
        quantity[a][b] = input("Please insert the quantity of the item %d bought in week %d: "%(a+1, b+1))
    price[a] = input("Please insert the total price of week %d: "%(a+1))
inverseQ = npy.linalg.inv(quantity)
ans = npy.dot(inverseQ, price)
for a in range(2):
    print ("the price of item", a, "is", int(ans[a]))
exit()
