# 输出1到100之间的所有偶数
list = []
for i in range(1, 101):
    if i % 2 == 0:
        list.append(i)
print(list)
