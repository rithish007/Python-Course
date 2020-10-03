import sys

class BankAccount:
    def __init__ (self, uname, upass, Balance = 10000):
        self.uname = Username
        self.upass = Password
        self.Balance = Balance

    def id(self):
        self.id
        print(f"Enter the user name : \t")

    def deposit(self):
        amt = eval(input("Enter the amount to deposit"))
        self.Balance += amt
        print(f"\nThe current balance is = {self.Balance}")

    def withdraw(self):
        withdraw = eval(input("Enter the amount to withdraw"))
        self.Balance -= withdraw
        print(f'\nThe current balance is = {self.Balance}')

    def transfer(self):
        transfer = eval(input("Enter the amount to transfer"))
        self.Balance -= transfer
        print(f'\nThe current balance is = {self.Balance}')


if __name__ == "__main__":
    while():
        print(f"\nPress 1  to Deposit\nPress 2  to Withdraw\nPress 3  to Transfer")
        selection = int(input('Enter the Choice = '))
        
        if (selection == 1):
            print(f'Enter the amount to DEPOSIT = ')
            
        elif (selection == 2):
            print(f'Enter the amount to WITHDRAW = ')
            
        elif (selection == 3):
            print(f'Enter the amount to TRANSFER = ')
            
        else:
            print(f'Exiting...')
            sys.exit
            

ob = BankAccount(self)
ob.self_uname = "Bank"
ob.self_upass = "Bank@123"

ob.id_self()

