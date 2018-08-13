"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-13 0:38
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for i in range(10000)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        k = self.hashFun(key)
        if not self.contains(key):
          self.arr[k].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        k = self.hashFun(key)
        if key in self.arr[k]:
            idx=self.arr[k].index(key)
            del self.arr[k][idx]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        k = self.hashFun(key)
        return key in self.arr[k]

    def hashFun(self,key):
        return key//100

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
#obj.remove(1)
param_3 = obj.contains(1)
print(param_3)