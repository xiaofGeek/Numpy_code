import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])
c = np.array([3,3,3])

# vertical stack
d = np.vstack((a,b,c))
# horizontal stack
e = np.hstack((a,b,c))
print(d.shape)
print(d)
print(e.shape)
print(e)

print(30*'-')

# np.newaxis:插入新维度
a1 = a[:,np.newaxis] # 将a变成列向量
b1 = b[:,np.newaxis]
c1 = c[:,np.newaxis]

d1 = np.vstack((a1,b1,c1))
e1 = np.hstack((a1,b1,c1))
print(d1.shape)
print(d1)
print(e1.shape)
print(e1)

print(30*'-')

# concatenate：实现指定轴连接数组
z = np.concatenate((a1,b1,c1,a1),axis=1) # 1-列连接
print(z)
