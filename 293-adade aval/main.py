# import the math module 
import math 

a = int(input())
b = int(input())

def isAval(n):
    if n < 2:
        return False
    i = 2
    s = math.sqrt(n)
    while i <= s:
        if n % i == 0:
            return False
        i += 1
    return True

start = 0
end = 0
if a > b:
    start = b
    end = a
else:
    start = a
    end = b

i = start
while i <= end:
    if isAval(i):
        print(i)
    i += 1