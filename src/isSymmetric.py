"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-6 11:05
"""

# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # empty or
        if not root or (not root.left and not root.right):
            return True

        q = queue.Queue()
        q.put(root)

        while not q.empty():

            n = q.qsize()
            arr = []
            while n > 0:
                node = q.get()

                arr.append(node)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                n -= 1

            i, j = 0, len(arr) - 1
            while i <= j:

                node1, node2 = arr[i], arr[j]
                t = []
                t.append(None if not node1.left else node1.left.val)
                t.append(None if not node1.right else node1.right.val)
                t.append(None if not node2.left else node2.left.val)
                t.append(None if not node2.right else node2.right.val)

                if t[0] != t[3] or t[1] != t[2]:
                    return False
                i += 1
                j -= 1

        return True

    # 递归
    def isSymmetric2(self, root):
        if not root:
            return True

        def isSymmetric(node1, node2):

            # if not node1 and not node2:
            # return

            if (node1 and not node2) or (not node1 and node2):
                return False
            t = []
            t.append(None if not node1.left else node1.left.val)
            t.append(None if not node1.right else node1.right.val)
            t.append(None if not node2.left else node2.left.val)
            t.append(None if not node2.right else node2.right.val)

            if t[0] != t[3] or t[1] != t[2]:
                return False

            ret1, ret2 = True, True

            if node1.left:
                ret1 = isSymmetric(node1.left, node2.right)
            if node1.right:
                ret2 = isSymmetric(node1.right, node2.left)

            return ret1 and ret2

        return isSymmetric(root, root)

    # 递归 优化版
    def isSymmetric3(self,root):

        def isSymmetric(node1, node2):

            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return isSymmetric(node1.left, node2.right) and isSymmetric(node1.right, node2.left)

        return isSymmetric(root, root)


a = TreeNode("A")

b = TreeNode("B")
c = TreeNode("B")

d = TreeNode("C")
e = TreeNode("C")

f = TreeNode("D")
g = TreeNode("D")

a.left = b
a.right = c

b.right = d
c.left = e

# d.right = f
# e.right = g

s = Solution()
print(s.isSymmetric2(f))
