"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-8 9:51
"""

# Definition for a binary tree node.
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        list = []
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            list.append(node.val if node else None)
            if node:
                q.put(node.left)
                q.put(node.right)
        while  list[-1] is None:
            list = list[:-1]
        return list

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None

        li = data

        le = len(li)
        root = TreeNode(li[0])
        q = queue.Queue()
        q.put(root)
        i = 1

        while not q.empty():
            n = q.qsize()

            while n > 0:
                node = q.get()
                if i < le:
                    if li[i] is not None:
                        left = TreeNode(li[i])
                        node.left = left
                        q.put(left)
                    i += 1
                if i < le:
                    if li[i] is not None:
                        right = TreeNode(li[i])
                        node.right = right
                        q.put(right)
                    i += 1
                n -= 1
        return root
        # print(li)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(0)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)

n1.left = n2
n1.right = n3

n2.left = n4
#n3.right = n5

s = Solution()
#s.serialize()
h = s.deserialize(s.serialize(n1))
print(1)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
