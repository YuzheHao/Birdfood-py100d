import numpy as np
import random

# 功能：判断第二个数是否大于第一个数，如果第二个数大，label为1，如果第一个数大，label为-1

# 给定初始样本值
sample = [
    [2,3,1],
    [3,2,-1],
    [-1,5,1],
    [-2,-3,-1],
    [-4,3.2,1]
]

# 随机化感知器的初始参数
w1 = random.random() # 这一行是在生成一个0～1的随机数
w2 = random.random()
b = random.random()

# 学习率/步长值，决定学习的速度
lr = 0.001 # 你可以试着把这个数变大一点/变小看看会发生什么

# 将样本输入感知器计算
i = 0
while(i<len(sample)):
    print("当前正在处理样本：",sample[i])
    print(w1, w2, b)
    x1 = sample[i][0]
    x2 = sample[i][1]
    label = sample[i][2]
    # 计算激活后的感知器输出结果
    wx = x1*label*w1 + x2*label*w2 + b

    if wx <= 0 : # 如果输入样本被错分，则更新权值，然后重新对所有样本进行分类
        w1 = w1 - lr * x1
        w2 = w2 - lr * x2
        i = 0
    else:  # 如果输入样本没有被错分，就进行下一个样本样本的分类
        i = i + 1

print('最终结果为：')
print(w1,w2,b)

test = [
    [6,7],
    [6,3],
    [-1,7],
    [3,-5]
]
print('测试开始：')
for x in test:
    y = x[0]*label*w1 + x[1]*label*w2 + b
    if y > 0 : y = 1
    else: y = -1
    print('样本为：',x)
    print('label为：',y)