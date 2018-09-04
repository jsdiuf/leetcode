"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-4 17:28
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        i, j = 0, len(s) - 1
        arr=list(s)
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return "".join(arr)


s = Solution()
print(s.reverseString("a"))
