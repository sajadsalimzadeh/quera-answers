n = int(input())

columns = []

_sum = 0
i = 0
while i < n:
    a = int(input())
    _sum += a
    columns.append(a)
    
    i += 1
    

avg = round(_sum/len(columns))
moves = 0
for c in columns:
    if c < avg:
        moves += avg - c
        
print(moves)