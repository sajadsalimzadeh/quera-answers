import math

a = int(input())
b = int(input())

m = min(a, b)
i = 2
s = m
r = 1
while s >= 2:
    if a % s == 0 and b % s == 0:
        r = round(s)
        break
    s = m / i
    i += 1

print(r)