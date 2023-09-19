# 牛顿迭代法
a = int(input())
b = a / 4
while True:
    # 牛顿迭代公式
    c = (b + a / b) / 2
    if abs(b - c) < 0.00001:
        break
    b = c
b = "%.5f" % b
print(b)
# 如果将起始值修改对结果有影响
