inp = list(map(int, input().split()))
n = inp[0]
k = inp[1]
a = list(map(int, input().split()))

b = 0
i = 1
while i < n:
    if a[b] < k and a[i] > 0:
        a[i] -= 1
        a[b] += 1
    if a[b] == k:
        b += 1
    if a[i] == 0 or i <= b:
        i += 1

i = 0
c = 0
while i < n:
    if a[i] == 0:
        c += 1
    i += 1
print(c)