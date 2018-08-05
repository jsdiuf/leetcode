"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-4 2:13
"""
import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        reduce=len(nums)-k
        while reduce>0:
            heapq.heappop(self.heap)
            reduce-=1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
           heapq.heappop(self.heap)
        return self.heap[0]


s=KthLargest(2,[1])
print(s.add(-3))
print(s.add(-2))
print(s.add(-4))
print(s.add(0))
print(s.add(4))
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)