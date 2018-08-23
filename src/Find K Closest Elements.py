"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-23 14:56

Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers).
Please reload the code definition to get the latest changes.
"""


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        def findclosed():
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == x:
                    return m
                if arr[m] < x < arr[m + 1]:
                    if x - arr[m] <= arr[m + 1] - x:
                        return m
                    else:
                        return m + 1
                if m - 1 > -1 and arr[m - 1] < x < arr[m]:
                    if x - arr[m - 1] <= arr[m] - x:
                        return m - 1
                    else:
                        return m
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m - 1

        m = findclosed()

        l, r = m, m
        while r - l + 1 < k:
            while l > 0 and r < len(arr) - 1 and r - l + 1 < k and (x - arr[l - 1]) <= (arr[r + 1] - x):
                l -= 1
            while l > 0 and r < len(arr) - 1 and r - l + 1 < k and (x - arr[l - 1]) > (arr[r + 1] - x):
                r += 1
            if l == 0:
                return arr[:k]
            if r == len(arr) - 1:
                return arr[-k:]
        return arr[l:r + 1]


s = Solution()
print(s.findClosestElements([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2))
