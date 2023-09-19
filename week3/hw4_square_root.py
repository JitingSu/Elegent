# “笨”方法
num = int(input())
temp = num
# 最大允许误差
measure = 0.000001
low = 0
# 先假设二次方根与数的一半差不多大
high = temp / 2
while abs(high * high - temp) > measure:
    # 如果假设的值大于实际值，则执行
    if (high * high) > temp:
        high = high - (high - low) / 2
    # 如果假设的值小于实际值，则执行
    else:
        high = high + (high - low) / 2
high = "%.5f" % high
print(high)

