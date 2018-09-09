"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 15:01
https://www.2cto.com/kf/201611/561018.html

1.每个节点或是红色的，或是黑色的。
2.根节点是黑色的。
3.每个叶节点（NIL）是黑色的。
4.如果一个节点是红色的，则它的俩个字节点都是黑色的。
5.对每个节点，从该节点到其他所有后代叶节点的简单路径上，均包含相同数目的黑色节点。
"""
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class BRNode:
    def __init__(self, val):
        self.color = None
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BRTree:
    def __init__(self):
        self.root = None

    """
       node                 r                    
      /    \               /  \ 
     a      r       -->   node c
            /   \        /\
            b     c     a  b   
    """

    def print(self, root):
        if root:
            print(root.val)
            self.print(root.left)
            self.print(root.right)
        pass

    def left_roate(self, node):
        if not node or not node.right:
            return
        r = node.right

        node.right = r.left
        if r.left:
            r.left.parent = node

        r.parent = node.parent
        if not node.parent:  # node is root
            r.parent = None
            self.root = r
        else:
            if node == node.parent.left:
                node.parent.left = r
            else:
                node.parent.right = r

        r.left = node
        node.parent = r

        pass

    """
       node              l                          
      /    \            / \   
     l       c   -->   a   node 
    / \                    / \
   a   b                   b  c
                         
                      
    """

    def right_roate(self, node):
        if not node or not node.left:
            return
        l = node.left

        node.left = l.right
        if l.right:
            l.right.parent = node

        l.parent = node.parent
        if not node.parent:
            l.parent = None
            self.root = l
        else:
            if node == node.parent.left:
                node.parent.left = l
            else:
                node.parent.right = l

        l.right = node
        node.parent = l


X = BRNode("X")
Y = BRNode("Y")
a = BRNode("a")
b = BRNode("b")
c = BRNode("c")

X.left = a
a.parent = X
X.right = Y
Y.parent = X
Y.left = b
b.parent = Y
Y.right = c
c.parent = Y

s = BRTree()
s.left_roate(X)
s.print(s.root)
s.right_roate(Y)
s.print(s.root)
