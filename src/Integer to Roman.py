"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-7-31 9:53
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        q = num // 1000
        num = num - q * 1000
        b = num // 100
        num = num - b * 100
        s = num // 10
        num = num - s * 10
        g = num % 10

        ret = ""
        if q > 0:
            while q > 0:
                ret += "M"
                q -= 1
        if b > 0:
            if b == 9:
                ret += "CM"
            elif b >= 5:
                ret += "D"
                while b > 5:
                    ret += "C"
                    b -= 1
            elif b == 4:
                ret += "CD"
            else:
                while b > 0:
                    ret += "C"
                    b -= 1

        if s > 0:
            if s == 9:
                ret += "XC"
            elif s >= 5:
                ret += "L"
                while s > 5:
                    ret += "X"
                    s -= 1
            elif s == 4:
                ret += "XL"
            else:
                while s > 0:
                    ret += "X"
                    s -= 1

        if g > 0:
            if g == 9:
                ret += "IX"
            elif g >= 5:
                ret += "V"
                while g > 5:
                    ret += "I"
                    g -= 1
            elif g == 4:
                ret += "IV"
            else:
                while g > 0:
                    ret += "I"
                    g -= 1

        return ret


s=Solution()
print(s.intToRoman(1994))