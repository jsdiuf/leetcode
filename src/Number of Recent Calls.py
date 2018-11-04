"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-4 9:33
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.



Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]


Note:

Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
"""


class RecentCounter:

    def __init__(self):
        self.arr = []
        self.p = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.arr.append(t)
        while self.arr[-1] - self.arr[self.p] > 3000:
            self.p += 1
        return len(self.arr) - self.p


s = RecentCounter()
print(s.ping(1))
print(s.ping(100))
print(s.ping(3001))
print(s.ping(3002))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
