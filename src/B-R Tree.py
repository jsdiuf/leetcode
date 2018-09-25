"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 15:01
https://www.2cto.com/kf/201611/561018.html

1.每个节点或是红色的，或是黑色的。
2.根节点是黑色的。
3.每个叶节点（NIL 空节点）是黑色的。
4.如果一个节点是红色的，则它的俩个字节点都是黑色的。
5.对每个节点，从该节点到其他所有后代叶节点的简单路径上，均包含相同数目的黑色节点。
"""
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class BRNode:
    def __init__(self, val, color):
        self.color = color
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BRTree:
    def __init__(self):
        self.root = None
        self.nil = BRNode(0, Color.BLACK)

    """
       node                 r                    
      /    \               /  \ 
     a      r       -->   node c
            /   \        /\
            b     c     a  b   
    """

    def print(self, root):
        if root:
            print(root.val, root.color)
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

    def insert(self, val):

        if not self.root:
            self.root = BRNode(val, Color.BLACK)
            self.root.left = self.nil
            self.root.right = self.nil
            return
        cur = self.root
        while cur:
            if cur.val > val:
                if cur.left != self.nil:
                    cur = cur.left
                else:
                    cur.left = n = BRNode(val, Color.RED)
                    n.parent = cur
                    n.left = self.nil
                    n.right = self.nil
                    cur = cur.left
                    break
            else:
                if cur.right != self.nil:
                    cur = cur.right
                else:
                    cur.right = n = BRNode(val, Color.RED)
                    n.parent = cur
                    n.left = self.nil
                    n.right = self.nil
                    cur = cur.right
                    break
        self.RBInsertFixup(cur)
        """
        case 0 父节点为黑  直接返回
        
        Case 1	当前节点的父节点是红色，且当前节点的祖父节点的另一个子节点（叔叔节点）也是红色。	
               (01) 将“父节点”设为黑色。
               (02) 将“叔叔节点”设为黑色。
               (03) 将“祖父节点”设为“红色”。
               (04) 将“祖父节点”设为“当前节点”(红色节点)；即，之后继续对“当前节点”进行操作。
               
        Case 2	当前节点的父节点是红色，叔叔节点是黑色，且当前节点是其父节点的右孩子	
               (01) 将“父节点”作为“新的当前节点”。
               (02) 以“新的当前节点”为支点进行左旋。
               
        Case 3	当前节点的父节点是红色，叔叔节点是黑色，且当前节点是其父节点的左孩子	
               (01) 将“父节点”设为“黑色”。
               (02) 将“祖父节点”设为“红色”。
               (03) 以“祖父节点”为支点进行右旋。
               
        具体有出入  具体看代码
        """

    def RBInsertFixup(self, cur):

        # 父节点为黑直接返回
        if not cur.parent or cur.parent.color == Color.BLACK:
            self.root.color = Color.BLACK
            return
        if cur.parent == cur.parent.parent.left:  # 待插节点父节点为祖父节点的left
            u = cur.parent.parent.right
            if u.color == Color.RED:
                cur.parent.color = Color.BLACK
                u.color = Color.BLACK
                u.parent.color = Color.RED
                self.RBInsertFixup(u.parent)
            else:
                if cur == cur.parent.right:
                    cur = cur.parent
                    self.left_roate(cur)
                cur.parent.color = Color.BLACK
                cur.parent.parent.color = Color.RED
                self.right_roate(cur.parent.parent)
                self.RBInsertFixup(cur)
        else:
            u = cur.parent.parent.left
            if u.color == Color.RED:
                cur.parent.color = Color.BLACK
                u.color = Color.BLACK
                u.parent.color = Color.RED
                self.RBInsertFixup(u.parent)
            else:
                if cur == cur.parent.left:
                    cur = cur.parent
                    self.right_roate(cur)
                cur.parent.color = Color.BLACK
                cur.parent.parent.color = Color.RED
                self.left_roate(cur.parent.parent)
                self.RBInsertFixup(cur)

    def getNodeByVal(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left

    def getMinNode(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def delete(self, val):
        node = self.getNodeByVal(val)
        if not node:
            return
        self.RBDelete(node)

    def RBDelete(self, d):
        p = d.parent
        color = d.color
        if d.left == self.nil and d.right == self.nil:  # 左右子节点都为nil
            if d == self.root:
                self.root = None
                return
            if d == d.parent.left:
                d.parent.left = self.nil
                if color == Color.BLACK:
                    self.deleteFixUp(p.left)
            else:
                d.parent.right = self.nil
                if color == Color.BLACK:
                    self.deleteFixUp(p.right)

        elif d.left == self.nil:  # 左子节点为nil
            if d == self.root:
                d.right.parent = None
                self.root = d.right
                self.root.color = Color.BLACK

            elif d == d.parent.left:
                d.parent.left = d.right
                d.right.parent = d.parent
                if color == Color.BLACK:
                    self.deleteFixUp(p.left)
            else:
                d.parent.right = d.right
                d.right.parent = d.parent
                if color == Color.BLACK:
                    self.deleteFixUp(p.right)
        elif d.right == self.nil:  # 右子节点为nil
            if d == self.root:
                d.left.parent = None
                self.root = d.left
                self.root.color = Color.BLACK
            elif d == d.parent.left:
                d.parent.left = d.left
                d.left.parent = d.parent
                if color == Color.BLACK:
                    self.deleteFixUp(p.left)
            else:
                d.parent.right = d.left
                d.left.parent = d.parent
                if color == Color.BLACK:
                    self.deleteFixUp(p.right)
        else:  # 左右子节点都不为nil
            m = self.getMinNode(d.right)
            d.val = m.val
            self.RBDelete(m)

    """
    Case 1	x是"黑+黑"节点，x的兄弟节点是红色。(此时x的父节点和x的兄弟节点的子节点都是黑节点)。	
       (01) 将x的兄弟节点设为“黑色”。
       (02) 将x的父节点设为“红色”。
       (03) 对x的父节点进行左旋。
       (04) 左旋后，重新设置x的兄弟节点。
    
    Case 2	x是“黑+黑”节点，x的兄弟节点是黑色，x的兄弟节点的两个孩子都是黑色。	
       (01) 将x的兄弟节点设为“红色”。
       (02) 设置“x的父节点”为“新的x节点”。
    
    Case 3	x是“黑+黑”节点，x的兄弟节点是黑色；x的兄弟节点的左孩子是红色，右孩子是黑色的。	
       (01) 将x兄弟节点的左孩子设为“黑色”。
       (02) 将x兄弟节点设为“红色”。
       (03) 对x的兄弟节点进行右旋。
       (04) 右旋后，重新设置x的兄弟节点。
    
    Case 4	x是“黑+黑”节点，x的兄弟节点是黑色；x的兄弟节点的右孩子是红色的，x的兄弟节点的左孩子任意颜色。	
       (01) 将x父节点颜色 赋值给 x的兄弟节点。
       (02) 将x父节点设为“黑色”。
       (03) 将x兄弟节点的右子节设为“黑色”。
       (04) 对x的父节点进行左旋。
       (05) 设置“x”为“根节点”。
    """

    def deleteFixUp(self, node):

        pass


t = BRTree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(7)
t.insert(6)
t.insert(5)
t.print(t.root)
