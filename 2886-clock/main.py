inp = list(map(int, input().split()))
a = inp[0]
b = inp[1]

if a > 0:
    a = 12 - a
if b > 0:
    b = 60 - b

if a < 10:
    a = "0" + a.__str__()

if b < 10:
    b = "0" + b.__str__()

print(f"{a}:{b}")