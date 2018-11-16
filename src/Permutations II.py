"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-16 14:59
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Seen this question in a real interview before?

"""


class Solution:
    #900ms
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        s = set()

        def backtrack(arr, index):
            if index == len(nums) - 1:
                s.add(",".join([str(c) for c in arr]))
            else:
                backtrack([nums[index + 1]] + arr, index + 1)
                for j in range(1, len(arr)):
                    backtrack(arr[:j] + [nums[index + 1]] + arr[j:], index + 1)
                backtrack(arr + [nums[index + 1]], index + 1)

        backtrack(nums[0:1], 0)
        ans = []
        for item in s:
            t = item.split(",")
            ans.append([int(i) for i in t])
        return ans


    #60ms
    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:return []
        if len(nums)==1:return [nums]
        tmp = []
        a = self.permuteUnique(nums[:-1])
        for i in a:
            for j in range(len(nums)):
                tmp+=[i[:j]+[nums[-1]]+i[j:]]
                if j<len(nums)-1 and i[j]==nums[-1]:break
        return tmp


s = Solution()
print(s.permuteUnique([2, 1, 1]))
