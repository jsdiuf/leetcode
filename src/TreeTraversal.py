"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 21:35
"""

"""
        F
     /    \
    B      G
   / \      \
  A   D      I
     / \    /
    C   E  H
    
前序遍历  根左右 ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
中序遍历  左根右 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
后续遍历  左右根 ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
（所谓的前中后 指的是 “根”）
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 前序遍历
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list = []

        def preTraver(root, list):
            list.append(root.val)
            if root.left:
                preTraver(root.left, list)
            if root.right:
                preTraver(root.right, list)

        preTraver(root, list)
        return list

    # 中序遍历
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list = []

        def inTraver(root, list):
            if root.left:
                inTraver(root.left, list)
            list.append(root.val)
            if root.right:
                inTraver(root.right, list)

        inTraver(root, list)
        return list

    # 后序遍历
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list = []

        def postTraver(root, list):
            if root.left:
                postTraver(root.left, list)
            if root.right:
                postTraver(root.right, list)
            list.append(root.val)

        postTraver(root, list)
        return list


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

f.left = b
f.right = g

b.left = a
b.right = d

d.left = c
d.right = e

g.right = i
i.left = h

s = Solution()
print(s.preorderTraversal(f))
print(s.inorderTraversal(f))
print(s.postorderTraversal(f))
