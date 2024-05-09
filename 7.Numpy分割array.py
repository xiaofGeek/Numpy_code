import numpy as np

a = np.arange(12).reshape(3,4)

print(a)
# split:等量分割
print(np.split(a,3,axis=0)) # 按行
print(np.split(a,2,axis=1)) # 按列
print(np.split(a,4,axis=1)) # 按列

# array_split:不等量分割
print(np.array_split(a,2,axis=0))

# 纵向和横向分割
print(np.vsplit(a,3))
print(np.hsplit(a,2))
