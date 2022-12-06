t = int(input())

arr = []

i = 0
while i < t:
    inp = list(map(int, input().split()))
    if inp[0] == 0 or inp[1] == 0:
        if inp[0] == 0 and inp[1] == 0:
            arr.append(0)
        else:
            arr.append(-1)
    elif inp[0] % 2 == 0 and (inp[0] == inp[1] or inp[1] == inp[0] - 2):
        arr.append(inp[0] + inp[1])
    elif inp[0] % 2 == 1 and (inp[0] == inp[1] or inp[1] == inp[0] - 2):
        arr.append(inp[0] + inp[1] - 1)
    else:
        arr.append(-1)
    i += 1

for item in arr:
    print(item)