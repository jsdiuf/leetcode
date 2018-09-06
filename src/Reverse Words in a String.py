"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-6 14:13
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string
should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""
        s = list(s)

        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        while s and s[-1] == " ":
            del s[-1]
        while s and s[0] == " ":
            del s[0]
        if not s:
            return ""
        for i in range(len(s) - 2, -1, -1):
            if s[i] == " " and s[i + 1] == " ":
                del s[i + 1]

        reverse(0, len(s) - 1)
        emptyindex = []
        for i in range(len(s)):
            if s[i] == " ":
                emptyindex.append(i)
        if not emptyindex:
            reverse(0, len(s) - 1)
            return "".join(s)

        reverse(0, emptyindex[0] - 1)
        reverse(emptyindex[-1] + 1, len(s) - 1)
        for i in range(1, len(emptyindex)):
            reverse(emptyindex[i - 1] + 1, emptyindex[i] - 1)

        return "".join(s)


s = Solution()
print(s.reverseWords("abc "))
