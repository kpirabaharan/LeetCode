# 300 - Longest Increasing Subsequence
from typing import List

# FAILED CASE: [1,3,6,7,9,4,10,5,6]


def lengthOfLIS(nums: List[int]) -> int:
    lp, rp, lenArr = 0, 1, len(nums)
    res, curr = 0, 1
    currMax = nums[0]

    while rp < lenArr:

        if nums[rp] < nums[lp]:
            lp = rp
            curr = 1
            currMax = nums[rp]
            print("Exec at", rp)
        if nums[rp] > nums[rp - 1] and nums[rp] > currMax:
            curr += 1
            print(nums[rp], curr)
            res = max(res, curr)
        currMax = max(currMax, nums[rp])
        rp += 1

    return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums1 = [0, 1, 0, 3, 2, 3]
nums2 = [1, 3, 6, 7, 9, 4, 10, 5, 6]

print(lengthOfLIS(nums1))
