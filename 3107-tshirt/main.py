t = list(map(int, input().split()))
f = list(map(int, input().split()))

if t[0] >= f[0] and t[1] >= f[1]:
    print('yes')
else:
    print('no')