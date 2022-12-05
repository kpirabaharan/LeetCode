# 15 3Sum
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            total = v + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([v, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result


nums = [-4, -1, -1, 0, 1, 2]
nums1 = [0, 0, 0, 0]
# nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums=nums))
