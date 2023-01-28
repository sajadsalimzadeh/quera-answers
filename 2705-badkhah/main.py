inp = list(map(int, input().split()))
p = inp[0]
d = inp[1]

s = d
i = 1
while (s % p) > (p / 2):
    s = d * i
    i += 1

print(s)