"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-19 18:49
"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        abbe cddf
        """

        def helper(word):
            if len(pattern) != len(word):
                return False
            map1 = {}
            map2 = {}
            for i in range(len(pattern)):
                if word[i] not in map1:
                    map1[word[i]] = pattern[i]
                if pattern[i] not in map2:
                    map2[pattern[i]] = word[i]
                if word[i] in map1 and map1[word[i]] != pattern[i]:
                    return False
                if pattern[i] in map2 and map2[pattern[i]] != word[i]:
                    return False
            return True

        return [word for word in words if helper(word)]


s = Solution()
print(s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
