def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [x for x in set1 if x in set2]


numbers1 = [4, 9, 5]
numbers2 = [9, 4, 9, 8, 4]

arr = intersection(numbers1, numbers2)
print(arr)
