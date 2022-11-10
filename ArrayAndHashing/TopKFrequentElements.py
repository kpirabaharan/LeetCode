# 347. Top K Frequent Elements
from typing import List


def takeSecond(elem):
    return elem[1]


# My initial attempt
# I used a hashmap to count the number of occurrences of each number, and I gave up, but it's the same thing Neet did
def topKFrequent(nums: List[int], k: int) -> List[int]:
    arr = {}
    ret = []
    length = len(nums)
    for ind in nums:
        if ind not in arr:
            arr[ind] = 1
        else:
            arr[ind] += 1
    # for i in range(length, 0 ,-1):
    #     if arr[i]


# Neetcode's method of solution, essentially a bucketsort approach
def topKFrequent2(nums: List[int], k: int) -> List[int]:
    count = {}  # Hashmap to store how many times each element appears in nums
    freq = [[] for i in range(len(nums) + 1)]  # Init a list of length nums + 1 to store what element appears i number of times
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)  # Count.get = value for the key n, default to 0 in case element is not initialized
        # Above is equivalent to below
        # if n in count:
        #     count[n] += 1
        # else:
        #     count[n] = 1

    for n, c in count.items():  # Reverse key and count in array
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


num = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent2(num, k))
