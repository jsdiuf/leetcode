# https://leetcode.com/problems/regular-expression-matching/description/
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        for i in arr:
            while "**" in p or ".*.*" in p or i + "*" + i + "*" in p:
                p = p.replace("**", "*")
                p = p.replace(".*.*", ".*")
                p = p.replace(i + "*" + i + "*", i + "*")
        return self.judge(s, p)

    def judge(self, s, p):

        if s == "" and p == "":
            return True
        if s != "" and p == "":
            return False

        # a
        if len(p) == 1 and p[0].islower() and len(s) > 0 and p[0] == s[0]:
            return self.judge(s[1:], p[1:])
        # aa
        if len(p) > 1 and p[0].islower() and p[1].islower() and len(s) > 0 and p[0] == s[0]:
            return self.judge(s[1:], p[1:])
        # a*
        if len(p) > 1 and p[0].islower() and p[1] == "*":
            if self.judge(s, p[2:]):
                return True
            while s != "" and s[0] == p[0]:
                if self.judge(s[1:], p[2:]):
                    return True
                s = s[1:]
            return False
        # a.
        if len(p) > 1 and p[0].islower() and p[1] == "." and len(s) > 0 and p[0] == s[0]:
            return self.judge(s[1:], p[1:])

        # .*
        if len(p) > 1 and p[0:2] == ".*":
            if self.judge(s, p[2:]): return True
            while s != "":
                if self.judge(s[1:], p[2:]):
                    return True
                s = s[1:]
            return False
        # ..
        if len(p) > 1 and p[0:2] == ".." and len(s) > 0:
            return self.judge(s[1:], p[1:])

        # .a
        if len(p) > 1 and p[0] == "." and p[1].islower() and len(s) > 0:
            return self.judge(s[1:], p[1:])

        # .
        if len(p) == 1 and p[0] == "." and len(s) > 0:
            return self.judge(s[1:], p[1:])
        return False

    def dp(self, st, p):
        return


s = Solution()
print(s.isMatch("a", ".*.."))
