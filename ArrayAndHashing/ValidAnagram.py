#  242. Valid Anagram
from collections import Counter, defaultdict


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


def isAnagram4(s: str, t: str):
    sdict = defaultdict(lambda: 0)
    tdict = defaultdict(lambda: 0)

    if len(s) != len(t):
        return False

    for ch in s:
        sdict[ch] += 1

    for ch in t:
        tdict[ch] += 1

    if sdict == tdict:
        return True
    else:
        return False

def isAnagram5(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        
        if len(s) != len(t):
            return False

        for i in range(97, 123):
            first[i] = 0
            second[i] = 0

        for ch in s:
            first[ord(ch)] += 1

        for ch in t:
            second[ord(ch)] += 1
        
        if first == second:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"
print(isAnagram5(s, t))
