n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
_sum = 0
while i < n:
    _sum += a[i] * b[i]
    i += 1
    
print(_sum)