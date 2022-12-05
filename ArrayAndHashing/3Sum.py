# 15 3Sum
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    boo = False

    nums = sorted(nums)

    for target in range(len(nums) - 2):
        if target > 0 and nums[target] == nums[target - 1]:
            continue

        l, r = target + 1, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]
            totalTarget = -1 * nums[target]

            if total < totalTarget:
                l += 1
                boo = False
            if total > totalTarget:
                r -= 1
                boo = True
            if total == totalTarget:
                if [nums[target], nums[l], nums[r]] not in result:
                    result.append([nums[target], nums[l], nums[r]])
                if boo == False:
                    l += 1
                else:
                    r -= 1

    return result


nums = [-4, -1, -1, 0, 1, 2]
nums1 = [0, 0, 0, 0]
# nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums=nums1))
