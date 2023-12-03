# 424 Longest Repeating Character Replacement

# A-X = 65-90


def characterReplacement(s: str, k: int) -> int:
    maxLength = 0
    k2 = k
    l, r = 0, 0



s = "ABBB"
k = 2

print(characterReplacement(s, k))
