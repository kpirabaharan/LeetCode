from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    maxCount, count = 0, 0
    for i in nums:
        if i == 0:
            count = 0
        if i == 1:
            count += 1
        if count > maxCount:
            maxCount = count

    return maxCount


nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums=nums))
