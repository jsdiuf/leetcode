"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2019/1/6 12:06
Given two non-negative integers x and y, an integer is powerful
if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.



Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""
import math


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if x == 1 and y == 1:
            return [2] if bound >= 2 else []
        if x == 1:
            jtop = int(math.log(bound - 1, y))
            return [1 + y ** j for j in range(jtop+1)]
        if y == 1:
            itop = int(math.log(bound - 1, x))
            return [1 + x ** i for i in range(itop+1)]

        ans = set()
        itop = int(math.log(bound - 1, x))
        jtop = int(math.log(bound - 1, y))
        for i in range(itop+1):
            for j in range(jtop+1):
                t = x ** i + y ** j
                if t <= bound:
                    ans.add(t)
                else:
                    break
        return list(ans)


s = Solution()
print(s.powerfulIntegers(1, 2, 100))
