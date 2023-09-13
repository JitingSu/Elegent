num = float(input())


def calculation(num):
    if num < 0:
        temp = -num
    else:
        temp = num
    # 最大允许误差
    measure = 0.000001
    low = 0
    # 先假设三次方根与数的一半差不多大
    high = temp / 2
    while abs(high * high * high - temp) > measure:
        if (high * high * high) > temp:
            high = high - (high - low) / 2
        else:
            high = high + (high - low) / 2
    return high


if num > 0:
    print("%.6lf" % calculation(num))
else:
    print("%.6lf" % -calculation(num))
