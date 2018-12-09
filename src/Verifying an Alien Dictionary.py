"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-12-9 10:34
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""


class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        map = {}
        for i in range(len(order)):
            map[order[i]] = i

        for i in range(1, len(words)):
            str1, str2 = words[i - 1], words[i]

            i, j = 0, 0
            while i < len(str1) and j < len(str2):
                if map[str1[i]] < map[str2[j]]:
                    break
                if map[str1[i]] > map[str2[j]]:
                    return False
                i += 1
                j += 1
                if i == len(str1) and j != len(str2):
                    break
                if j == len(str2) and i != len(str1):
                    return False
        return True


s = Solution()
print(s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
