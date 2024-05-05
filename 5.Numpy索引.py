import numpy as np

a = np.arange(5,17).reshape(3,4)
print(a)
# 索引
print(a[0]) # 第0行
print(a[0][1]) # 第0行1列
print(a[0,1])
print(a[1,:]) # 第1行
print(a[1,1:]) # 第1行1列后
print(a[:,1:]) # 所有第1列后
print("-"*20)

# 遍历
for row in a:
    print(row)
for col in a.T:
    print(col)
print("-"*20)

# 将多维数组转换为一维数组
print(a.flatten())

# 获取数组的迭代器
for elem in a.flat:
    print(elem)
