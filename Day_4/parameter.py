def printmyname(name):
    print(f'I\'m printing the function parameter name: {name}')


def add(a, b):
    return a+b, a, b


if __name__ == "__main__":
    printmyname('Sample Name')
    ans, x, y = add(5, 6)
    print(f'Ans : {x} + {y} = {ans}')
