"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-8 10:08
Given a string S, return the "reversed" string where all characters that
are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        t = []
        for i in range(len(S)):
            if 'a' <= S[i] <= 'z' or 'A' <= S[i] <= 'Z':
                t.append(S[i])
        ans = list(S)
        for i in range(len(ans)):
            if 'a' <= ans[i] <= 'z' or 'A' <= ans[i] <= 'Z':
                ans[i] = t.pop()
        return "".join(ans)


s = Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
