from typing import List


def maxProduct(nums: List[int]) -> int:
    # Brute Force Method, Time Complexity O(n^2)
    maxP = []
    subArrayMax = 1

    for i in range(0, len(nums)):
        subArrayMax = 1
        for j in range(i, len(nums)):
            subArrayMax *= nums[j]
            maxP.append(subArrayMax)

    return max(maxP)


def maxProduct2(nums: List[int]) -> int:
    # Time Complexity: O(n)
    maxP = nums[0]
    currentMax, currentMin = 1, 1

    for i in nums:
        if i == 0:
            currentMax, currentMin = 1, 1

        temp = i * currentMax
        currentMax = max(i, i * currentMin, temp)
        currentMin = min(i, i * currentMin, temp)

        if currentMax > maxP:
            maxP = currentMax

    return maxP


nums = [2, -5, -2, -4, 3]
print(maxProduct2(nums=nums))
