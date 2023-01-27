n = 3

a = []
b = []

i = 0
while i < n:
    a.append(int(input()))
    b.append(int(input()))
    i += 1

_sum = 0
i = 0
while i < n:
    _sum += min(a[i], b[i])
    i += 1

print(_sum)