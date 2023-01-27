args = list(map(int, input().split()))
n = args[0]
m = args[1]

costs = []
i = 0
while i < n:
    cost = list(map(int, input().split()))
    costs.append(cost)
    i += 1

travels = []
i = 0
while i < m:
    travel = list(map(int, input().split()))
    travels.append(travel)
    i += 1

_sum = 0
i = 0
while i < m:
    travel = travels[i]
    cost = costs[travel[0] - 1][travel[1] - 1]
    _sum += cost
    i += 1

print(_sum)
