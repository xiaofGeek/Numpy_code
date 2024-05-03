import numpy as np

# 一维
a = np.array([1,2,3])
print(a)
# 二维
b = np.array([[1,2,3],
              [4,5,6]])
print(b)

# 零矩阵
c = np.zeros((4,4))
print(c)

# 有序数列矩阵
d = np.arange(12).reshape(3,4)
print(d)

# 线性矩阵
e = np.linspace(1,10,5)
print(e)

# 随机矩阵
f = np.random.random((3,4))
print(f)

