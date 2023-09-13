# 给定数组
L = input()
# 将输入的每个数用逗号隔开做成数组
L = [int(n) for n in L.split(",")]
latter_L = []

# 方法一，for循环"D:\Git\mingw64\bin\git.exe"
"""for element in L:
    latter_L.insert(0, element)"""

# 方法一，while循环
length = len(L)
while length > 0:
    latter_L.append(L[length - 1])
    length -= 1


# 输出
print(latter_L)
