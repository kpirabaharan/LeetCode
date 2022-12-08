#  268. Missing Number
import time


def MissingNumber(nums: list):
    answer = 0
    for n in nums:
        answer ^= n
    if len(nums) % 4 == 0:
        answer ^= len(nums)
    elif len(nums) % 4 == 1:
        answer ^= 1
    elif len(nums) % 4 == 2:
        answer ^= len(nums) + 1
    elif len(nums) % 4 == 3:
        answer = answer
    return answer


def MissingNumber2(nums: list):
    length = len(nums)
    total = length * (length + 1) / 2
    totalarr = sum(nums)
    return int(total - totalarr)


def MissingNumber3(nums: list):
    answer = 0
    length = len(nums)
    rem = length % 4
    for n in nums:
        answer ^= n
    if rem == 0:
        answer ^= length
    elif rem == 1:
        answer ^= 1
    elif rem == 2:
        answer ^= length + 1
    return answer


nums = [0, 11, 2, 3, 4, 5, 6, 1, 9, 8, 12, 10, 13]
nums1 = [3, 0, 1]

# n
# 1
# n+1
# 0
# repeat
start = time.time()
print(MissingNumber(nums))
print("Time: ", time.time() - start)
start = time.time()
print(MissingNumber2(nums))
print("Time: ", time.time() - start)
start = time.time()
print(MissingNumber3(nums))
print("Time: ", time.time() - start)
