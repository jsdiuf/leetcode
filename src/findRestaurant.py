"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 9:10
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {val: idx for idx, val in enumerate(list1)}
        ret = []
        leastindex = 0

        for idx, val in enumerate(list2):
            if val in dic:
                if not ret:
                    ret.append(val)
                    leastindex = idx + dic[val]
                elif idx + dic[val] == leastindex:
                    ret.append(val)
                elif idx + dic[val] < leastindex:
                    ret.clear()
                    ret.append(val)
                    leastindex = idx + dic[val]
        return ret


s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                       ["KFC", "Shogun", "Burger King"]))
