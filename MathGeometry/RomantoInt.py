# 13. Roman to Integer

# I thought IIV was a thing and implemented it this way. OOPS
def romanToInt(s: str) -> int:
    num = 0
    arr = []
    romans = {'I': 1, '-I': -1, 'V': 5, 'X': 10, '-X': -10, 'L': 50, 'C': 100, '-C': -100, 'D': 500, 'M': 1000}
    numRomans = {'I': 0, '-I': 0, 'V': 0, 'X': 0, '-X': 0, 'L': 0, 'C': 0, '-C': 0, 'D': 0, 'M': 0}
    for rom in s:
        arr.append(rom)
    arr = arr[::-1]
    for rom in arr:
        if rom == 'I' and (numRomans['V'] > 0 or numRomans['X'] > 0):
            numRomans['-I'] += 1
        elif rom == 'X' and (numRomans['L'] > 0 or numRomans['C'] > 0):
            numRomans['-X'] += 1
        elif rom == 'C' and (numRomans['D'] > 0 or numRomans['M'] > 0):
            numRomans['-C'] += 1
        else:
            numRomans[rom] += 1
    for ch in numRomans:
        num += numRomans[ch] * romans[ch]
    return num


def romanToInt2(s: str) -> int:
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and rom[s[i]] < rom[s[i + 1]]:
            result -= rom[s[i]]
        else:
            result += rom[s[i]]
    return result

s = "MCMXCIV"
print(romanToInt2(s))
