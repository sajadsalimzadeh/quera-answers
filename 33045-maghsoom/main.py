import math

n = int(input())

def is_aval(p):
    if p == 1:
        return False
    s = math.ceil(math.sqrt(p))
    i = 2
    while i <= s:
        if p % i == 0:
            return False
        i += 1
    return True

avals = []
i = 2
while i <= n:
    if is_aval(i):
        avals.append(i)
    i += 1

print(avals)
i = 1
_sum = 0
_count = 0
while i <= n:
    for aval in avals:
        if i % aval == 0:
            _sum += aval
            _count += 1
    i += 1

print(f"{_count} {_sum}")
