"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-8 23:07
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        cur=root
        parent=None
        while cur:
            if key<cur.val:
                parent=cur
                cur=cur.left
                continue
            if key>cur.val:
                parent=cur
                cur=cur.right
                continue
            if key==cur.val:
                break
        # not found
        if not cur:
            return root
        #leaf node
        if not cur.left and not cur.right:
            if not parent:
                return None
            else:
                if parent.left==cur:
                    parent.left=None
                    return root
                else :
                    parent.right=None
                    return root
        #only left Tree
        if cur.left and not cur.right:
            if not parent:
                    return cur.left
            else:
                if parent.left==cur:
                    parent.left=cur.left
                    return root
                else:
                    parent.right=cur.left
                    return root
        #only right Tree
        if not cur.left and cur.right:
            if not parent:
                return cur.right
            else:
                if parent.left==cur:
                    parent.left=cur.right
                    return root
                else:
                    parent.right=cur.right
                    return root
        # both left and right Tree  shift up right Tree
        # 在右子树种中找到合适的位置放置 左子树 （一直left）
        if cur.left and cur.right:
            posi=cur.right
            while posi.left:
                posi=posi.left
            posi.left=cur.left
            if not parent:
                return cur.right
            else:
                if parent.left==cur:
                    parent.left=cur.right
                else:
                    parent.right=cur.right
                return root


n5=TreeNode(5)
n3=TreeNode(3)
n6=TreeNode(6)
n2=TreeNode(2)
n4=TreeNode(4)
n7=TreeNode(7)

n5.left=n3
n5.right=n6
n3.left=n2
n3.right=n4
n6.right=n7

s=Solution()
h=s.deleteNode(n5,5)
print(1)



