restart = "yes"
while restart[0] == "y" or restart[0] == "Y":
    n1, n2, n3, n4, n5 = eval(input('Enter the value of n1,n2,n3,n4,n5 :'))
    sum = n1 + n2 + n3 + n4 + n5
    print(f'The sum of natural numbers is : {sum}')
    restart = input('Do you want to continue. press (Yes/No)')
