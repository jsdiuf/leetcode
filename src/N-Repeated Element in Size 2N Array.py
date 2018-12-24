"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/23 10:33
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
"""


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        map = {}
        for e in A:
            if e not in map:
                map[e] = 1
            else:
                map[e] += 1
                if map[e] == len(A) // 2:
                    return e


s = Solution()
print(s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
