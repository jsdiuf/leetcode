"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-7-31 11:50
@url  https://leetcode.com/problems/longest-common-prefix/description/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        le = len(strs)
        if le == 0:
            return ""
        maxcom = strs[0]
        i = 1
        while i < le:
            maxcom = self.commonInTwo(maxcom, strs[i])
            i += 1
            if maxcom == "":
                return ""
        return maxcom

    def commonInTwo(self, str1, str2):
        if str2 == "":
            return ""
        len1 = len(str1)
        len2 = len(str2)

        i = 0
        while i < len1 and i < len2 and str1[i] == str2[i]:
            i += 1
        return str1[:i]


s = Solution()
print(s.longestCommonPrefix(["c","acc","bcc"]))
