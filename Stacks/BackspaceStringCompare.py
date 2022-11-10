#  844 Backspace String Compare

s = "c##"
t = "ab##"

sArr, sArr2, tArr, tArr2 = [], [], [], []
for i in s:
    sArr.append(i)
for i in t:
    tArr.append(i)

for i, val in enumerate(sArr):
    if val != '#':
        sArr2.append(val)
    if val == '#' and len(sArr2) > 0:
        sArr2.pop()

for i, val in enumerate(tArr):
    if val != '#':
        tArr2.append(val)
    if val == '#' and len(tArr2) > 0:
        tArr2.pop()


