args = input().split(' ')
n = int(args[0])
t = args[1]

chars = []
for ch in t:
    if ch not in chars:
        chars.append(ch)

results = []
while n > 0:
    inp = input()
    f = True
    for ch in inp:
        if ch not in chars:
            f = False
            break

    if f:
        for ch in t:
            if ch not in inp:
                f = False
                break
    if f:
        results.append('Yes')
    else:
        results.append('No')
    n -= 1

for r in results:
    print(r)