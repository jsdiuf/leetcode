"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-7-31 14:20
sort()
p1=nums[0]
p2=nums[1]
then process...
"""
import time
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res

    #
    def threeSum2(self,nums):
        if len(nums) < 3:
            return []
        if len(nums) == 3 and nums[0] + nums[1] + nums[2] == 0:
            return [nums]
        nums.sort()
        list = []
        map = {}
        le = len(nums)
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        i = 0
        # [-1 0,0,1]
        while i < le and nums[i] <= 0:
            j = i + 1
            left = nums[i]
            while j < le:
                right = nums[j]
                need = 0 - left - right
                if need < right:
                    break
                if need not in map:
                    if left == right:
                        j += (map[right] - 1)
                    else:
                        j += map[right]
                    continue
                if left == right and (need > right or (need == right and map[need] > 2)):
                    list.append([left, left, need])
                    j += (map[right] - 1)
                elif left != right and ((need == right and map[need] > 1) or need > right):
                    list.append([left, right, need])
                    j += map[right]
                else:
                    j += map[right]

            i += map[left]
        return list


# [-18,-4,-4,-3,-3,-2,-1,0,0,1,2,2,3,5,6,6,7,8,8,9,9]
s = Solution()
print(time.time())
print(s.threeSum2([-4,-1,-1,0,1,2]))
print(time.time())