"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 13:40
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return head

    p=reverse(head.next)
    head.next.next=head
    head.next=None
    return p

def reserve2(head):
    if head is None or head.next is None:
        return head
    pl=None
    p=head
    pr=head.next
    while pr:
        p.next=pl
        pl=p
        p=pr
        pr=pr.next
    p.next=pl
    return p

n1=ListNode(1)
n1.next=ListNode(2)
n1.next.next=ListNode(3)
n1.next.next.next=ListNode(4)

h=reserve2(n1)
print(1)