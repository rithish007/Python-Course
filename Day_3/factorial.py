n = eval(input('Enter the value of n :'))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print(f'The factorial of {n} is : {factorial}')
