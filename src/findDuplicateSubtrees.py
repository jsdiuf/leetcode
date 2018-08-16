"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 9:15
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def preOrderHelper(node, orderarr):
            if not node:
                orderarr.append("#")
                return
            orderarr.append(str(node.val))
            preOrderHelper(node.left, orderarr)
            preOrderHelper(node.right, orderarr)

        dic = {}
        ret = []

        def preOrderjudge(root):
            if root:
                orderarr = []
                preOrderHelper(root, orderarr)
                orderStr = "".join(orderarr)
                if orderStr not in dic:
                    dic[orderStr] = [root]
                else:
                    dic[orderStr].append(root)

                preOrderjudge(root.left)
                preOrderjudge(root.right)

        preOrderjudge(root)
        for e in dic:
            if len(dic[e]) > 1:
                ret.append(dic[e][0])
        return ret

    # post_order_traversal   nice solution
    def findDuplicateSubtrees2(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.visited_subtrees = set()
        self.res = {}

        def post_order_traversal(node):
            order = ''
            if node.left:
                order += post_order_traversal(node.left)
            else:
                order += '*'
            if node.right:
                order += post_order_traversal(node.right)
            else:
                order += '*'
            order += str(node.val)
            if order in self.visited_subtrees:
                self.res[order] = node
            self.visited_subtrees.add(order)
            return order

        if root is None:
            return []
        post_order_traversal(root)
        return list(self.res.values())


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(2)
n6 = TreeNode(4)
n7 = TreeNode(4)

n1.left = n2
n1.right = n3

n2.left = n4
n3.left = n5
n3.right = n6
n5.left = n7

s = Solution()
arr = s.findDuplicateSubtrees(n1)
print(1)
