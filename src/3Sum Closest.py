"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-1 9:06
@url https://leetcode.com/problems/3sum-closest/description/
"""

import time


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        nums.sort()

        le = len(nums)

        if nums[le - 1] + nums[le - 2] + nums[le - 3] <= target:
            return nums[le - 1] + nums[le - 2] + nums[le - 3]

        if nums[0] + nums[1] + nums[2] >= target:
            return nums[0] + nums[1] + nums[2]

        map = {}
        i = 0
        while i < le:
            if nums[i] not in map:
                # key在数组中存在的个数,
                map[nums[i]] = [1, 0, 0]
            else:
                map[nums[i]][0] += 1
            if i == le - 1:
                break
            for e in range(nums[i] + 1, nums[i + 1]):
                # key 在数组中的个数,左边最近的数组元素的距离,右边最近的数组元素的距离
                map[e] = [0, e - nums[i], nums[i + 1] - e]
            i += 1
        p1 = 0
        ret = nums[0] + nums[1] + nums[2]
        while p1 < le - 2:
            # nums[p1]!=nums[p2]
            # 下一个不同于nums[p1] 的元素
            p2 = p1 + map[nums[p1]][0]
            while p2 < le - 1:
                need = target - nums[p1] - nums[p2]
                # 命中数组元素
                if need in map.keys():
                    # 命中数组中元素(这个元素存在大于1个) 直接返回target
                    if map[need][0] > 1:
                        return target
                    # 命中数组中元素(这个元素就只有一个) 并且need不等于nums[p1] 和 nums[p2] 直接返回target
                    if map[need][0] == 1 and need != nums[p1] and need != nums[p2]:
                        return target
                    # 命中的是nums[p1] (nums[p1] 只有一个)
                    left = need - map[need][1]
                    right = need + map[need][2]

                    # 左边找一个最近的未用数组元素 超出范围返回nums[0]-1
                    if left == nums[p2] and map[nums[p2]][0] == 1:
                        left = nums[p2 - 1]
                    if left == nums[p1] and nums[p1] != nums[0] and map[nums[p1]][0] == 1:
                        left = nums[p1 - 1]
                    if left == nums[p1] and nums[p1] == nums[0] and map[nums[p1]][0] == 1:
                        left = nums[0] - 1

                    # 右边找一个未用的数组元素 超出范围使用nums[len-1]+1
                    if right == nums[p1] and map[nums[p1]][0] == 1:
                        right = nums[p1 + 1]
                    if right == nums[p2] and nums[p2] != nums[le - 1] and map[nums[p2]][0] == 1:
                        right = nums[p2 + 1]
                    if right == nums[p2] and nums[p2] == nums[le - 1] and map[nums[p2]][0] == 1:
                        right = nums[le - 1] + 1

                    # 找出(线性)离need最近的可用数组元素 并比较替换操作
                    if left < nums[0] and abs(target - ret) > right - need:
                        ret = nums[p1] + nums[p2] + right
                    if right > nums[le - 1] and abs(target - ret) > need - left:
                        ret = nums[p1] + nums[p2] + left

                    if right - need >= need - left and abs(target - ret) > need - left:
                        ret = nums[p1] + nums[p2] + left
                    if right - need < need - left and abs(target - ret) > right - need:
                        ret = nums[p1] + nums[p2] + right

                else:
                    # need超出数组左边边界 找出一个下表最小的可用元素 比较替换
                    if need < nums[0]:
                        right = nums[0]
                        if right == nums[p1] and map[nums[p1]][0] == 1:
                            right = nums[p1 + 1]
                        if right == nums[p2] and map[nums[p2]][0] == 1:
                            right = nums[p2 + 1]
                        if abs(target - ret) > right - need:
                            ret = nums[p1] + nums[p2] + right
                    # need超出数组右边边界 找出一个下表最大的可用元素 比较替换
                    if need > nums[le - 1]:
                        left = nums[le - 1]
                        if left == nums[p2] and map[nums[p2]][0] == 1:
                            left = nums[p2 - 1]
                        if left == nums[p1] and map[nums[p1]][0] == 1:
                            left = nums[p1 - 1]
                        if abs(target - ret) > need - left:
                            ret = nums[p1] + nums[p2] + left
                # 跳到下一个比当前大的元素
                p2 += map[nums[p2]][0]
            # 跳到下一个比当前大的元素
            p1 += map[nums[p1]][0]
        return ret

    def fun2(self, nums, target):
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum==target:
                    return target
                if sum > target:
                    end -= 1
                else:
                    start += 1
                if abs(sum - target) < abs(result - target):
                   result = sum
        return result


s = Solution()
print(time.time())
print(s.fun2([1,2,5,10,11], 12))
print(time.time())
