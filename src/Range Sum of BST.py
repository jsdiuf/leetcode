"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-11 13:06
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def helper(node, res):
            if node:
                if node.val >= L:
                    helper(node.left, res)
                if L <= node.val <= R:
                    res[0] += node.val
                if node.val <= R:
                    helper(node.right, res)
        res = [0]
        helper(root, res)
        return res[0]


n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(15)
n4 = TreeNode(3)
n5 = TreeNode(7)
n6 = TreeNode(18)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

s = Solution()
print(s.rangeSumBST(n1, 7, 15))
