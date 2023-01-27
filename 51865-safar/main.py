x = int(input())
n = int(input())

res = x
if n == 0:
    res = 20
elif n == 7:
    res = x
elif n != 7:
    res -= n

if res < 0:
    res = 0

print(res)