def sum_natural(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i

    return sum


if __name__ == '__main__':
    x = eval(input('Enter the value of n:'))
    print(f'The sum of {x} natural number is : {sum_natural(x)}')
