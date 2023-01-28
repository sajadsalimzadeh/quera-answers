n = input()

status = 'YES'
len_n = len(n) / 2
i = 0
while(i < len_n):
    if(n[i] != n[-i - 1]):
        status = 'NO'
        break
    i += 1

print(status)   