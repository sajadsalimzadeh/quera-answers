import math

a = int(input())
b = int(input())


def is_aval(n):
    if n == 1:
        return False
    s = math.sqrt(n)
    i = 2
    while i <= s:
        if n % i == 0:
            return False;
        i += 1
    return True


arr = []
i = a + 1
while i < b:
    if is_aval(i):
        arr.append(i)
    i += 1

print(','.join(map(str, arr)))
