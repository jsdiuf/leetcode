"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-12-3 13:57
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        m, n, q = 0, 0, 0
        while seats[m] == 0 and m < len(seats):
            m += 1
        while seats[len(seats) - 1 - q] == 0 and q < len(seats):
            q += 1
        l, r = 0, 0
        while l < len(seats) and r < len(seats):
            while l < len(seats) and seats[l] == 1:
                l += 1
            r = l
            while r < len(seats) and seats[r] == 0:
                r += 1
            n = max(n, r - l)
            l = r
        return max(m, (n+1)//2, q)


s = Solution()
print(s.maxDistToClosest([1,0,0,0]))