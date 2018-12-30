"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/30 10:45
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false


Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

        arr = []

        def helper(node, arr):
            if node:
                arr.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root, arr)

        for i in range(1, len(arr)):
            if arr[i] != arr[0]:
                return False
        return True
