def TwoSum1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(TwoSum1(nums, target))

