n = int(input())
w = list(map(int, input().split(' ')))

wc = w.copy()
_min = 0
i = 0
while i < n - 1:
    _min = min(w[0], w[1])
    w.remove(_min)
    i += 1

print(wc.index(w[0]) + 1)
