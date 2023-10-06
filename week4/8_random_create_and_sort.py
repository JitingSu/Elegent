# 随机生成多组长度递增的随机数列，使用不同的排序算法进行排序，并分析不同排序算法在不同长度数列下的运行效果
import random
import datetime
import copy

num = range(0, 100000)
# 随机地从指定列表中提取出1000个不同的元素，列表的维数没有限制
nums = random.sample(num, 1000)
# print(nums)
# 将nums深度复制为5份
# 深度复制是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。因此，新对象和原对象没有任何关联.
nums0 = copy.deepcopy(nums)
nums1 = copy.deepcopy(nums)
nums2 = copy.deepcopy(nums)
nums3 = copy.deepcopy(nums)
nums4 = copy.deepcopy(nums)


# 选择排序
# 工作原理：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，继续放在起始位置直到未排序元素个数为0。
def select_sort(nums):
    for i in range(len(nums)):
        min_num = i
        for j in range(i + 1, len(nums)):
            if nums[min_num] > nums[j]:
                nums[j], nums[min_num] = nums[min_num], nums[j]
    # print("选择排序结果如下：")
    # print(nums)




# 归并排序
def mergesort(nums):
    if len(nums) <= 1:
        return nums
    else:
        count = int(len(nums) / 2)
        left = mergesort(nums[:count])
        right = mergesort(nums[count:])
        return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 剩余的数也要加上
    # list()函数是Python的内置函数。它可以将任何可迭代数据转换为列表类型，并返回转换后的列表。
    result += list(left[l:])
    result += list(right[r:])
    return result
# print(mergesort(nums))


# 冒泡排序
# 每进行一轮“冒泡”，需要比较的元素都少一个
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # print("冒泡排序结果如下：")
    # print(nums)


# 快速排序
def quick_sort(nums):
    if len(nums) < 2:
        return nums
    else:
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


# 插入排序
def insertion_sort(nums):
    # 从1开始是因为已经将0位置的元素当做已排序的数
    for i in range(1, len(nums)):
        # 设置当前需要插入的元素
        current = nums[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        # while循环中依次比较当前元素与它之前的数的大小关系
        while pre_index >= 0 and nums[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            nums[pre_index + 1] = nums[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
            # 当比较元素小于当前元素 则把当前元素插入在其后
            nums[pre_index + 1] = current
    # print("插入排序结果如下：")
    # print(nums)  # 输出排序后的数据


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
    # print("希尔排序结果如下：")
    # print(nums)

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
    bubble_sort(nums2)
    end2 = datetime.datetime.now()  # 记录冒泡排序结束的时刻
    print('冒泡排序运行时间为: %s.%s 秒' % ((end2 - start2).seconds, (end2 - start2).microseconds))  # 输出冒泡排序时间
    t2 = end2 - start2

    # 进行选择排序
    start3 = datetime.datetime.now()  # 记录选择排序开始的时刻
    select_sort(nums3)
    end3 = datetime.datetime.now()  # 记录选择排序结束的时刻
    print('选择排序运行时间为: %s.%s 秒' % ((end3 - start3).seconds, (end3 - start3).microseconds))  # 输出选择排序时间
    t3 = end3 - start3

    # 进行快速排序
    start4 = datetime.datetime.now()
    quick_sort(nums4)
    end4 = datetime.datetime.now()
    print('快速排序运行时间为: %s.%s 秒' % ((end4 - start4).seconds, (end4 - start4).microseconds))
    t4 = end4 - start4
    
main()

# 快速排序和归并排序通常在不同长度的数列上都表现良好（特别是在大型数列上）。
# 希尔排序在某些情况下表现良好，但是性能不稳定。
# 选择排序和冒泡排序在大型数列上性能较差。
# 插入排序在小型数列和接近有序的数列上性能较好，但在大型乱序数列上性能较差。