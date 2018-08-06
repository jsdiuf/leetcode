"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-6 10:26
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right))+1


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

print(s.maxDepth(f))
