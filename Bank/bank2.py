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
        print(f'\nAmount Deposited\t{amt}')

    def withdraw(self):
        withdraw = eval(input("Enter the amount to withdraw"))
        self.Balance -= withdraw
        print(f'\nThe current balance is = {self.Balance}')
        print(f'\nWithdrawn Amount\t{withdraw}')

    def transfer(self):
        transfer = eval(input("Enter the amount to transfer"))
        self.Balance -= transfer
        print(f'\nThe current balance is = {self.Balance}')
        print(f'\nAmount Transffered\t{transfer}')





if __name__ == "__main__":
    restart = "Yes"
    while(1):
        print(f"\nPress 1  to Deposit\nPress 2  to Withdraw\nPress 3  to Transfer\nPress 4  to Exit")
        input = eval(input('Enter the Choice = '))
        restart[0] == 'Y' or restart[0] == 'y'
        if (input == 1):
            print(f'Enter the amount to DEPOSIT = {amt}')
            restart = input('Do you want to continue. press (Yes/No)')
        elif (input == 2):
            print(f'Enter the amount to WITHDRAW = {withdraw}')
            restart = input('Do you want to continue. press (Yes/No)')
        elif (input == 3):
            print(f'Enter the amount to TRANSFER = {transfer}')
            restart = input('Do you want to continue. press (Yes/No)')
        else:
            print(f'Exiting...')
            restart = input('Do you want to continue. press (Yes/No)')

ob = BankAccount(self)
ob.self_uname = "Bank"
ob.self_upass = "Bank@123"

ob.id_self()

