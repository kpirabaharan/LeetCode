# 191. Number of 1 Bits

def hammingWeight(n: int):
    num = 0
    while n:
        num += n % 2
        n >>= 1
    return num


def hammingWeight2(n: int):
    num = 0
    while n:
        if n & 1 == 1:
            num += 1
        n >>= 1
    return num


n = 0b111111111111
print(hammingWeight2(n))
