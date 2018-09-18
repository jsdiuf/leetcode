"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-18 23:33
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.

        [[3,3],[1,1],[2,1]]  .....[val,min]

        """
        self.arr = []
        self.sortarr = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)
        if not self.sortarr:
            self.sortarr.append(x)
            return
        if x <= self.sortarr[0]:
            self.sortarr.insert(0, x)
            return
        if x >= self.sortarr[0]:
            self.sortarr.append(x)
            return
        i, j = 0, len(self.sortarr) - 1
        while i <= j:
            m = (i + j) // 2
            if self.sortarr[m - 1] <= x and self.sortarr[m] >= x:
                self.sortarr.insert(m, x)
                return
            if self.sortarr[m] < x:
                i = m + 1
            else:
                j = m - 1

    def pop(self):
        """
        :rtype: void
        """
        if not self.arr:
            return
        x = self.arr[-1]
        del self.arr[-1]
        i, j = 0, len(self.sortarr) - 1
        while i <= j:
            m = (i + j) // 2
            if self.sortarr[m] == x:
                del self.sortarr[m]
                return
            if self.sortarr[m] < x:
                i = m + 1
            else:
                j = m - 1

    def top(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.sortarr:
            return self.sortarr[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
print(obj.arr)
print("sortarr", obj.sortarr)
obj.push(2)
print(obj.arr)
print("sortarr", obj.sortarr)
obj.push(3)
print(obj.arr)
print("sortarr", obj.sortarr)
obj.push(-2)
print(obj.arr)
print("sortarr", obj.sortarr)
obj.pop()
print(obj.arr)
print("sortarr", obj.sortarr)
print(obj.top())

print(obj.getMin())
