"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 10:25
输入:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

输出:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        还可以用栈做 stack
        """

        def dfs(cur):
            if cur:

                while cur.next and not cur.child:
                    cur = cur.next
                # 1
                if not cur.next and not cur.child:
                    return cur
                # 2
                if not cur.next and cur.child:
                    cur.next = cur.child
                    cur.next.prev = cur
                    cur.child = None
                    return dfs(cur.next)
                # 3
                if cur.next and cur.child:
                    t = dfs(cur.child)

                    cur.child.prev = cur
                    t.next = cur.next
                    cur.next.prev = t
                    cur.next = cur.child
                    cur.child = None

                    return dfs(t.next)

        dfs(head)
        return head


n1 = Node(1, None, None, None)
n2 = Node(2, None, None, None)
n3 = Node(3, None, None, None)
n4 = Node(4, None, None, None)
n5 = Node(5, None, None, None)
n6 = Node(6, None, None, None)
n7 = Node(7, None, None, None)
n8 = Node(8, None, None, None)
n9 = Node(9, None, None, None)
n10 = Node(10, None, None, None)
n11 = Node(11, None, None, None)
n12 = Node(12, None, None, None)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

n7.next = n8
n8.next = n9
n9.next = n10

n11.next = n12

n1.child = n7
n8.child = n11

s = Solution()
s.flatten(n1)
print(1)
