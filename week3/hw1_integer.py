n = int(input())


def find_max_array(n):
    x = n % 3
    y = int(n / 3)
    result = []
    if x == 0:
        for i in range(y):
            result.append(3)
    # 取余还有1说明这个n中一定包含一个4，即2*2
    elif x == 1:
        result.append(2)
        result.append(2)
        # 范围到y-1是因为前面已经拿掉一个4（3+1）了，其中包含一个3
        for i in range(y - 1):
            result.append(3)
    else:
        result.append(2)
        for i in range(y):
            result.append(3)
    return result


print(find_max_array(n))
