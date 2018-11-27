"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-27 9:50
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        [1,2,3,4,5], popped = [4,5,3,2,1]

        [1,2,3,4,5], popped = [4,3,5,1,2]

        [0,2,1] [0,1,2]
        """

        i, idx = 0, 0
        temp = []

        while i < len(popped):
            if temp and temp[-1] == popped[i]:
                temp = temp[:-1]
                i += 1
            else:
                while idx < len(pushed) and pushed[idx] != popped[i]:
                    temp.append(pushed[idx])
                    idx += 1
                if idx < len(pushed):
                    temp.append(pushed[idx])
                    idx += 1
                else:
                    return False
        return len(temp) == 0


s = Solution()
print(s.validateStackSequences([0,2,1], [0,1,2]))
