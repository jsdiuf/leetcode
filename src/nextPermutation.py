"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 0:16
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                p, q = i, len(nums) - 1
                while p < q:
                    nums[p], nums[q] = nums[q], nums[p]
                    p += 1
                    q -= 1
                t = i
                while nums[t] <= nums[i - 1]:
                    t += 1
                nums[t], nums[i - 1] = nums[i - 1], nums[t]
                return
        i, j = 0, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


s = Solution()
a = [1,2,3,6,5,4,3,2,1]
s.nextPermutation(a)
print(a)

"""
213
"""
