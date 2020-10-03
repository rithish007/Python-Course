a = eval(input('Enter the number a : '))
b = eval(input('Enter the number b : '))
c = eval(input('Enter the number c : '))
if a >= b and b >= c:
    print(f'{a} is the greatest number')
elif b >= a and b >= c:
    print(f'{b} is the greatest number')
else:
    print(f'{c} is the greatest number')
