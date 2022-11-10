import collections


def firstUniqueChar(s):
    count = collections.Counter(s)
    print(count)

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


str = "lolloveleetcode"
index = firstUniqueChar(str)
print(index)