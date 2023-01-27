import math

inputs = input().split(' ')
n = int(inputs[0])
k = int(inputs[1])

while k > 0:
    n /= 2
    k -= 1

print(math.floor(n))
