# 9. Palindrome Number

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif 0 <= x <= 9:
        return True
    dig = []
    for digits in str(x):
        dig.append(int(digits))
    length = len(dig)//2
    for i in range(length):
        if dig[i] != dig[(-i-1)]:
            return False
    return True


x = -121
print(isPalindrome(x))

