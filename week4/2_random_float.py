import random

# random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
# 如果a > b，则生成的随机数n: a >= n >= b。如果 a <b， 则 b >= n >= a
print(random.uniform(10, 20))
