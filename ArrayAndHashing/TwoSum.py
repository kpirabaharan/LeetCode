# 1. Two Sum
nums = [11, 7, 15, 2]
target = 9
Index1, Index2 = 0, 0


def twoSumBrute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return i, j
    return -1, -1


def twoSum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return [seen[remaining], index]
        seen[value] = index


Index1, Index2 = twoSum(nums, target)
print("Index 1:", Index1, "Index 2: ", Index2)
