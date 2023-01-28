import math
inp = input()

sedadar = ['a','e', 'i', 'o', 'u']

c = 0
for ch in inp:
    if ch.lower() in sedadar:
        c += 1

print(round(math.pow(2,c)))