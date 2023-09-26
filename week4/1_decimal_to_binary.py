# 实现十进制向二进制的转换

def decimal_to_binary(number):
    # 定义一个栈
    stack = []
    # 定义最后输出的二进制字符串
    binary_string = ''
    while number > 0:
        # number取余的数进栈
        remain = number % 2
        stack.append(remain)
        # //相当于C语言中的/,向下取整
        number = number // 2
    while len(stack) > 0:
        binary_string += str(stack.pop())
    print(binary_string)


num = int(input())
decimal_to_binary(num)
