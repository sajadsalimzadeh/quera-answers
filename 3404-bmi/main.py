n = int(input())
m = float(input())

bmi = n / (m * m)

print('{:.2f}'.format(bmi))
if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')
