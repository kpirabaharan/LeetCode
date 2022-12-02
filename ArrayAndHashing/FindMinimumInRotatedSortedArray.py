from typing import List


def findMin(nums: List[int]) -> int:
    for ind in range(1, len(nums)):
        if nums[ind] < nums[ind - 1]:
            return nums[ind]
    return nums[0]


nums = [3, 4, 5, 1, 2]
print(findMin(nums=nums))
