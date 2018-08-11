"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-10 14:38
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        """
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:idx + 1], inorder[0:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node


s=Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
h=s.buildTree(preorder,inorder)
print(1)

