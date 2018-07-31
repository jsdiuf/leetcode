"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-7-31 10:47
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic1 = {'M': 1000,
                'D': 500, 'C': 100,
                'L': 50, 'X': 10,
                'V': 5, 'I': 1}
        dic2 = {
            'CM': 900, 'CD': 400,
            'XC': 90, 'XL': 40,
            'IX': 9, 'IV': 4, }
        ret = 0
        while len(s) > 0:
            if s[:2] in dic2.keys():
                ret += dic2[s[:2]]
                s = s[2:]
            else:
                ret += dic1[s[:1]]
                s = s[1:]

        return ret


s = Solution()
print(s.romanToInt("MCMXCIV"))
