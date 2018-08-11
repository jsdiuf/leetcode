class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
list=[]
def perorder(nd):
    if not nd:
        list.append(None)
        return
    list.append(nd.val)
    perorder(nd.left)
    perorder(nd.right)




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


print(perorder(n1))
print(list)