"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-3 9:47
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {"(": -3, "{": -2, "[": -1, "]": 1, "}": 2, ")": 3}
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for e in s:
            n = len(stack)
            # not empty
            if map[e] < 0:
                stack.append(e)
                continue
            if n > 0 and map[stack[n - 1]] + map[e] == 0:
                stack.pop()
                continue
            return False
        return len(stack) == 0

    def isValid2(self, s):
        """
        ([)]
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0

    def isValid3(self, s):
        """这也行！！！！！
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        if n % 2 != 0:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')
        return s == ''


s = Solution()
print(s.isValid("{{}[()][]}"))
