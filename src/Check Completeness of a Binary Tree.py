"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/20 14:08
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Note:

The tree will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root.left and not root.right:
            return True

        res = [[root]]
        tmp = [root]

        while tmp:
            s = []
            for e in tmp:
                if e.left:
                    s.append(e.left)
                if e.right:
                    s.append(e.right)
            tmp = s
            if tmp:
                res.append(tmp)
        for i in range(len(res) - 1):
            if len(res[i]) != 2 ** i:
                return False

        for i in range(len(res[-1])):
            if i & 1 == 0 and res[-1][i] != res[-2][i // 2].left:
                return False
            if i & 1 == 1 and res[-1][i] != res[-2][i // 2].right:
                return False
        return True


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n3.right = n6

s = Solution()
print(s.isCompleteTree(n1))
