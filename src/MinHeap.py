"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-4 13:55
"""


# 小根堆
class MinHeap():
    def __init__(self):
        self.arr = []
        self.count = 0

    # 上浮(小的上浮 上浮到使他的父节点大于他) i表示i个元素 其在数组中的下表为i-1
    def shift_up(self, i):
        while i // 2 >= 1:
            if self.arr[i - 1] < self.arr[i // 2 - 1]:
                self.arr[i - 1], self.arr[i // 2 - 1] = self.arr[i // 2 - 1], self.arr[i - 1]
                i = i // 2
            else:
                break

    # 下沉（大的下沉 下沉到他的比较小的子节点那 直到不能再下沉） arr中第i个数  arr[i] 是第i+1个数 如果想下沉arr[i] 请传参i+1
    def shift_down(self, i):
        while i * 2 <= self.count:
            T = i * 2
            # 找出较小的子节点
            if T + 1 <= self.count and self.arr[T - 1] > self.arr[T]:
                T += 1
            # 父节点与较小的子节点交换 并指向较小的子节点
            if self.arr[i - 1] > self.arr[T - 1]:
                self.arr[i - 1], self.arr[T - 1] = self.arr[T - 1], self.arr[i - 1]
                i = T
            else:
                break

    # 插入  插入数组最后 使其上浮
    def push(self, n):
        self.count += 1
        self.arr.append(n)
        self.shift_up(self.count)

    # 弹出 数组头尾互换  头下沉
    def pop(self):
        if self.count > 1:
            ret = self.arr[0]
            self.arr[0] = self.arr[self.count - 1]
            self.count -= 1
            self.shift_down(1)
            return ret


s = MinHeap([])
s.push(8)
print(s.arr)
s.push(5)
print(s.arr)
s.push(2)
print(s.arr)
s.push(9)
print(s.arr)
s.push(3)
print(s.arr)
s.push(7)
print(s.arr)
s.push(1)
print(s.arr)
s.push(4)
print(s.arr)
s.push(6)
print(s.arr)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
