"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-28 22:42
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        [1,2,3,(3),4,(4),5,(5),6,(6),7,(7),8,(8),(9)]
        [3,4,5,6,7,8,9]
        """
        le1 = len(nums1)
        le2 = len(nums2)
        if not nums1:
            return (nums2[le2 // 2] + nums2[(le2 - 1) // 2]) / 2
        if not nums2:
            return (nums1[le1 // 2] + nums1[(le1 - 1) // 2]) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 2, 3, 4], []))
