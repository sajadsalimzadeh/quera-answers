n = int(input())

max_r = 0
i = 0
while i < n:
    inp = input()
    r = 0
    chars = []
    for c in inp:
        if c not in chars:
            chars.append(c)
            r += 1
    if r > max_r:
        max_r = r
    i += 1

print(max_r)
