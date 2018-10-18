"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 9:11
基本排序算法
"""


class Solution:
    # quicksort O(N*logN)
    def quicksort(self, nums, l, r):

        def sub_sort(array, l, r):
            key = array[l]
            while l < r:
                while l < r and array[r] >= key:
                    r -= 1
                while l < r and array[r] < key:
                    array[l] = array[r]
                    l += 1
                    array[r] = array[l]
            array[l] = key
            return l

        if l < r:
            m = sub_sort(nums, l, r)
            self.quicksort(nums, l, m)
            self.quicksort(nums, m + 1, r)

    def quicksort2(self, qlist):

        if not qlist:
            return []
        else:
            qfirst = qlist[0]
            qless = self.quicksort2([l for l in qlist[1:] if l < qfirst])
            qmore = self.quicksort2([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore

    def quicksort3(self, nums):
        return [] if not nums else self.quicksort3([i for i in nums[1:] if i < nums[0]]) + nums[0:1] + self.quicksort3(
            [i for i in nums[1:] if i >= nums[0]])



    #堆排序
    def heapsort(self, list):
        if list != None:
            if list == 1:
                pass
            else:
                for start in range((len(list)) // 2, -1, -1):  # 顶层循环第一步，找到堆的根结点
                    self.rootsort(list, start, len(list) - 1)
                for end in range(len(list) - 1, -1, -1):  # 顶层循环第二步，讲根结点依次提取并排序
                    list[0], list[end] = list[end], list[0]
                    end -= 1
                    self.rootsort(list, 0, end)
        print(list)

    def rootsort(self, list, root, end):  # 递归函数，对list做最大堆调整
        left = 2 * root  # 父结点的左结点
        right = left + 1  # 父结点的右结点
        if left <= end and list[root] < list[left]:  # 控制左结点边界，判断父结点和左结点的大小
            largest = left  #
        else:
            largest = root
        if right <= end and list[largest] < list[right]:  # 控制右结点边界，判断父结点、右结点和左结点的大小
            largest = right  #
        if largest != root:  # 如果计算出来的根结点不是初始设置值，则让根结点与初始值互换位置，直至函数满足这三个条件
            list[root], list[largest] = list[largest], list[root]
            self.rootsort(list, largest, end)  # 递归函数，终止条件是larger不变


s = Solution()
a = [2, 6, 3, 8, 1, 7, 4, 9, 5, 5, 6]
print(s.quicksort3(a))
print(a)

list1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
s.heapsort(list1)
