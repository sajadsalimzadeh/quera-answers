x1 = input()
op = input()
x2 = input()

if op == '+':
    l1 = len(x1) - 1
    l2 = len(x2) - 1
    if l1 > l2:
        s = list(x1)
        s[l1 - l2] = (int(s[l1 - l2]) + 1).__str__()
        x1 = ''.join(s)
        print(x1)
    else:
        s = list(x2)
        s[l2 - l1] = (int(s[l2 - l1]) + 1).__str__()
        x2 = ''.join(s)
        print(x2)
else:
    l = len(x1) + len(x2) - 2
    print('1' + ('0' * l))