# Reading
name = input('Enter the student name: ')

a, b, c, d, e = eval(input('Enter the marks: \t'))

# Total

Total = a + b + c + d + e
print(f'The Total marks of {name} is :\t{Total}')

# Average

Avg = (Total/5)

print(f'The avg marks of {name} is {Avg}')

# Grading

if (Total >= 90):
    print(f'A')
elif (Total >= 80):
    print(f'B')
elif (Total >= 70):
    print(f'C')
elif (Total >= 60):
    print(f'D')
else:
    print(f'FAIL')
