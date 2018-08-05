"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 10:35
"""


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        nums=0
        i=0
        j=len(people)-1

        while i<=j:
            if people[i]+people[j]>limit:
                nums+=1
                j-=1
                continue
            else:
                nums+=1
                i+=1
                j-=1
        return nums


s=Solution()
print(s.numRescueBoats([3,5,3,4],5))