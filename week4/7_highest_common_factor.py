# 求两个正整数的最大公约数
a = int(input())
b = int(input())
# 创建两个变量存储a和b,为了在最后打印出a,b原来的值
m, n = a, b
# t作为储存最大公约数的载体
t = 1
for i in range(2, min(a, b)):
    while a % i == 0 and b % i == 0:
        # 所有公约数累乘起来
        t *= i
        a /= i
        b /= i
# 字符串前面加f表示格式化字符串，formatting，加f后可以在字符串里面使用{ }括起来的变量和表达式
print(f"{m},{n}的最大公约数为：{t}")
