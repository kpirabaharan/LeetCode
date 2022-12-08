# 3 Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    maxCount = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        maxCount = max(r - l + 1, maxCount)
    return maxCount


s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

print(lengthOfLongestSubstring(s))
