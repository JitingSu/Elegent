import random


# 法一 蒙特卡洛方法
def pi(n):
    i = 0
    count = 0
    # n 为传入的总点数量
    while i < n:
        # 随机产生x,y坐标
        # random() 方法返回随机生成的一个实数，它在[0,1)范围内
        x = random.random()
        y = random.random()
        # 如果x平方 + y平方 < 1，说明在圆内
        if (pow(x, 2) + pow(y, 2)) < 1:
            count += 1
        i += 1
    # π的值为：4 * （落在圆内的点/总的点）
    return 4 * (count / n)


"""
# 法二 级数展开的方法
def pi(n):
    summ = 0.0
    for i in range(n):
        sign = (-1) ** i
        term = 1 / (i * 2 + 1)
        summ += sign * term
    return 4.0 * summ
"""

"""
# 法三 公式法


def pi(m):
    p = 0
    for n in range(m):
        p += 1 / pow(16, n) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
    return p
"""

# 保留到小数点后10位的方法
print("%.10f" % pi(100000))
