a = int(input())
b = a / 2
while True:
    c = (2 * b + a / (b * b)) / 3.0
    if abs(b - c) < 0.000001:
        break
    b = c
b = "%.5f" % b
print(b)
# 用牛顿迭代法求得10的三次方根为2.15443（保留五位小数）
"""a = int(input())
b = a / 2
while abs(b**3 - a) > 0.000001:
    if (b**3) > a:
        b = b - b / 2
    else:
        b = b + b / 2
b = "%.5f" % b
print(b)"""
