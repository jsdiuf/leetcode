import heapq
heap=[-1 for i in range(10) ]
heapq.heapify(heap)
heapq.heappush(heap,-2)
print(heap)