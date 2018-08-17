nums=[1,2]
i, j = 0, len(nums) - 1
while i < j:
    if nums[i] != nums[j]:
        print(False)
    i += 1
    j -= 1
print(True)