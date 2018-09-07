"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-7 9:11
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
https://leetcode.com/problems/longest-valid-parentheses/solution/
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        ...()()...
        ...(())(())...
        """
        if not s:
            return 0
        L = len(s)

        ans = []
        maxL = 0
        for i in range(1, L):
            if s[i - 1] == "(" and s[i] == ")":
                ans.append([i - 1, i])
                maxL = 2
        if not maxL:
            return 0

        def helper1():
            change = False
            for i in range(len(ans)):
                while ans[i][0] - 1 >= 0 and ans[i][1] + 1 < L and s[ans[i][0] - 1] == "(" and s[ans[i][1] + 1] == ")":
                    ans[i][0] -= 1
                    ans[i][1] += 1
                    change = True
            return change

        def helper2():
            change = False
            for i in range(len(ans) - 1, 0, -1):
                if ans[i][0] == ans[i - 1][1] + 1:
                    ans[i - 1][1] = ans[i][1]
                    del ans[i]
                    change = True
            return change

        while 1:
            if not helper1() and not helper2():
                break

        for e in ans:
            maxL = max(maxL, e[1] - e[0] + 1)

        return maxL

    def longestValidParentheses2(self, s):
        stk = []
        stk.append(-1)
        l = len(s)
        r = 0
        for i in range(l):
            if s[i] == "(":
                stk.append(i)
            else:
                stk.pop()
                if len(stk) != 0:
                    r = max(r, i - stk[-1])
                else:
                    stk.append(i)
            print(stk)
        return r


s = Solution()
print(s.longestValidParentheses2(")(()())"))
