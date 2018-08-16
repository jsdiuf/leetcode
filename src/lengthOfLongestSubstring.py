"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 11:10
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        pwwkew
        """
        if not s:
            return 0
        dic = {}
        # means 不存在重复字符的子字符的开始位置
        i = 0
        maxlen = 0
        for idx, val in enumerate(s):
            if val in dic:
                i = max(i, dic[val] + 1)
            dic[val] = idx
            maxlen = max(maxlen, idx - i + 1)
        return maxlen


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
