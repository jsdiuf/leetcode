"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-8 14:01
"""


# Definition for a binary tree node. {binary search tree (BST)}
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur(node, list):
            if node.left:
                recur(node.left, list)
            list.append(node.val)
            if node.right:
                recur(node.right, list)

        list = []
        recur(root, list)
        for i in range(len(list) - 1):
            if list[i] >= list[i + 1]:
                return False
        return True




n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(15)
n4 = TreeNode(6)
n5 = TreeNode(20)

n1.left = n2
n1.right = n3

n3.left = n4
n3.right = n5

s = Solution()
print(s.isValidBST(n1))
