k = int(input())
p = input()

inps = []
i = 0
while i < k:
    inps.append(input())
    i += 1

c = 0
i = 0
while i < k:
    inp = inps[i]
    inp_len = len(inp)
    ch = p[i]
    index = inp.index(ch)
    if index > inp_len / 2:
        index = inp_len - index
    c += index
    i += 1
print(c)