#  242. Valid Anagram
from collections import Counter

def isAnagram1(s: str, t: str):
    sArr = []
    tArr = []

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        sArr.append(s[i])
        tArr.append(t[i])

    sArr.sort()
    tArr.sort()

    if sArr == tArr:
        return True
    else:
        return False


def isAnagram2(s: str, t: str):
    sdict = {}
    tdict = {}

    if len(s) != len(t):
        return False

    for ch in s:
        if ch in sdict:
            sdict[ch] += 1
        else:
            sdict[ch] = 1

    for ch in t:
        if ch in tdict:
            tdict[ch] += 1
        else:
            tdict[ch] = 1

    if sdict == tdict:
        return True
    else:
        return False


def isAnagram3(s: str, t: str):
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
print(isAnagram3(s, t))