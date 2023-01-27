a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))
d = [0, 0]

if a[0] == b[0]: d[0] = c[0]
if b[0] == c[0]: d[0] = a[0]
if a[0] == c[0]: d[0] = b[0]

if a[1] == b[1]: d[1] = c[1]
if b[1] == c[1]: d[1] = a[1]
if a[1] == c[1]: d[1] = b[1]

print(f"{d[0]} {d[1]}")