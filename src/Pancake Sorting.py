"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2019/1/6 13:39
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length,
then reverse the order of the first k elements of A.
We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""


class Solution:
    def pancakeSort(self, A):
        """ [3,2,4,1]
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []

        if len(A) == 1:
            return []

        def findmaxindex(A, r):
            maxindex = 0
            for i in range(r + 1):
                if A[i] > A[maxindex]:
                    maxindex = i
            return maxindex

        for i in range(len(A) - 1, 1, -1):
            maxindex = findmaxindex(A, i)
            if maxindex == i:
                A = A[:i]
                continue
            ans.append(maxindex + 1)
            ans.append(i + 1)
            A = A[:maxindex + 1][::-1] + A[maxindex + 1:]
            A = A[::-1]
            A = A[:i]
        if len(A) >= 2 and A[0] > A[1]:
            ans.append(2)
        return ans


s = Solution()
print(s.pancakeSort([3, 2, 4, 1]))
