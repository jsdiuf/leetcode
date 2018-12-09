"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-12-9 10:59
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.



Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false


Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        arr_1, arr0, arr1 = [], [], []
        for i in A:
            if i < 0:
                arr_1.append(i)
            if i == 0:
                arr0.append(i)
            if i > 0:
                arr1.append(i)
        if len(arr_1) % 2 != 0 or len(arr0) % 2 != 0 or len(arr1) % 2 != 0:
            return False
        arr_1.sort(reverse=True)
        arr1.sort()

        def helper(arr):
            if not arr:
                return True
            map = {}
            for e in arr:
                if e not in map:
                    map[e] = 1
                else:
                    map[e] += 1
            for e in arr:
                if map[e] == 0:
                    continue
                if map[e] > 0:
                    if 2 * e not in map or map[2 * e] == 0:
                        return False
                    else:
                        map[e] -= 1
                        map[2 * e] -= 1
            return True

        return helper(arr_1) and helper(arr1)


s = Solution()
print(s.canReorderDoubled([1, 2, 4, 8]))