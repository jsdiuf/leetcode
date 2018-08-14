"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 9:11
基本排序算法
"""


class Solution:
    # quicksort O(N*logN)
    def quicksort(self, nums,start,end):

        # 判断low是否小于high,如果为false,直接返回
        if start < end:
            i, j = start, end
            # 设置基准数
            base = nums[i]

            while i < j:
                # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
                while (i < j) and (nums[j] >= base):
                    j = j - 1

                # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
                    nums[i] = nums[j]

                # 同样的方式比较前半区
                while (i < j) and (nums[i] <= base):
                    i = i + 1
                    nums[j] = nums[i]
            # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
                    nums[i] = base

            # 递归前后半区
            self.quicksort(nums, start, i - 1)
            self.quicksort(nums, j + 1, end)
        return nums


s = Solution()
a=[2, 6, 3, 8, 1, 7, 4, 9, 5, 5, 6]
print(s.quicksort(a,0,9))
print(a)
