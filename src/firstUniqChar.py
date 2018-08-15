"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 9:40
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        leetcode
        loveleetcode
        """
        dic = {}
        for e in s:
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] += 1
        for e in s:
            if dic[e] == 1:
                return s.index(e)
        return -1

        """
        res = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            left_idx = s.find(c)
            if left_idx != -1:
                right_idx = s.rfind(c)
                if left_idx == right_idx:
                    res = min(res, left_idx)
        return res if res < len(s) else -1
        """


s = Solution()
print(s.firstUniqChar("loveleetcode"))
