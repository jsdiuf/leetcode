"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-13 1:13
"""


class Buckets:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * 10000

    def hash(self, key):
        return key // 100

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashval = self.hash(key)
        if not self.buckets[hashval]:
            self.buckets[hashval] = Buckets(key, value)
        else:
            cur = self.buckets[hashval]
            pre = None
            while cur:
                if cur.key == key:
                    cur.val = value
                    return
                pre = cur
                cur = cur.next
            pre.next = Buckets(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashval = self.hash(key)
        cur = self.buckets[hashval]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashval = self.hash(key)
        cur = self.buckets[hashval]

        # 不存在该key值
        if not cur:
            return
        if cur.key == key:
            self.buckets[hashval] = cur.next
            return
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
print(obj.get(1))
obj.put(1, 3)
print(obj.get(1))
obj.remove(1)
print(obj.get(1))
