import datetime
import random


# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


num = range(0, 10000)
# 随机地从指定列表中提取出1000个不同的元素，构造一个随机数组
nums = random.sample(num, 1000)
start = datetime.datetime.now()
bubble_sort(nums)
end = datetime.datetime.now()
print("运行时间为：%s.%s秒" % ((end - start).seconds, (end - start).microseconds))
