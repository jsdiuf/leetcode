"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 20:42
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1 - l2 + 1):
            if haystack[i:i + l2] == needle:
                return i
        return -1


s = Solution()
print(s.strStr("abcdefg", "a"))
