s = input()

count = 1
for c in s:
    if c == 'T':
        count += 1
for c in s:
    if c == 'D' or c == 'L' or c == 'F':
        count *= 2

print(count)