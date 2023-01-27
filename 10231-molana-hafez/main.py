n = 5
inputs = list(range(n))

i = 0
while i < n:
    inputs[i] = input()
    i += 1

finds = []
i = 1
while i <= n:
    inp = inputs[i - 1]
    if inp.find('HAFEZ') > -1 or inp.find('MOLANA') > -1:
        finds.append(i.__str__())
    i += 1

if len(finds) > 0:
    print(' '.join(finds))
else:
    print('NOT FOUND!')
