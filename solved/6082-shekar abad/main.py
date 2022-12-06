inputs = input().split(' ')
n = int(inputs[0])
m = int(inputs[1])

i = 0
stars = 0
while i < n:
    inp = input()
    stars += inp.count('*')
    i += 1

print(stars)