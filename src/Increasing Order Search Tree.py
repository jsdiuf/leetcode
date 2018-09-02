"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-2 9:40
Given a binary search tree, rearrange the tree so that the minimum value in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(root, tail=None):
            if root is None:
                return tail
            x = TreeNode(root.val)
            x.right = dfs(root.right, tail)
            return dfs(root.left, x)

        return dfs(root)

    def increasingBST2(self, root):

        def inorder(node, p):
            if node:
                inorder(node.left, p)
                if not p[0]:
                    p[0] = node
                    p[1] = node
                else:
                    p[1].right = TreeNode(node.val)
                    p[1] = p[1].right
                inorder(node.right, p)

        p = [None, None]
        inorder(root, p)
        return p[0]


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

n5.left = n3
n5.right = n6

n3.left = n1
n3.right = n4
n1.left = n2
n6.right = n8
n8.left = n7
n8.right = n9

s = Solution()
ret = s.increasingBST2(n5)
print(1)
