w = int(input("第一个数:"))
x = int(input("第二个数:"))
y = int(input("第三个数:"))
z = int(input("第四个数:"))
a = {"w": w, "x": x, "y": y, "z": z}
# sorted() 作为Python 内置函数之一，其功能是对序列（列表、元组、字典、集合、还包括字符串）进行排序。
for i in sorted(a, key=a.get):
    # 打印新的已排序过后的列表
    print(a[i], end=' ')
