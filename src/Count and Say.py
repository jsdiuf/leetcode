"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-29 23:32
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = [1]
        for i in range(n - 1):
            ch = []
            begin = ans[0]
            cnt = 0
            for idx, s in enumerate(ans):
                if s == begin:
                    cnt += 1
                    continue
                ch.append(cnt)
                ch.append(ans[idx - 1])
                begin = s
                cnt = 1
            ch.append(cnt)
            ch.append(ans[-1])
            ans = ch
        ret = ""
        for e in ans:
            ret += str(e)
        return ret


s = Solution()

for i in range(25):
    print(s.countAndSay(i + 1))
