"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-17 10:29
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are
only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = list(s)
        stack = []
        for c in s:
            if c.isalpha():
                if not stack or (str(stack[-1])).isdigit():
                    stack.append(c)
                else:
                    stack[-1] += c
            if c.isdigit():
                if not stack or not (str(stack[-1])).isdigit():
                    stack.append(int(c))
                else:
                    stack[-1] *= 10
                    stack[-1] += int(c)
            if c == ']':
                s = stack.pop()
                n = stack.pop()
                if not stack:
                    stack.append(s * n)
                    continue
                if stack[-1].isalpha():
                    stack[-1] += s * n
        return stack[0]


s = Solution()
print(s.decodeString("2[ab3[e2[r]]]"))
