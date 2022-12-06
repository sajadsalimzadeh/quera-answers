inp = list(map(int, input().split()))
x1 = inp[0]
x2 = inp[1]

if x1 == x2:
    print('Saal Noo Mobarak!')
elif x1 < x2:
    i = x1
    while i < x2:
        print('R', end='')
        i += 1
elif x1 > x2:
    i = x1
    while i > x2:
        print('L', end='')
        i -= 1