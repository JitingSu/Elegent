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
cnt = guess / count * 21.0
print(cnt)
