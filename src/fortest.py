class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(head,tail):
    right=tail

    while head!=tail:
        t=head.next
        head.next=right
        right=head
        head=t
    tail=right







n1=ListNode(1)
n1.next=ListNode(2)
n1.next.next=ListNode(3)
n4=ListNode(4)
n1.next.next.next=n4

h=reserve(n1,n4)
print(1)