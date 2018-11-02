"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-2 17:58
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        ml = 0
        for node in root.children:
            t = self.maxDepth(node)
            if t > ml:
                ml = t
        return ml + 1

        #if not root:
        #    return 0
        #if not root.children:
        #    return 1
        #else:
        #    return max([self.maxDepth(c) for c in root.children]) + 1
