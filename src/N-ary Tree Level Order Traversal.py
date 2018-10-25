"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-23 9:26
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

# Definition for a Node.
from queue import Queue


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = Queue()

        def helper():
            while not q.empty():
                len = q.qsize()
                t = []
                for i in range(len):
                    node = q.get()
                    t.append(node.val)
                    for e in node.children:
                        q.put(e)
                res.append(t)

        q.put(root)
        helper()
        return res

    def levelOrder2(self, root):
        if not root:
            return []
        q = [root]
        out = []
        while len(q):
            tmp = []
            out.append([])
            for x in q:
                out[-1].append(x.val)
                tmp.extend([c for c in x.children])
            q = tmp
        return out
