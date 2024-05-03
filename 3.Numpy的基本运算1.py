import numpy as np

a = np.array([10,11,12,13])
b = np.array([0,1,2,3])

c = a+b # 加法
print(c)
c = a-b # 减法
print(c)
c = a*b # 乘法
print(c)

d = b**2 # 平方
print(d)

e = np.sin(b) # 三角函数
print(e)

a1 = np.array([[0,1],
               [2,3]])
b1 = np.array([[0,1,2],
               [3,4,5]])
c_dot = np.dot(a1,b1) # 矩阵相乘
c_dot_2 = a1.dot(b1)
print(c_dot)
print(c_dot_2)
