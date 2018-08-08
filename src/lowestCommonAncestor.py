"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-7 15:49
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        prelist=[]
        inlist=[]
        postlist=[]
        def traver(node, prelist,inlist):

            prelist.append(node)

            if node.left:
                traver(node.left, prelist,inlist)
            inlist.append(node)

            if node.right:
                traver(node.right, prelist,inlist)
            postlist.append(node)

        traver(root,prelist,inlist)

        prelist=prelist[0:min(prelist.index(p),prelist.index(q))+1]
        inlist=inlist[min(inlist.index(p),inlist.index(q)):max(inlist.index(p),inlist.index(q))+1]
        postlist=postlist[max(postlist.index(p),postlist.index(q)):]
        inlist=set(prelist).intersection(set(inlist))
        postlist=set(postlist).intersection(set(inlist))

        return list(postlist)[0]

    def lowestCommonAncestor2(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor2(root.left, p, q)
        r = self.lowestCommonAncestor2(root.right, p, q)
        if l and r:
            return root
        return r if l is None else l

n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n5.left = n8
n5.right = n9

s = Solution()
print(s.lowestCommonAncestor2(n1, n4, n7).val)
