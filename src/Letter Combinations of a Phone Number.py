"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-2 10:05
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        list = [map[digits[0]][0], map[digits[0]][1], map[digits[0]][2]]
        if len(map[digits[0]]) > 3:
            list.append(map[digits[0]][3])
        i = 1
        while i < len(digits):
            t = []
            for c in map[digits[i]]:
                for e in list:
                    t.append(e + c)
            list = t
            i += 1
        return list


s = Solution()
s.letterCombinations("22")
