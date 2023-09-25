import random
import math

count = 0
guess = 0
for i in range(10000):
    count += 1
    x = random.uniform(2.0, 3.0)
    # 设最高点不超过21
    y = random.uniform(0.0, 21.0)
    if y <= x ** 2 + 4 * x * math.sin(x):
        guess += 1
# 按面积的思想来理解：总面积为（3-2）*21=21。guess / count是按蒙特卡罗法算出的概率（10000个点中在函数面积的中的点的比例），然后乘以总面积，就可以算出定积分。
cnt = guess / count * 21.0
print(cnt)
