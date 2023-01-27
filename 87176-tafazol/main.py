
def game(number):
    number = number.__str__()
    x1 = int(number[0])
    x2 = int(number[1])
    if x1 > x2:
        return x1 - x2
    return x2 - x1
