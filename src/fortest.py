from pip._vendor.progress.counter import Stack

s=Stack()
s.append(1)
s.append(2)
print(s.pop())
print(s.pop())
print(s.pop())
print(len(s))