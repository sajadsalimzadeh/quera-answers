inp = list(map(int, input().split()))
n = inp[0]
k = inp[1]

c = 1
s = k
while s != 0:
    if s == n:
        break
    if s > n:
        s -= n
    s += k
    c += 1

print(c)