n = int(input())

names = []

while n > 0:
    inp = list(input())
    i = 0
    l = len(inp)
    while i < l:
        if i == 0 or inp[i - 1] == ' ':
            inp[i] = inp[i].upper()
        else:
            inp[i] = inp[i].lower()
        i += 1
    names.append(''.join(inp))
    n -= 1

for name in names:
    print(name)