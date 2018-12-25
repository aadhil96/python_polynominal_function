import numpy as np
from matplotlib import pyplot

a = np.array([[1,-3,2,-1,5],[3,2,-7,2,-1],[-1,1,3,-5,12],[2,4,-12,6,1],[1,1,-1,-3,-11]])
b = np.array([[11],[-7],[24],[17],[-13]])

print(a)
print()
print(b)

a_inv = np.linalg.inv(a)

print()

print(a_inv)
x = np.matmul(a_inv,b)

print()

print(x)