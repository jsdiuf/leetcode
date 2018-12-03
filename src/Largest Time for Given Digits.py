"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-12-3 9:19
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
"""


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        arr = []

        def valid(item):
            if item[0] >= 3:
                return False
            if item[0] == 2 and item[1] >= 4:
                return False
            if item[2] >= 6:
                return False
            return True

        def backtrack(t, remain):
            if not remain and valid(t):
                arr.append(t)
                return
            for i in range(len(remain)):
                backtrack(t + [remain[i]], remain[:i] + remain[i + 1:])

        backtrack([], A)
        if not arr:
            return ""

        def bigger(arr1, arr2):
            for i in range(4):
                if arr1[i] > arr2[i]:
                    return True
                if arr2[i] > arr1[i]:
                    return False
            return True

        ans = arr[0]
        for i in range(1, len(arr)):
            if bigger(arr[i], ans):
                ans = arr[i]
        return str(ans[0]) + str(ans[1]) + ":" + str(ans[2]) + str(ans[3])


s = Solution()
print(s.largestTimeFromDigits([1, 9,6,0]))
