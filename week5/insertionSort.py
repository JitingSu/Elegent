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
    print("插入排序结果如下：")
    print(nums)  # 输出排序后的数据
    
nums = [9,5,7,2,1,3,6]
insertion_sort(nums)