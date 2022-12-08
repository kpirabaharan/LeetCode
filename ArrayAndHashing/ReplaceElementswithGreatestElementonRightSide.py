# 1299. Replace Elements with Greatest Element on Right Side
from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    maxVal = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        temp = maxVal
        if arr[i] > maxVal:
            temp = arr[i]
        arr[i] = maxVal
        maxVal = temp

    return arr


arr = [17, 18, 5, 4, 6, 1]

print(replaceElements(arr))
