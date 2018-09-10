"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-10 21:12
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if not candidates or min(candidates) > target:
            return []
        ans = []

        def backtrack(cur=[], sum=0):
            if sum == target:
                ans.append(cur)
            if target > sum:
                for num in candidates:
                    if num + sum > target:
                        break
                    # 保证递增
                    if cur and cur[-1] < num:
                        continue
                    # cur + [num] 就不是引用传递了   cur.append(num) 再传cur 不行的
                    backtrack(cur + [num], sum + num)

        ans = []
        backtrack()
        return ans


s = Solution()
print(s.combinationSum([3, 12, 9, 11, 6, 7, 8, 5, 4],
                       15))
