import math
args = list(map(int, input().split()))
n = args[0]
m = args[1]

bmm = math.gcd(n,m)
kmm = round(n * m / bmm)

print(bmm, kmm)