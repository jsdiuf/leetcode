"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 17:47
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.count:
            return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
         After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = TreeNode(val)
        node.next = self.head
        self.head = node
        self.count += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if not self.head:
            self.addAtHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = TreeNode(val)
        self.count += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.count:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        while index > 1:
            cur = cur.next
            index -= 1
        newNd = TreeNode(val)
        newNd.next = cur.next
        cur.next = newNd
        self.count += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.count == 0:
            return
        if index < 0 or index >= self.count:
            return
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            return
        cur = self.head
        while index > 1:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtIndex(1, 2)
print(obj.get(1))
print(obj.get(0))
print(obj.get(2))


