n = int(input())

pre = 0
c = 0
i = 0
while i < n:
    t = int(input())
    if t != pre and i > 0:
        c += 1
    pre = t
    i += 1

print(c)
