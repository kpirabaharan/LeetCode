#  217. Contains Duplicate

nums = [1, 2, 3, 1]
distinct = {}

for i in nums:
    if i in distinct:
        print("True")
        # return True
    else:
        distinct[i] = i
print("False")
#  return False
