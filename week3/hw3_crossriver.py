name = ["farmer", "wolf", "sheep", "grass"]
scheme_count = 0


# 完成局面 判断条件，只有四者全过岸时status[]才全为true
def is_done(status):
    return status[0] and status[1] and status[2] and status[3]


# 生成下一个局面的所有情况
def create_all_next_status(status):
    # 创建一个新列表存放局面
    next_status_list = []
    for i in range(0, 4):
        # 如果和农夫不同一侧
        if status[0] != status[i]:
            # continue是提前结束本次循环，但会继续执行下一次的循环。
            continue
        # 提前记录局面状态
        next_status = [status[0], status[1], status[2], status[3]]
        # 农夫和其中一个过河，i 为 0 时候，农夫自己过河。
        # 农夫过河之后状态需要改变（false变true）
        next_status[0] = not next_status[0]
        # 和农夫一起过河，状态需要跟农夫一样改变
        next_status[i] = next_status[0]
        # 如果符合题目规则
        if is_valid_status(next_status):
            next_status_list.append(next_status)
    return next_status_list


# 判断是否合法的局面
def is_valid_status(status):
    if status[1] == status[2]:
        if status[0] != status[1]:
            # 狼和羊同侧，且这时农夫不在此侧
            return False

    if status[2] == status[3]:
        if status[0] != status[2]:
            # 羊和草同侧，且这时农夫不在此侧
            return False
    # 除了这两种情况，都对
    return True


def search(history_status):
    # 定义全局变量，使函数里面这个scheme_count变成全局变量
    global scheme_count
    # 找到现在进行到的局面current_status，history_status记录的是已经走过的每一步
    current_status = history_status[len(history_status) - 1]
    # 找到下一步的所有情况
    next_status_list = create_all_next_status(current_status)
    for next_status in next_status_list:
        # 如果出现重复的情况
        if next_status in history_status:
            continue
        history_status.append(next_status)
        if is_done(next_status):
            scheme_count += 1
            # scheme_count要用str括号起来是因为前面的"scheme "和后面的":"都是字符串形式
            print("scheme " + str(scheme_count) + ":")
            print_history_status(history_status)
        else:
            # 递归
            search(history_status)
        # 出栈
        history_status.pop()


def readable_status(status, is_across):
    result = ""
    for i in range(0, 4):
        # 判断status是在岸的哪一边
        if status[i] == is_across:
            if len(result) != 0:
                result += ","
            result += name[i]
    return "[" + result + "]"


# 打印结果
def print_history_status(history_status):
    for status in history_status:
        print(readable_status(status, False) + "≈≈≈≈≈≈≈≈≈≈" + readable_status(status, True))


# 程序开始的入口
if __name__ == "__main__":
    # 初始局面
    # 使用一个布尔数组表示它们的状态，布尔值状态 false 代表对应的人（物）还没有过河，状态 true 代表对应人（物）已经过河了
    status = [False, False, False, False]
    # 局面队列
    history_status = [status]
    # 对已知状态进行求解
    search(history_status)
    print("finish search, find " + str(scheme_count) + " scheme")
