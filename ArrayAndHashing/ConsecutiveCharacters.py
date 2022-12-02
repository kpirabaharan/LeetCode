def maxPower(s: str) -> int:
    maxCount, count = 1, 1
    for ind in range(1, len(s)):
        if s[ind] == s[ind - 1]:
            count += 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count

    return maxCount


s = "abbcccddddeeeeedcba"
print(maxPower(s=s))
