# 方法一
# 初始化一个表
mylist = []
for i in range(100):
    if i % 2 != 0:
        # append() 方法用于在列表末尾添加新的对象。
        mylist.append(i)
print(mylist)

# 方法二
# Python的一个高级特性“切片”
# print(list(range(100))[1:100:2])

# 方法三
# 列表表达式
# print([x for x in range(100) if x % 2 != 0])
