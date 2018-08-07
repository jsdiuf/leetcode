"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-7 9:59
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
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        node = TreeNode(preorder[0])

        rootindex = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:rootindex + 1], inorder[0:rootindex])
        node.right = self.buildTree(preorder[rootindex + 1:len(preorder)], inorder[rootindex + 1:len(inorder)])
        return node


# 前序遍历 preorder = [(3),9,20,15,7]
# 中序遍历 inorder = [9,(3),15,20,7]
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
root = s.buildTree(preorder, inorder)
print(1)
