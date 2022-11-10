# 136. Single Number

def singleNumber(nums):
    element = {}

    for n in nums:
        if n in element:
            element[n] = 2
        else:
            element[n] = 1
    print(element)

    for e in element:
        if element[e] == 1:
            return e


def singleNumber2(nums):
    single = 0
    for num in nums:
        # print(single)
        single ^= num  # HOOOOWWWW????
        print(single)
    return single


nums = [2, 1, 3, 1, 2, 4, 4]
# 0000 ^ 0010 = 0010
# 0010 ^ 0001 = 0011
# 0011 ^ 0011 = 0000
# 0000 ^ 0001 = 0001
# 0111 ^ 0100 = 0011
# 0001 ^ 0010 = 0011
# 0011 ^ 0100 = 0111
print(singleNumber2(nums))
