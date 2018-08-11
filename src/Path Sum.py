"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-10 9:18
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

        def recur(node, s):
            if not node:
                return False
            if node.val == s and not node.left and not node.right:
                return True
            return recur(node.left, s - node.val) or recur(node.right, s - node.val)
        return recur(root, sum)


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(1)

n1.left = n2
n1.right = n3

n2.left = n4

n3.left = n5
n3.right = n6

n4.left = n7
n4.right = n8

n6.right = n9
s = Solution()
print(s.hasPathSum(n1, 22))
