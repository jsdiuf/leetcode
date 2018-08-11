"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-10 11:14
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        """
        if not inorder:
            return None
        node = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return node


s=Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
h=s.buildTree(inorder,postorder)
print(1)
