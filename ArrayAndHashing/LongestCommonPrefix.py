# 14 Longest Common Prefix

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortest = min(strs)

    ret = ""
    for i in range(len(shortest)):
        for string in strs:
            if string[i] != shortest[i]:
                return ret
        ret += shortest[i]

    return ret


def longestCommonPrefixFirst(strs: List[str]) -> str:
    if len(strs[0]) == 0 or len(strs) == 1:
        return strs[0]
    match = strs[0][0]
    preMatch = ""
    length = len(match)

    for i in range(len(strs[0])):
        for ind, s in enumerate(strs):
            if s[0:length] == match:
                continue
            return preMatch
        length += 1
        preMatch = match
        match = strs[0][0:length]
    return strs[0]


strs = ["flower", "flower", "flower", "flower"]
print(longestCommonPrefix(strs=strs))
