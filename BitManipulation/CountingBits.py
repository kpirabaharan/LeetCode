# 338. Counting Bits
from typing import List


def countBits(n: int) -> List[int]:
    res = []
    for i in range(n + 1):
        num = 0
        while i != 0:
            if i & 1:
                num += 1
            i >>= 1
        res.append(num)

    return res


n = 5
print(countBits(n=n))
