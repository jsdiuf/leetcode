"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-11 20:39
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def gethight(nd):
            return 0 if not nd else max(gethight(nd.left), gethight(nd.right)) + 1

        if abs(gethight(root.left) - gethight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(3)
n6 = TreeNode(4)
n7 = TreeNode(4)

n1.left = n2
n1.right = n3

n2.left = n4
n3.right = n5

n4.left = n6
n5.right = n7

s = Solution()
print(s.isBalanced(n1))
