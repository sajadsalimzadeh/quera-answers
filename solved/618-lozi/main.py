n = int(input())

i = 0
while i < n:
    j = 0
    while j < n * 2:
        if n - i <= j <= n + i:
            print('*', end='')
        else:
            print(' ', end='')
        j += 1
    print()
    i += 1

j = 0
while j <= n * 2:
    print('*', end='')
    j += 1
print()

i = n - 1
while i >= 0:
    j = 0
    while j < n * 2:
        if n - i <= j <= n + i:
            print('*', end='')
        else:
            print(' ', end='')
        j += 1
    print()
    i -= 1