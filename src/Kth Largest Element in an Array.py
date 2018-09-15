"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-15 15:09
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = [-float('inf')] * k
        heapq.heapify(h)

        for i in nums:
            if h[0] < i:
                heapq.heappop(h)
                heapq.heappush(h, i)
        return h[0]


s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
