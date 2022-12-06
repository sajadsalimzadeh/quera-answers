inp = list(map(int, input().split()))
n = inp[0]
k = inp[1]

i = 0
_sum = 0
while i < n:
    _sum += int(input())
    i += 1

if _sum >= k:
    print('YES')
else:
    print('NO')