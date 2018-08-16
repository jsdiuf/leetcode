"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 15:01
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 左旋
    def left_roate(self, P, pivot):
        if pivot.right:
            P.left = pivot.right
            pivot.right = pivot.right.left
            P.left.left = pivot


P = TreeNode("P")
pivot = TreeNode("pivot")
d = TreeNode("d")
a = TreeNode("a")
Y = TreeNode("Y")
b = TreeNode("b")
c = TreeNode("c")

P.left = pivot
P.right = d

pivot.left = a
pivot.right = Y
Y.left = b
Y.right = c

s = Solution()
s.left_roate(P, pivot)
print(1)
