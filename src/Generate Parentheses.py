"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-3 15:22
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        self.exec(list, "(", n - 1, n)
        return list

    def exec(self, list, str, l, r):
        if l == 0:
            str = str + ")" * r
            if str not in list:
                list.append(str)
            return

        if r >= l:
            self.exec(list, str + "(", l - 1, r)
            self.exec(list, str + ")", l, r - 1)

    def generateParenthesis2(self, n):
        list = []

        #str 任意时刻右括号数量不能大于左括号  left（str中左括号的数量） right（str中右括号的数量）
        def backtrack(str="", left=0, right=0):
            if len(str) == n * 2:
                list.append(str)
                return

            if left < n:
                backtrack(str + "(", left + 1, right)
            if right < left:
                backtrack(str + ")", left, right + 1)

        backtrack()
        return list


s = Solution()
print(s.generateParenthesis2(3))
