# 153 Find Minimum in Rotated Sorted Array
from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] < nums[r]:
            r = m
        else:
            l = m + 1

    return nums[l]


nums = [11, 13, 15, 17]
nums = [3, 4, 5, 1, 2]
print(findMin(nums=nums))
