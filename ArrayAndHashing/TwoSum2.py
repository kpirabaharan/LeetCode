# 167 Two Sum II
# Only works if sorted
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return [l + 1, r + 1]
        elif curr > target:
            r -= 1
        else:
            l += 1

    return []


numbers = [2, 7, 11, 15]
target = 13

print(twoSum(numbers, target))
