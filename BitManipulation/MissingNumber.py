#  268. Missing Number

def MissingNumber(nums: list):
    answer = 0
    for n in nums:
        answer ^= n
    if len(nums) % 4 == 0:
        answer ^= len(nums)
    elif len(nums) % 4 == 1:
        answer ^= 1
    elif len(nums) % 4 == 2:
        answer ^= (len(nums) + 1)
    elif len(nums) % 4 == 3:
        answer = answer
    return answer


def MissingNumber2(nums: list):
    length = len(nums)
    total = length*(length+1)/2
    totalarr = sum(nums)
    return int(total - totalarr)


nums = [0, 1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 10, 13]
nums1 = [3, 0, 1]

# n
# 1
# n+1
# 0
# repeat
print(MissingNumber2(nums))
