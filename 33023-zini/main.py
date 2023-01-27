args = list(map(int, input().split()))
n = args[0]
m = args[1]

matrix = []
i = 0
while i < n:
    row = list(map(int, input().split()))
    matrix.append(row)
    i += 1

c = 0
i = 1
while i < n - 1:
    j = 1
    while j < m - 1:
        x = matrix[i][j]
        top = matrix[i - 1][j]
        bottom = matrix[i + 1][j]
        left = matrix[i][j - 1]
        right = matrix[i][j + 1]
        if (left > x < right and top < x > bottom) or (left < x > right and top > x < bottom):
            c += 1
        j += 1
    i += 1

print(c)