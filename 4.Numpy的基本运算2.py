import numpy as np

a = np.array([[3,4,5],
              [6,7,8]])
print(np.sum(a))
# axis:0-行 1-列
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

b = np.arange(5,15).reshape(2,5)
print(b)
print(np.average(b,axis=1)) # 平均值
print(np.mean(b,axis=1))
print(np.median(b)) # 中位数
print(np.cumsum(b)) # 累加
print(np.diff(b)) # 累差
print("*"*20)

c = np.arange(15,5,-1).reshape(2,5)
print(c)
print(np.sort(c)) # 排序-升序
print(np.transpose(c)) # 矩阵行列转换 np.T
print(np.clip(c,9,12)) # 将小于9的数都为9，大于12的数都为12
