# 118. Pascal's Triangle
numRows = 10
arr = [1] * numRows

for i in range(numRows):
    arr[i] = [1] * (i + 1)
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

print(arr)


