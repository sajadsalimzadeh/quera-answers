import math

n = input()
l = len(n)
b = 0
i = 0

while i < l:
    b += int(n[i])
    i += 1 


def isAval(n):
    if n < 2:
        return False
    i = 2
    s = math.ceil(n / 2)
    while i <= s:
        if n % i == 0:
            return False
        i += 1
    return True
    
i = int(n) + 1
while True:
    if isAval(i):
        b -= 1
    if b == 0:
        break
    i += 1
    
print(i)