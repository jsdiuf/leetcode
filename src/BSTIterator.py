"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-8 15:06
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """

        '''
        self.stack = []
        while (root!=None):
            self.stack.append(root)
            root = root.left
        '''
        self.list = []
        self.index = 0

        def PRT(node):
            if node.left:
                PRT(node.left)
            self.list.append(node.val)
            if node.right:
                PRT(node.right)
        if root:
            PRT(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        '''
        return len(self.stack)>0
        '''
        return self.index < len(self.list)

    def next(self):
        """
        :rtype: int
        """

        '''
        ret = self.stack.pop(-1)
        r = ret.right
        while (r!=None):
            self.stack.append(r)
            r = r.left
        return ret.val
        '''
        ret = self.list[self.index]
        self.index += 1
        return ret

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
