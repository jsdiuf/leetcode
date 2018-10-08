"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 9:11
基本排序算法
"""


class Solution:
    # quicksort O(N*logN)
    def quicksort(self, nums, l, r):

        def sub_sort(array, l, r):
            key = array[l]
            while l < r:
                while l < r and array[r] >= key:
                    r -= 1
                while l < r and array[r] < key:
                    array[l] = array[r]
                    l += 1
                    array[r] = array[l]
            array[l] = key
            return l

        if l < r:
            m = sub_sort(nums, l, r)
            self.quicksort(nums, l, m)
            self.quicksort(nums, m + 1, r)

    def quicksort2(self, qlist):

        if not qlist:
            return []
        else:
            qfirst = qlist[0]
            qless = self.quicksort2([l for l in qlist[1:] if l < qfirst])
            qmore = self.quicksort2([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore

    def quicksort3(self,nums):
        return [] if not nums else self.quicksort3([i for i in nums[1:] if i<nums[0]])+nums[0:1]+self.quicksort3([i for i in nums[1:] if i>=nums[0]])


s = Solution()
a = [2, 6, 3, 8, 1, 7, 4, 9, 5, 5, 6]
print(s.quicksort3(a))
print(a)