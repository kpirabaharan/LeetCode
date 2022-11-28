from typing import List

# Can optimize this a little using range and one list
def productExceptSelf(nums: List[int]) -> List[int]:
    forwardsArr = []
    result = []
    total = 1

    for val in nums[:len(nums)-1]:
        total *= val
        forwardsArr.append(total)
    
    total = nums[-1]
    result.append(forwardsArr[-1])
    for ind, val in enumerate(reversed(nums[1:-1])):
        result.append(total*forwardsArr[-ind-2])
        total *= val
    result.append(total)
    
    return list(reversed(result))


nums = [1,2,3,4]
# Forward: 1 2 6 24
# Backward: 24 24 12 4
# Need: 24 12 8 6
print(productExceptSelf(nums))
