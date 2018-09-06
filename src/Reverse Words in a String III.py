"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-6 15:09
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        return ' '.join(w[::-1] for w in s.split())
        """
        if not s:
            return ""
        s = list(s)

        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        begin = []
        end = []

        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                begin.append(i)
            if s[i] != " " and (i == len(s) - 1 or s[i + 1] == " "):
                end.append(i)

        for i in range(len(begin)):
            reverse(begin[i], end[i])

        return "".join(s)

s=Solution()
print(s.reverseWords("  "))
