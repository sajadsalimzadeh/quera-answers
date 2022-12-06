import math

n = 4
nums = []

_sum = 0
product = 1
_max = -100000
_min = 1000000

i = 0
while i < n:
    num = int(input())
    if num > _max:
        _max = num
    if num < _min:
        _min = num
    _sum += num
    product *= num
    i += 1

print('Sum : {:.6f}'.format(_sum))
print('Average : {:.6f}'.format(_sum / n))
print('Product : {:.6f}'.format(product))
print('MAX : {:.6f}'.format(_max))
print('MIN : {:.6f}'.format(_min))

