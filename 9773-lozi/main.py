import math

n = int(input())

middle = math.floor(n / 2)


def get_row(space):
    str_row = ''
    col = 0
    while col < n:
        if (middle - space) <= col <= (middle + space):
            str_row += '*'
        else:
            str_row += ' '
        col += 1
    return str_row


space = 0
row = 0
while row < n:
    print(get_row(space) + get_row(space))
    if row > middle - 1:
        space -= 1
    else:
        space += 1

    row += 1
