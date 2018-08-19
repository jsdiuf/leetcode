"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-19 19:19
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        [1,2,4,5,3,6,7]
        [4,5,2,6,7,3,1]
        """
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        crindex = post.index(pre[1])  # 2
        root.left = self.constructFromPrePost(pre[1:crindex + 2], post[:crindex + 1])
        root.right = self.constructFromPrePost(pre[crindex + 2:], post[crindex + 1:-1])
        return root
