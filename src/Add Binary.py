"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-1 20:43
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            sum += int(a[i]) if i >= 0 else 0
            sum += int(b[j]) if j >= 0 else 0
            ans.append(str(sum % 2))
            carry = sum // 2
            i -= 1
            j -= 1
        if carry:
            ans.append("1")
        return "".join(ans[::-1])


s = Solution()
print(s.addBinary("1010", "1011"))
