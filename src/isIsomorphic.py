"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 10:50
"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = dict()
        for idx, val in enumerate(s):
            if val in dic and t[idx] != t[dic[val]]:
                return False
            dic[val] = idx
        dic.clear()
        for idx, val in enumerate(t):
            if val in dic and s[idx] != s[dic[val]]:
                return False
            dic[val] = idx
        return True


s = Solution()
print(s.isIsomorphic("paper", "titll"))
