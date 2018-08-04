"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-3 20:13
"""


# Definition for singly-linked list.
import heapq
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val<other.val


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while None in lists:
            lists.remove(None)
        if len(lists)==0:
            return None
        head = cur = ListNode(0)
        lists = sorted(lists, key=lambda x: x.val)
        while len(lists) > 0:
            cur.next = lists[0]
            nextNode=lists[0].next
            lists = lists[1:]
            cur = cur.next
            if nextNode:
                lists.append(nextNode)
                lists=sorted(lists,  key=lambda x: x.val)
        return head.next

    def insertRightposition(self,arr):
        n=len(arr)
        i=1
        val=arr[0][1]
        while i<n and val>arr[i][1]:
            i+=1
        arr.insert(i,arr[0])
        return arr[1:]
    #PriorityQueue 优先队列

    def mergeKLists2(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, lists.index(node)))
        while q.qsize() > 0:
            index=q.get()[1]
            curr.next = lists[index]
            lists[index]=lists[index].next
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, index))
        return dummy.next


    def mergeKLists3(self, lists):
        dummy = ListNode(None)
        curr = dummy
        heap=[]
        for node in lists:
            if node:
                heapq.heappush(heap, node)
        while len(heap) > 0:
            curr.next = heapq.heappop(heap)
            curr = curr.next
            if curr.next:
                heapq.heappush(heap,curr.next)
        return dummy.next


n1 = ListNode(1)
n1.next = ListNode(4)
n1.next.next = ListNode(5)

n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(4)

n3 = ListNode(2)
n3.next = ListNode(6)

s = Solution()
head = s.mergeKLists([n1,n2,n3])
print(1)
