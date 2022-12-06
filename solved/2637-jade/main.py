import math

n = int(input())

res = 0
if n == 1:
    res = 2
elif n % 2 == 0:
    f = math.floor(n / 2) + 1
    res = f * f
else:
    f = math.ceil(n / 2)
    res = f * (f + 1)

print(res)
