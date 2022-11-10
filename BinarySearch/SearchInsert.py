
def searchInsert(nums, target):
    val = 0
    print(len(nums))
    while nums[val] < target:
        val += 1
        print(val)
        if val == len(nums):
            break
    return val

listofnums = [1,3,5,6]
targ = 7
value = searchInsert(listofnums, targ)
print(value)