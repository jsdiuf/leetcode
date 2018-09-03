"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-3 22:25
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
 and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        hello  ll
        """
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        l1, l2 = len(haystack), len(needle)

        def helper(i):
            for j in range(l2):
                if needle[j] != haystack[i + j]:
                    return False
            return True

        for i in range(l1 - l2 + 1):
            if haystack[i] == needle[0] and helper(i):
                return i
        return -1

s=Solution()
print(s.strStr("hello","dwewefwf"))
