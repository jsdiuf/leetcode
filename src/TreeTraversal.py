"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 21:35
"""
import queue
from inspect import stack

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

    # 前序遍历 recursion define a new function
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        def preTraver(root, list):
            if root:
                list.append(root.val)
                preTraver(root.left, list)
                preTraver(root.right, list)

        preTraver(root, list)
        return list

    # recursion use itself
    def preorderTraversal2(self, root):
        if not root:
            return []
        list = []
        list.append(root.val)

        if root.left:
            list += (self.preorderTraversal2(root.left))
        if root.right:
            list += (self.preorderTraversal2(root.right))
        return list

    # user stack
    def preorderTraversal3(self, root):
        if not root:
            return []
        list = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return list
        pass

    # only store right node by stack
    def preorderTraversal4(self, root):
        if not root:
            return []
        list = []
        stack = []

        while root:
            list.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
            if not root and stack:
                root = stack.pop()
        return list

    # 中序遍历
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inTraver(root, list):
            if root:
                inTraver(root.left, list)
                list.append(root.val)
                inTraver(root.right, list)

        list = []
        inTraver(root, list)
        return list

    # stack
    def inorderTraversal2(self, root):
        if not root:
            return []
        list, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            list.append(root.val)
            root = root.right
        return list
        pass

    # 后序遍历
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []

        def postTraver(root, list):
            if root:
                postTraver(root.left, list)
                postTraver(root.right, list)
                list.append(root.val)

        postTraver(root, list)
        return list

    # stack
    def postorderTraversal2(self, root):

        list, stack = [], []

        pass

    # 广度优先搜索 Breadth First Search  BFS
    def BFSTraver(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        1初始化一个队列，并把根结点入列队；

        2当队列为非空时，循环执行步骤3到步骤5，否则执行6；

        3出队列取得一个结点，访问该结点；

        4若该结点的左子树为非空，则将该结点的左子树入队列；

        5若该结点的右子树为非空，则将该结点的右子树入队列；

        6结束。
        """
        if root is None:
            return []
        list = []
        q = queue.Queue()
        q.put(root)
        while q.empty() is False:
            node = q.get()
            # 访问
            list.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
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
# print(s.inorderTraversal(f))
# print(s.postorderTraversal(f))

# print(s.BFSTraver(f))
# print(s.preorderTraversal4(f))
# print(s.inorderTraversal(f))
