# 125. Valid Palindrome
def isPalindrome(self, s: str) -> bool:
    char = []
    ind = 0
    for ch in s:
        if ch.isalnum():
            char.append(ch.lower())
    print(char)

    while ind < len(char) // 2:
        if char[ind] == char[(-ind - 1)]:
            ind += 1
        else:
            return False
    return True