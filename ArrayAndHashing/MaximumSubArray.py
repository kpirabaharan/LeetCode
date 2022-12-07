from typing import List


def maxSubArray(nums: List[int]) -> int:
    # Kadane's Algorithm of Dynamic Programming
    # Local_max(i) = max(A(i), A(i) + Local_Max(i-1))
    global_max = nums[0]
    local_max = 0
    for i in nums:
        local_max = max(i, i + local_max)
        if local_max > global_max:
            global_max = local_max

    return global_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums=nums))
