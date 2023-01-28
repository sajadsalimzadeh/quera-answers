n = int(input())
a = list(map(int, input().split()))

result = []
i = 0
while i < n:
    if a[i] <= 3:
        result.append(a[i])
    else:
        result.append(1)
    i += 1
    
for item in result:
    i = 0
    while i < item:
        print('*', end='')
        i += 1
    print()