import math

n = int(input())

s = math.ceil(n/2)
i = 1
_sum = 0
while i <= s:
    if n % i == 0:
        _sum += i
    i += 1

if _sum == n:
    print('YES')
else:
    print('NO')
