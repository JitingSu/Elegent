# 方法一


"""n = int(input())
ans = n
i = 1
if n == 0:
    print(1)
else:
    while i < n:
        ans = ans * i
        i = i + 1
    print(ans)"""

# 方法二


def factorial(n):
    if n == 0:
        return 1
    else:
        # 递归调用
        return factorial(n - 1) * n


n = int(input())
print(factorial(n))
