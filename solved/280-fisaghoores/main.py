a = int(input())
b = int(input())
c = int(input())


def is_equal(a, b, c):
    return (a * a) == (b * b) + (c * c)


if is_equal(a, b, c) or is_equal(b, a, c) or is_equal(c, a, b):
    print('YES')
else:
    print('NO')
