"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-6 16:25
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def hasPath(node, s):
            if not node:
                return False
            if s + node.val == sum and not node.left and not node.right:
                return True
            return hasPath(node.left,s+node.val) or hasPath(node.right,s+node.val)
        return hasPath(root,0)


s=Solution()
a=TreeNode(-2)
b=TreeNode(-3)
c=TreeNode(-3)
d=TreeNode(4)
e=TreeNode(5)

#a.left=b
a.right=c

#b.left=d
#b.right=e

print(s.hasPathSum(a,-5))
