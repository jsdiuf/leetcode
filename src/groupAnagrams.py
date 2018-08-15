"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 11:07
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for str in strs:
            sortStr = "".join(sorted(str))
            if sortStr not in dic:
                dic[sortStr] = [str]
            else:
                dic[sortStr].append(str)
        return [dic[i] for i in dic]


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
