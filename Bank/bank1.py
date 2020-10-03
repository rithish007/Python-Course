import sys

main_bal = 10000

restart = "Yes"
while (1):
    print ("Press 1  To withdraw\nPress 2  To deposit\nPress 3  To transfer\nPress 4  To check the balance\npress 5  Exit")
    int = eval(input('Enter the choice: '))
    restart[0] == 'Y' or restart[0] == 'y'
    if (int='1'):
        print(f'Enter the amount to withdraw = ')
        
        restart = input('Do you want to continue. press (Yes/No)')
    elif (int='2'):
        print(f'Enter the amount to deposit:      ')
        new_bal = 10000 + deposit
        print(f'The current balance is {new_balance}')
        restart = input('Do you want to continue. press (Yes/No)')
    else:
        print(f'exiting...')