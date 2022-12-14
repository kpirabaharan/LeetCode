# 88 - Merge Sorted Array
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    mp, np = 0, 0
    newL = []
    for i in range(m):
        newL.append(nums1[i])


    while mp < m and np < n:
        if newL[mp] <= nums2[np]:
            nums1[mp + np] = newL[mp]
            mp += 1
        elif nums2[np] < newL[mp]:
            nums1[mp + np] = nums2[np]
            np += 1

    if mp == m:
        while np < n:
            nums1[mp + np] = nums2[np]
            np += 1
    if np == n:
        while mp < m:
            nums1[mp + np] = newL[mp]
            mp += 1


nums1 = [-1, -1, 0, 0, 0, 0]
m = 4
nums2 = [-1, 0]
n = 2

merge(nums1, m, nums2, n)


print(nums1)
