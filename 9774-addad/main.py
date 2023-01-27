inp = input()
l = len(inp)

i = 0
while i < l:
    s = inp[i]
    t = int(s)
    print(s + ": ", end='')
    while t > 0:
        print(s, end='')
        t -= 1
    print()
    i += 1
