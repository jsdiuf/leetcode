"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 23:46
"""

# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret = []
        q = queue.Queue()

        q.put(root)
        while not q.empty():

            n = q.qsize()
            t = []
            while n > 0:
                node = q.get()
                t.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                n -= 1
            ret.append(t)

        return ret


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

f.left = b
f.right = g

b.left = a
b.right = d

d.left = c
d.right = e

g.right = i
i.left = h

s = Solution()
print(s.levelOrder(f))
