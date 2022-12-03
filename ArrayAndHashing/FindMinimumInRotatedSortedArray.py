# 153 Find Minimum in Rotated Sorted Array
from typing import List


def findMin(nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            if nums[l] < res:
                res = nums[l]
            break

        m = (l + r) // 2
        if nums[m] < res:
            res = nums[m]

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res


nums = [11, 13, 15, 17]
nums = [3, 4, 5, 1, 2]
print(findMin(nums=nums))
