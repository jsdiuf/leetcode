"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 23:09
"""


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        # length of words
        n = len(words)

        # length of items
        l = len(words[0])

        wordsmap = {}
        for e in words:
            if e not in wordsmap:
                wordsmap[e] = 1
            else:
                wordsmap[e] += 1

        def judge(str):
            i = 0
            substrmap = {}
            while i < len(str):
                substr = str[i:i + l]
                if substr not in substrmap:
                    substrmap[substr] = 1
                else:
                    substrmap[substr] += 1
                i += l
            for e in wordsmap:
                if e not in substrmap or wordsmap[e] != substrmap[e]:
                    return False
            return True

        ret = []
        for i in range(len(s) - n * l + 1):
            if judge(s[i:i + n * l]):
                ret.append(i)
        return ret


s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
