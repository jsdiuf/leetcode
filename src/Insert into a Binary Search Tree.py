"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-8 16:04
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursion
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        def recur(node):
            if val < node.val:
                if node.left:
                    recur(node.left)
                else:
                    node.left = TreeNode(val)
            if val > node.val:
                if node.right:
                    recur(node.right)
                else:
                    node.right = TreeNode(val)

        recur(root)

        return root

    def insertIntoBST2(self, root, val):

        if not root:
            return TreeNode(val)

        node = root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            if val > node.right:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root
