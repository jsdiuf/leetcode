import queue

q=queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.get()
while not q.empty():
    print(q.get())
print(1)
print(q is None)