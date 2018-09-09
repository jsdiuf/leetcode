"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-9 9:44
"""


class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.arr=A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not self.arr:
            return -1
        while 1:
            if self.arr[0]>n:
                self.arr[0]-=n
                return self.arr[1]
            if self.arr[0]==n:
                ans=self.arr[1]
                del self.arr[0]
                del self.arr[0]
                return ans
            if self.arr[0]<n:
                if len(self.arr)==2:
                    del self.arr[0]
                    del self.arr[0]
                    return -1
                else:
                    n-=self.arr[0]
                    del self.arr[0]
                    del self.arr[0]


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3,8,0,9,2,5])
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))