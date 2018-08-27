"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-26 17:34
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output:
[
[0,0,0,null,null,0,0,null,null,0,0],
[0,0,0,null,null,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],
[0,0,0,0,0,null,null,0,0]
]
Explanation:

Note:

1 <= N <= 20
"""

# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        very clever!!!!!!
        """
        if not N & 1: return []
        if N == 1: return [TreeNode(0)]
        s = []
        for i in range(1, N - 1, 2):
            l, r = self.allPossibleFBT(i), self.allPossibleFBT(N - i - 1)
            for ll in l:
                for rr in r:
                    p = TreeNode(0)
                    p.left = ll
                    p.right = rr
                    s.append(p)
        return s

    # Memory Limit Exceeded
    def allPossibleFBT2(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        ans = []

        def recur(n, s):
            if n == 0:
                ans.append(s if s[-1] == "0" else s[:-2])
                return
            recur(n - 2, s + "00NN")
            recur(n - 2, s + "NN00")
            if n >= 4:
                recur(n - 4, s + "0000")

        recur(N - 3, "000")
        ret = []

        # [0,0,0,null,null,0,0,null,null,0,0]
        def build(list):
            head = TreeNode(0)
            stack = []
            stack.append(head)
            list = list[1:]
            while list:
                if list[0] == "0":
                    cur = stack.pop()
                    cur.left = TreeNode(0)
                    cur.right = TreeNode(0)
                    stack.append(cur.left)
                    stack.append(cur.right)
                else:
                    stack.pop()
                list = list[2:]
            return head

        for list in ans:
            ret.append(build(list))
        return ret


s = Solution()
li = s.allPossibleFBT(5)
print(1)
