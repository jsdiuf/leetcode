"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-7 11:17
"""

# Definition for binary tree with next pointer.
import queue


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            n = q.qsize()
            arr = []
            while n > 0:
                node = q.get()
                arr.append(node)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                n -= 1

            for i in range(len(arr)):
                if i == len(arr) - 1:
                    arr[i].next = None
                else:
                    arr[i].next = arr[i + 1]

    # recursion
    def connect2(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect2(root.left)
            self.connect2(root.right)

    def connect3(self, root):
        if root and (root.left or root.right):
            if root.left and root.right:
                root.left.next = root.right
            if root.next:
                l = root.right if root.right else root.left

                nnode = root.next
                while nnode:
                    if nnode.left:
                        l.next = nnode.left
                        break
                    if nnode.right:
                        l.next = nnode.right
                        break
                    nnode = nnode.next

            # first right side  then left side
            self.connect3(root.right)
            self.connect3(root.left)



n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n4 = TreeLinkNode(4)
n5 = TreeLinkNode(5)
n6 = TreeLinkNode(6)
n7 = TreeLinkNode(7)
n8 = TreeLinkNode(8)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right=n5

# n3.left=n6
n3.right = n6

n4.left=n7

n6.right=n8

s = Solution()
s.connect3(n1)
print(1)
