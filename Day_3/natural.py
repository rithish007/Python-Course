n = eval(input('Enter the value of n :'))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f'The sum of {n} natural numbers is : {sum}')

"""
    i = 0   i < 5 + 1       i < 6   0 < 6
        sum = sum + 1
            = 0 + 0

    i = 1   1 < 6 
             = 0 + 1
             sum = 1        i = 1 + 1

    i = 2   2 < 6
             = 1 + 2
             sum = 3        i = 1 + 2
    
    i = 3   3 < 6
             = 1 + 3
             sum = 4        i = 1 + 4

    i = 4   4 < 6
             = 1 + 4        i = 1 + 4
             sum = 5
    i = 5   5 < 6
             = 1 + 5        i = 1 + 5
             sum = 6
    i = 6   6 < 6
            Loop Terminated

"""
