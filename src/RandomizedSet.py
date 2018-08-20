"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-20 9:47
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.set:
            t = random.randint(0, len(self.set) - 1)
            for val in self.set:
                if t == 0:
                    return val
                t -= 1
        return None


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(10)
obj.insert(20)
obj.insert(30)
for i in range(100):
    print(obj.getRandom())
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
