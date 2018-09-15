"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-15 12:46
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        ans = []

        def backtrack(arr, lastindex, sum):
            if sum == target:
                ans.append(arr)
                return
            for i in range(lastindex, len(candidates)):
                if sum + candidates[i] > target:
                    break
                if i - 1 >= lastindex and candidates[i - 1] == candidates[i]:
                    continue
                backtrack(arr + [candidates[i]], i + 1, sum + candidates[i])

        backtrack([], 0, 0)
        return ans


s = Solution()
print(s.combinationSum2([1, 1, 2, 5, 6, 7, 10], 8))
