"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-7 9:19
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
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        node = TreeNode(postorder[-1])

        rootindex = (inorder).index(postorder[-1])
        node.left = self.buildTree(inorder[0:rootindex], postorder[0:rootindex])
        node.right = self.buildTree(inorder[rootindex + 1:len(inorder)], postorder[rootindex:- 1])
        return node


s = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = s.buildTree(inorder, postorder)

print(1)
