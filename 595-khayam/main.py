n = int(input())

pre_row = []
i = 0
while i < n:
    row = []
    j = 0
    while j < i:
        if j == 0:
            row.append(pre_row[j])
        else:
            row.append(pre_row[j - 1] + pre_row[j])
        j += 1
    pre_row = row
    pre_row.append(1)
    print(' '.join(map(str, pre_row)))
    i += 1

