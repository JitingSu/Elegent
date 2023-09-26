# 随机生成多组长度递增的随机数列，使用不同的排序算法进行排序
# 作为测试代码，需要修改以及再看

import random
# 计算程序运行时间的库
import datetime
# 深度复制列表的库
import copy

num = range(0, 1000000)  # 范围在0到100000之间，需要用到range()函数。
nums = random.sample(num, 10010)  # 选取10010个元素
print(nums)
# 将nums深度复制为5份
nums0 = copy.deepcopy(nums)
nums1 = copy.deepcopy(nums)
nums2 = copy.deepcopy(nums)
nums3 = copy.deepcopy(nums)
nums4 = copy.deepcopy(nums)


# 冒泡排序
def MP(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:  # 如果前面的数小于后面的数则交换二者的值
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print("冒泡排序结果如下：")
    print(nums)  # 输出排序后的数据


# 插入排序
def insertion_sort(nums):
    for i in range(1, len(nums)):  # for表示循环插入的遍数
        # 设置当前需要插入的元素
        current = nums[i]
        # 与当前元素比较的比较元素
        preindex = i - 1
        while preindex >= 0 and nums[preindex] > current:
            # 当比较元素大于当前元素则把比较元素后移
            nums[preindex + 1] = nums[preindex]
            # 往前选择下一个比较元素
            preindex -= 1
            # 当比较元素小于当前元素 则把当前元素插入在其后
            nums[preindex + 1] = current
    print("插入排序结果如下：")
    print(nums)  # 输出排序后的数据


# 希尔排序
def shell_sort(nums):
    n = len(nums)
    gap = n // 2  # 定义一个变量gap，确定分组长度
    while gap > 0:
        for i in range(gap, n):  # 开始插入排序
            current = nums[i]
            j = i - gap
            if j >= 0 and nums[j] > current:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = current  # 这里的j是减过gap后不满足循环条件，所以这里的j要加上gap

        gap //= 2  # 将源列表分成更小的组，继续排序
    print("希尔排序结果如下：")
    print(nums)


# 快速排序
def quick_sort(nums):
    if len(nums) >= 2:  # 进行快速排序
        mid = nums[len(nums) // 2]
        left = []
        right = []
        nums.remove(mid)
        for num in nums:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return nums


# 选择排序
def sort_list(nums):
    for i in range(len(nums)):  # 进行选择排序
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                nums[j], nums[min_index] = nums[min_index], nums[j]
    print("选择排序结果如下：")
    print(nums)


def main():
    # 进行插入排序
    start0 = datetime.datetime.now()  # 记录插入排序开始时刻的时间
    insertion_sort(nums0)
    end0 = datetime.datetime.now()  # 记录插入排序结束的时刻
    print('插入排序运行时间为: %s.%s 秒' % ((end0 - start0).seconds, (end0 - start0).microseconds))  # 将插入排序所需时间输出
    t0 = end0 - start0

    # 进行希尔排序
    start1 = datetime.datetime.now()  # 记录希尔排序开始的时刻
    shell_sort(nums1)
    end1 = datetime.datetime.now()  # 记录希尔排序结束的时刻
    print('希尔排序运行时间为: %s.%s 秒' % ((end1 - start1).seconds, (end1 - start1).microseconds))  # 输出希尔排序时间
    t1 = end1 - start1

    # 进行冒泡排序
    start2 = datetime.datetime.now()  # 记录冒泡排序开始的时刻
    MP(nums2)
    end2 = datetime.datetime.now()  # 记录冒泡排序结束的时刻
    print('冒泡排序运行时间为: %s.%s 秒' % ((end2 - start2).seconds, (end2 - start2).microseconds))  # 输出冒泡排序时间
    t2 = end2 - start2

    # 进行选择排序
    start3 = datetime.datetime.now()  # 记录选择排序开始的时刻
    sort_list(nums3)
    end3 = datetime.datetime.now()  # 记录选择排序结束的时刻
    print('选择排序运行时间为: %s.%s 秒' % ((end3 - start3).seconds, (end3 - start3).microseconds))  # 输出选择排序时间
    t3 = end3 - start3

    # 进行快速排序
    start4 = datetime.datetime.now()
    nums4q = quick_sort(nums4)
    end4 = datetime.datetime.now()
    print(nums4q)
    print('快速排序运行时间为: %s.%s 秒' % ((end4 - start4).seconds, (end4 - start4).microseconds))
    t4 = end4 - start4

    ls_1 = []  # 建立一个列表用来存放算法运行时间
    ls_1.append(t0)
    ls_1.append(t1)
    ls_1.append(t2)
    ls_1.append(t3)
    ls_1.append(t4)
    ls = copy.deepcopy(ls_1)
    sx = ['插入排序', '希尔排序', '冒泡排序', '选择排序', '快速排序']
    min1 = ls_1.index(min(ls_1))  # 找到运行赶时间最短算法对应的时间下标
    min_time1 = ls_1[min1]  # 记录下最快排序的时间
    min_name1 = sx[min1]  # 记录下最快排序的名字
    ls_1.pop(min1)  # 删除该时间，继续查找除了该算法之外的最优算法

    min2 = ls_1.index(min(ls_1))  # 找到除了已去除算法之外的最优算法的下标
    min_time2 = ls_1[min2]  # 记录下第二快排序的时间
    min_name2 = sx[min2]  # 记录下第二快排序的名字

    fw = open("E:\\Elegent\\time.txt", 'w')  # 建立一个txt文件用来存放最大增幅的月份
    fw.write("排序算法性能最好的算法是：%s，该算法所需时间为：%s.%s秒，" % (
        min_name1, min_time1.seconds, min_time1.microseconds))  # 将最优算法写入txt文件
    fw.write("其次性能最好的是：%s，该算法所需时间为：%s.%s秒" % (
        min_name2, min_time2.seconds, min_time2.microseconds))  # 将第二优算法写入txt文件
    fw.write("\n")
    fw.write("需要进行排序的序列为：")  # 将需要排序的序列保存至txt文件
    fw.write(str(nums))
    fw.write("\n\n")
    fw.write("排序后的序列为：")  # 将排序好的序列保存至txt文件
    fw.write(str(nums1))
    fw.write("\n")
    fw.write("每种排序算法所需时间如下：")
    fw.write("\n")
    i = 0
    for i in range(len(ls)):  # 输出每种算法的所需时间
        fw.write("%s所需时间为%s.%s秒\n" % (sx[i], ls[i].seconds, ls[i].microseconds))
    fw.close()


main()
