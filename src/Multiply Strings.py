"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-31 10:06
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        123
          *
        456
        """
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0 for i in range(250)]

        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                m = int(num1[i]) * int(num2[j]) + carry
                carry = m // 10
                ans[len(num1) - i - 1 + len(num2) - j - 1] += m % 10
            ans[len(num1) - 1 - i + len(num2)] += carry
        for i in range(len(ans) - 1):
            if ans[i] >= 10:
                ans[i + 1] += ans[i] // 10
                ans[i] = ans[i] % 10
        res = ''
        ans.reverse()
        allzero = True
        for i in range(len(ans)):
            if ans[i] != 0:
                allzero = False
            if allzero:
                continue
            res += str(ans[i])
        return res



s = Solution()
print(s.multiply2("123", "456"))
